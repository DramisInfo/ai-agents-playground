"""
AI-powered FAQ Expert with RAG (Retrieval-Augmented Generation).
Uses vector search to find relevant knowledge and generates accurate answers.
"""

import asyncio
import time
import os
from typing import Optional, List, Dict
import psycopg2
from psycopg2.extras import RealDictCursor
from pgvector.psycopg2 import register_vector
from fastapi import HTTPException
from agent_framework import ChatAgent
from agent_framework.openai import OpenAIChatClient
from openai import OpenAI

# Global agent instance
_agent: Optional[ChatAgent] = None
_agent_lock = asyncio.Lock()
_db_connection = None


def get_db_connection():
    """Get or create database connection."""
    global _db_connection
    
    if _db_connection is None or _db_connection.closed:
        _db_connection = psycopg2.connect(
            host=os.getenv("POSTGRES_HOST", "localhost"),
            port=os.getenv("POSTGRES_PORT", "5432"),
            database=os.getenv("POSTGRES_DB", "techflow"),
            user=os.getenv("POSTGRES_USER", "techflow_user"),
            password=os.getenv("POSTGRES_PASSWORD", "techflow_pass_change_in_production")
        )
        register_vector(_db_connection)
    
    return _db_connection


def generate_embedding(text: str) -> List[float]:
    """
    Generate embedding for a query using the same provider as indexing.
    
    Args:
        text: Text to embed
        
    Returns:
        Embedding vector
    """
    embedding_provider = os.getenv("EMBEDDING_PROVIDER", "github").lower()
    
    if embedding_provider == "github":
        # Use GitHub Models for embeddings
        client = OpenAI(
            base_url="https://models.inference.ai.azure.com",
            api_key=os.getenv("GITHUB_TOKEN")
        )
        response = client.embeddings.create(
            input=text,
            model="text-embedding-3-small"
        )
        return response.data[0].embedding
    
    elif embedding_provider == "ollama":
        import ollama
        ollama_host = os.getenv("OLLAMA_HOST", "http://localhost:11434")
        ollama_model = os.getenv("OLLAMA_EMBEDDING_MODEL", "nomic-embed-text")
        
        # Parse host to extract hostname without http://
        import urllib.parse
        parsed = urllib.parse.urlparse(ollama_host)
        host = parsed.netloc or parsed.path
        
        response = ollama.Client(host=f"http://{host}").embeddings(
            model=ollama_model,
            prompt=text
        )
        return response["embedding"]
    
    elif embedding_provider == "lmstudio":
        lmstudio_url = os.getenv("LMSTUDIO_URL", "http://localhost:1234/v1")
        lmstudio_model = os.getenv("LMSTUDIO_MODEL", "text-embedding-nomic-embed-text-v2")
        
        client = OpenAI(
            base_url=lmstudio_url,
            api_key="lm-studio"
        )
        response = client.embeddings.create(
            input=text,
            model=lmstudio_model
        )
        return response.data[0].embedding
    
    else:
        raise ValueError(f"Unsupported embedding provider: {embedding_provider}")


def search_knowledge_base(query: str, top_k: int = 3) -> List[Dict]:
    """
    Search the knowledge base using vector similarity.
    
    Args:
        query: User's question
        top_k: Number of results to return
        
    Returns:
        List of relevant knowledge chunks with metadata
    """
    conn = get_db_connection()
    
    # Generate embedding for the query
    query_embedding = generate_embedding(query)
    
    # Search for similar chunks using cosine similarity
    with conn.cursor(cursor_factory=RealDictCursor) as cur:
        cur.execute("""
            SELECT 
                c.content,
                c.metadata,
                d.title,
                d.filename,
                1 - (c.embedding <=> %s::vector) as similarity
            FROM kb_chunks c
            JOIN kb_documents d ON c.document_id = d.id
            WHERE c.embedding IS NOT NULL
            ORDER BY c.embedding <=> %s::vector
            LIMIT %s
        """, (query_embedding, query_embedding, top_k))
        
        results = cur.fetchall()
    
    return [dict(row) for row in results]


