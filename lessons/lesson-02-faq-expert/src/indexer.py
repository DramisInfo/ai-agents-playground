"""
Document Indexer for Lesson 2: FAQ Expert
Uses lightweight markdown parsing (no heavy ML dependencies!) with HybridChunker from docling-core.
"""

import os
import time
import re
import warnings
from pathlib import Path
from typing import List, Dict
import psycopg2
from psycopg2.extras import Json
from pgvector.psycopg2 import register_vector
import frontmatter

# Suppress transformers warning (docling-core imports it for tokenization but we don't need models)
warnings.filterwarnings('ignore', message='.*PyTorch.*TensorFlow.*Flax.*')

from docling_core.types.doc import DoclingDocument, TextItem, DocItemLabel
from docling_core.transforms.chunker import HybridChunker
from openai import OpenAI
import ollama
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class DocumentIndexer:
    """Indexes knowledge base documents into pgvector."""
    
    def __init__(self):
        """Initialize the document indexer."""
        self.conn = None
        # Use HybridChunker from docling-core (lightweight, no ML dependencies!)
        self.chunker = HybridChunker(max_tokens=512)
        
        # Configure embedding provider based on environment
        self.embedding_provider = os.getenv("EMBEDDING_PROVIDER", "github").lower()
        
        if self.embedding_provider == "ollama":
            self.ollama_host = os.getenv("OLLAMA_HOST", "http://host.docker.internal:11434")
            self.ollama_model = os.getenv("OLLAMA_EMBEDDING_MODEL", "nomic-embed-text")
            self.embedding_dimensions = int(os.getenv("EMBEDDING_DIMENSIONS", "768"))
            print(f"🤖 Using Ollama embeddings: {self.ollama_model} ({self.embedding_dimensions}D) at {self.ollama_host}")
        elif self.embedding_provider == "lmstudio":
            # LM Studio provides OpenAI-compatible API
            lmstudio_url = os.getenv("LMSTUDIO_URL", "http://host.docker.internal:1234/v1")
            self.lmstudio_model = os.getenv("LMSTUDIO_MODEL", "text-embedding-nomic-embed-text-v2")
            self.embedding_dimensions = int(os.getenv("EMBEDDING_DIMENSIONS", "768"))
            self.openai_client = OpenAI(
                base_url=lmstudio_url,
                api_key="lm-studio"  # LM Studio doesn't require a real key
            )
            print(f"💻 Using LM Studio embeddings: {self.lmstudio_model} ({self.embedding_dimensions}D) at {lmstudio_url}")
        else:
            self.openai_client = OpenAI(
                base_url="https://models.github.ai/inference",
                api_key=os.getenv("GITHUB_TOKEN")
            )
            self.embedding_dimensions = 1536  # text-embedding-3-small dimensions
            print(f"🌐 Using GitHub Models embeddings: text-embedding-3-small ({self.embedding_dimensions}D)")
        
    def connect_db(self):
        """Connect to PostgreSQL database."""
        max_retries = 30
        retry_interval = 2
        
        for attempt in range(max_retries):
            try:
                self.conn = psycopg2.connect(
                    host=os.getenv("POSTGRES_HOST", "postgres"),
                    port=int(os.getenv("POSTGRES_PORT", 5432)),
                    database=os.getenv("POSTGRES_DB", "techflow"),
                    user=os.getenv("POSTGRES_USER", "techflow_user"),
                    password=os.getenv("POSTGRES_PASSWORD", "techflow_pass_change_in_production")
                )
                register_vector(self.conn)
                print(f"✓ Connected to PostgreSQL database")
                return
            except psycopg2.OperationalError as e:
                if attempt < max_retries - 1:
                    print(f"⏳ Waiting for database... (attempt {attempt + 1}/{max_retries})")
                    time.sleep(retry_interval)
                else:
                    raise Exception(f"Failed to connect to database after {max_retries} attempts: {e}")
    
    def get_embedding(self, text: str) -> List[float]:
        """
        Generate embeddings for text using configured provider (GitHub Models, Ollama, or LM Studio).
        
        Args:
            text: Text to embed
            
        Returns:
            List of float values representing the embedding (dimensions vary by model)
        """
        try:
            if self.embedding_provider == "ollama":
                # Use local Ollama for embeddings (no rate limits!)
                response = ollama.embeddings(
                    model=self.ollama_model,
                    prompt=text,
                    options={"host": self.ollama_host}
                )
                return response["embedding"]
            elif self.embedding_provider == "lmstudio":
                # Use LM Studio with OpenAI-compatible API
                response = self.openai_client.embeddings.create(
                    model=self.lmstudio_model,
                    input=text
                )
                return response.data[0].embedding
            else:
                # Use GitHub Models for embeddings
                response = self.openai_client.embeddings.create(
                    model="openai/text-embedding-3-small",
                    input=text
                )
                return response.data[0].embedding
        except Exception as e:
            print(f"    ⚠️  Warning: Failed to generate embedding: {e}")
            # Return zero vector as fallback
            return [0.0] * self.embedding_dimensions
    

    
    def markdown_to_docling_document(self, content: str, title: str) -> DoclingDocument:
        """
        Convert markdown content to a DoclingDocument for HybridChunker.
        
        Args:
            content: Markdown content
            title: Document title
            
        Returns:
            DoclingDocument object
        """
        doc = DoclingDocument(name=title)
        
        # Split content by paragraphs and add as text items
        paragraphs = [p.strip() for p in content.split('\n\n') if p.strip()]
        
        for para in paragraphs:
            # Detect if it's a heading (starts with #)
            if para.startswith('#'):
                label = DocItemLabel.SECTION_HEADER
            else:
                label = DocItemLabel.PARAGRAPH
            
            doc.add_text(text=para, label=label)
        
        return doc
    
    def store_document(self, file_path: Path, title: str, chunks: List):
        """
        Store document and its chunks with embeddings in the database.
        
        Args:
            file_path: Path to the document
            title: Document title
            chunks: List of text chunks
        """
        cursor = self.conn.cursor()
        
        try:
            # Insert or update document
            cursor.execute(
                "SELECT id FROM kb_documents WHERE filepath = %s",
                (str(file_path),)
            )
            existing = cursor.fetchone()
            
            if existing:
                document_id = existing[0]
                cursor.execute("DELETE FROM kb_chunks WHERE document_id = %s", (document_id,))
                cursor.execute(
                    "UPDATE kb_documents SET title=%s, file_size=%s, updated_at=NOW(), indexed_at=NOW() WHERE id=%s",
                    (title, file_path.stat().st_size, document_id)
                )
            else:
                cursor.execute(
                    "INSERT INTO kb_documents (filename, filepath, title, content_type, file_size, indexed_at) VALUES (%s, %s, %s, %s, %s, NOW()) RETURNING id",
                    (file_path.name, str(file_path), title, "text/markdown", file_path.stat().st_size)
                )
                document_id = cursor.fetchone()[0]
            
            # Store chunks with embeddings
            print(f"  🔄 Generating embeddings for {len(chunks)} chunks...")
            for idx, chunk in enumerate(chunks):
                # Get context-enriched text from HybridChunker
                enriched_text = self.chunker.contextualize(chunk=chunk)
                
                # Generate embedding from enriched text
                embedding = self.get_embedding(enriched_text)
                
                # Store chunk with raw text
                cursor.execute(
                    "INSERT INTO kb_chunks (document_id, chunk_index, content, embedding, metadata) VALUES (%s, %s, %s, %s, %s)",
                    (document_id, idx, chunk.text.strip(), embedding, Json({"tokens": len(chunk.text.split())}))
                )
            
            self.conn.commit()
            print(f"  ✓ Stored {len(chunks)} chunks with embeddings")
            
        except Exception as e:
            self.conn.rollback()
            print(f"  ✗ Error storing document: {e}")
            raise
        finally:
            cursor.close()
    
    def index_knowledge_base(self, kb_path: Path):
        """
        Index all markdown files in the knowledge base directory using batch processing.
        
        Args:
            kb_path: Path to the knowledge base directory
        """
        if not kb_path.exists():
            raise ValueError(f"Knowledge base path does not exist: {kb_path}")
        
        # Find all markdown files
        md_files = sorted(kb_path.glob("*.md"))
        
        if not md_files:
            print(f"⚠️  No markdown files found in {kb_path}")
            return
        
        print(f"\n📚 Found {len(md_files)} documents to index\n")
        print(f"🔄 Processing markdown files...\n")
        
        # Process each markdown file
        for file_path in md_files:
            try:
                print(f"  📄 Processing: {file_path.name}")
                
                # Read markdown file with frontmatter
                with open(file_path, 'r', encoding='utf-8') as f:
                    post = frontmatter.load(f)
                
                # Extract title (from frontmatter or filename)
                title = post.get('title', file_path.stem.replace("-", " ").title())
                
                # Get content
                content = post.content
                
                # Convert to DoclingDocument
                doc = self.markdown_to_docling_document(content, title)
                
                # Chunk using HybridChunker
                chunks = [c for c in self.chunker.chunk(doc) if c.text.strip()]
                
                print(f"    ✓ Generated {len(chunks)} chunks")
                
                # Store in database
                self.store_document(file_path, title, chunks)
                
            except Exception as e:
                print(f"  ✗ Failed to process {file_path.name}: {e}")
                continue
        
        print(f"\n✅ Indexing complete!\n")
    
    def close(self):
        """Close database connection."""
        if self.conn:
            self.conn.close()


def main():
    """Main indexing function."""
    print("=" * 60)
    print("  TechFlow Knowledge Base Indexer (Lesson 2)")
    print("=" * 60)
    
    # Path to knowledge base
    kb_path = Path(__file__).parent.parent / "knowledge-base"
    
    print(f"\n📁 Knowledge base path: {kb_path}\n")
    
    # Create indexer
    indexer = DocumentIndexer()
    
    try:
        # Connect to database
        indexer.connect_db()
        
        # Index all documents
        indexer.index_knowledge_base(kb_path)
        
    except Exception as e:
        print(f"\n❌ Indexing failed: {e}\n")
        raise
    finally:
        indexer.close()


if __name__ == "__main__":
    main()
