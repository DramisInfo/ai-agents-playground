"""
AI-powered FAQ Expert with RAG (Retrieval-Augmented Generation).
Uses tools for vector search - agent decides when to retrieve knowledge.
"""

import asyncio
import time
import os
import json
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


async def search_knowledge_base_tool(query: str, top_k: int = 3) -> str:
    """
    Search the FlowCRM/FlowAnalytics knowledge base for relevant documentation.
    
    Use this tool when you need to find information about:
    - FlowCRM features (contacts, email integration, workflows, etc.)
    - FlowAnalytics features (data sources, dashboards, reports, etc.)
    - How-to guides and step-by-step instructions
    - Troubleshooting and technical support
    - Best practices and recommendations
    - Account and permission management
    
    Args:
        query: Search query - use specific keywords from the user's question
               Examples: "import contacts CSV", "email integration setup", "user permissions"
        top_k: Number of results to return (default: 3, max: 5)
    
    Returns:
        JSON string containing relevant knowledge base articles with their content,
        titles, source files, and similarity scores.
    """
    # Limit top_k to reasonable bounds
    top_k = max(1, min(top_k, 5))
    
    try:
        results = search_knowledge_base(query, top_k)
        
        if not results:
            return json.dumps({
                "results": [],
                "count": 0,
                "message": "No relevant documentation found for this query."
            }, indent=2)
        
        # Format results for the agent
        formatted_results = {
            "results": [
                {
                    "content": chunk["content"],
                    "title": chunk["title"],
                    "source_file": chunk["filename"],
                    "relevance_score": round(chunk["similarity"], 3)
                }
                for chunk in results
            ],
            "count": len(results),
            "query": query
        }
        
        return json.dumps(formatted_results, indent=2)
    
    except Exception as e:
        return json.dumps({
            "error": f"Failed to search knowledge base: {str(e)}",
            "results": [],
            "count": 0
        }, indent=2)


async def get_agent() -> ChatAgent:
    """
    Get or create the FAQ Expert agent with tool-based RAG capabilities.
    
    Returns:
        ChatAgent instance configured with knowledge base search tool
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
            
            # Create the AI agent with tool-based RAG instructions
            _agent = ChatAgent(
                chat_client=chat_client,
                instructions="""You are an expert FAQ assistant for FlowCRM and FlowAnalytics products.

Your role is to answer customer questions by using the search_knowledge_base tool to find relevant documentation.

How to answer questions:
1. **Search first**: Use the search_knowledge_base tool with specific keywords from the user's question
2. **Multiple searches**: You can search multiple times with different queries if needed
3. **Combine information**: If multiple sources are needed, make additional searches
4. **Be accurate**: Only provide information from the search results - don't make things up
5. **Cite sources**: Reference the document titles and be specific about where information comes from
6. **Be concise**: Provide clear, helpful answers without unnecessary details

Tool usage tips:
- Use specific keywords: "import CSV contacts" is better than "how to add people"
- Search for related topics if the first search doesn't have enough information
- Use top_k=3 for most questions, increase to 5 for complex topics

If you can't find the answer after searching:
- Acknowledge what you don't know
- Suggest related topics that might help
- Recommend contacting support for specialized questions

Always maintain a professional, friendly tone and format your answers clearly.""",
                name="FlowCRM_FAQ_Expert",
                tools=[search_knowledge_base_tool]  # Register the search tool
            )
        
        return _agent


async def run_agent_with_tools(question: str) -> tuple[str, List[Dict]]:
    """
    Run the agent with tool-based RAG - agent decides when to search.

    Args:
        question: User's question

    Returns:
        Tuple of (answer text, list of tool calls made)
    """
    agent = await get_agent()

    # Simply ask the question - agent will use tools as needed
    response = await agent.run(question)

    # Extract the answer text
    if hasattr(response, 'text'):
        answer = response.text
    elif hasattr(response, 'content'):
        answer = response.content
    else:
        answer = str(response)

    # Extract tool calls to track what the agent searched for
    tool_calls = []
    if hasattr(response, 'messages'):
        for msg in response.messages:
            if hasattr(msg, 'tool_calls') and msg.tool_calls:
                for tc in msg.tool_calls:
                    if hasattr(tc, 'function'):
                        tool_calls.append({
                            "tool": tc.function.name,
                            "arguments": json.loads(tc.function.arguments) if isinstance(tc.function.arguments, str) else tc.function.arguments
                        })

    return answer, tool_calls


def process_faq_ai(question: str) -> dict:
    """
    Process an FAQ question using tool-based RAG AI agent.

    The agent autonomously decides when and how to search the knowledge base.

    Args:
        question: The user's question

    Returns:
        dict with response details including tool calls and sources
    """
    start_time = time.time()

    try:
        # Let the agent handle the question using tools
        answer, tool_calls = asyncio.run(run_agent_with_tools(question))

        total_time = time.time() - start_time

        # Extract sources from tool calls
        sources = []
        search_queries = []

        for tc in tool_calls:
            if tc["tool"] == "search_knowledge_base_tool":
                query = tc["arguments"].get("query", "")
                search_queries.append(query)

        # For source tracking, do a quick search with the last query used
        # (in a production system, you'd capture this from tool results)
        if search_queries:
            last_search = search_knowledge_base(search_queries[-1], top_k=3)
            sources = [
                {
                    "title": chunk["title"],
                    "filename": chunk["filename"],
                    "similarity": round(chunk["similarity"], 3)
                }
                for chunk in last_search
            ]

        print(f"[AI-RAG-TOOL] Question processed in {total_time:.2f}s")
        print(f"[AI-RAG-TOOL] Tool calls: {len(tool_calls)}")
        for i, tc in enumerate(tool_calls, 1):
            if 'arguments' in tc:
                print(f"  {i}. {tc['tool']}({tc['arguments']})")
            else:
                print(f"  {i}. {tc['tool']}")

        return {
            "question": question,
            "answer": answer,
            "mode": "ai-rag-tool",
            "sources": sources,
            "tool_calls": len(tool_calls),
            "search_queries": search_queries,
            "total_time": round(total_time, 3)
        }

    except Exception as e:
        print(f"[ERROR] AI processing failed: {str(e)}")
        raise HTTPException(status_code=500, detail=f"AI processing error: {str(e)}")