async def get_agent() -> ChatAgent:
    """
    Get or create the FAQ Expert agent with RAG capabilities.
    
    Returns:
        ChatAgent instance configured for knowledge retrieval
    """
    global _agent
    
    async with _agent_lock:
        if _agent is None:
            # Get configuration from environment
            api_key = os.getenv("GITHUB_TOKEN")
            model_id = os.getenv("GITHUB_MODEL", "gpt-4o-mini")
            
            if not api_key:
                raise ValueError(
                    "GITHUB_TOKEN environment variable is required. "
                    "Get your free token at https://github.com/settings/tokens"
                )
            
            # Create chat client for GitHub Models
            chat_client = OpenAIChatClient(
                model_id=model_id,
                api_key=api_key,
                base_url="https://models.inference.ai.azure.com"
            )
            
            # Create the AI agent with RAG instructions
            _agent = ChatAgent(
                chat_client=chat_client,
                instructions="""You are an expert FAQ assistant for FlowCRM and FlowAnalytics products.

Your role is to answer customer questions using the provided knowledge base context.

Guidelines:
1. **Use the provided context**: Base your answers on the knowledge base chunks provided
2. **Be accurate**: Only provide information that's in the context - don't make things up
3. **Be helpful**: If the context doesn't contain the answer, say so and suggest alternatives
4. **Be concise**: Provide clear, direct answers without unnecessary details
5. **Cite sources**: When referencing specific features or steps, mention which document they're from
6. **Format nicely**: Use bullet points and clear structure when appropriate

If the question cannot be answered with the provided context:
- Acknowledge what you don't know
- Suggest related topics that might help
- Recommend contacting support for specialized questions

Always maintain a professional, friendly tone.""",
                name="FlowCRM_FAQ_Expert"
            )
        
        return _agent


async def run_agent_with_context(question: str, context_chunks: List[Dict]) -> str:
    """
    Run the agent with retrieved context to answer the question.
    
    Args:
        question: User's question
        context_chunks: Retrieved knowledge chunks
        
    Returns:
        Generated answer
    """
    agent = await get_agent()
    
    # Build context from retrieved chunks
    context_text = "\n\n---\n\n".join([
        f"**Source: {chunk['title']}** (similarity: {chunk['similarity']:.2%})\n{chunk['content']}"
        for chunk in context_chunks
    ])
    
    # Create the prompt with context
    prompt = f"""Please answer the following question based on the provided knowledge base context:

QUESTION: {question}

KNOWLEDGE BASE CONTEXT:
{context_text}

Please provide a helpful, accurate answer based on the context above."""
    
    # Get response from agent
    response = await agent.run(prompt)
    
    # Extract text from response
    if hasattr(response, 'text'):
        return response.text
    elif hasattr(response, 'content'):
        return response.content
    else:
        return str(response)


def process_faq_ai(question: str) -> dict:
    """
    Process an FAQ question using RAG-powered AI agent.
    
    Args:
        question: The user's question
        
    Returns:
        dict with response details including sources
    """
    start_time = time.time()
    
    try:
        # Step 1: Search knowledge base for relevant context
        search_start = time.time()
        context_chunks = search_knowledge_base(question, top_k=3)
        search_time = time.time() - search_start
        
        if not context_chunks:
            return {
                "question": question,
                "answer": "I couldn't find relevant information in the knowledge base. Please contact support for assistance.",
                "mode": "ai-rag",
                "sources": [],
                "search_time": round(search_time, 3),
                "total_time": round(time.time() - start_time, 3)
            }
        
        # Step 2: Generate answer using LLM with context
        generation_start = time.time()
        answer = asyncio.run(run_agent_with_context(question, context_chunks))
        generation_time = time.time() - generation_start
        
        # Extract sources
        sources = [
            {
                "title": chunk["title"],
                "filename": chunk["filename"],
                "similarity": round(chunk["similarity"], 3)
            }
            for chunk in context_chunks
        ]
        
        total_time = time.time() - start_time
        
        print(f"[AI-RAG] Question processed in {total_time:.2f}s (search: {search_time:.3f}s, generation: {generation_time:.3f}s)")
        
        return {
            "question": question,
            "answer": answer,
            "mode": "ai-rag",
            "sources": sources,
            "search_time": round(search_time, 3),
            "generation_time": round(generation_time, 3),
            "total_time": round(total_time, 3)
        }
    
    except Exception as e:
        print(f"[ERROR] AI processing failed: {str(e)}")
        raise HTTPException(status_code=500, detail=f"AI processing error: {str(e)}")
