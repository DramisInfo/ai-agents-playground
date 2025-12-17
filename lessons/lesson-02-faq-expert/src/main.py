"""
Main FastAPI application for FAQ Expert (Lesson 2).
Demonstrates RAG-powered AI vs Manual keyword matching with feature flag control.
"""

import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from dotenv import load_dotenv

from .manual import process_faq_manual
from .agent import process_faq_ai

# Load environment variables
load_dotenv()

app = FastAPI(
    title="TechFlow FAQ Expert - Lesson 2",
    description="Compare RAG-powered AI vs manual keyword-based FAQ answering",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class FAQRequest(BaseModel):
    """Request model for FAQ question."""
    question: str


class Source(BaseModel):
    """Source document reference."""
    title: str
    filename: str
    similarity: float


class FAQResponse(BaseModel):
    """Response model for FAQ answer."""
    question: str
    answer: str
    mode: str
    sources: Optional[List[Source]] = None
    matched_faq: Optional[str] = None
    match_count: Optional[int] = None
    confidence: Optional[str] = None
    search_time: Optional[float] = None
    generation_time: Optional[float] = None
    response_time: Optional[float] = None
    total_time: Optional[float] = None


@app.get("/")
def root():
    """Root endpoint with API information."""
    ai_enabled = os.getenv("ENABLE_AI_FAQ_RAG", "false").lower() == "true"
    
    return {
        "service": "TechFlow FAQ Expert",
        "lesson": "02 - RAG-Powered Knowledge Search",
        "ai_enabled": ai_enabled,
        "mode": "AI-RAG" if ai_enabled else "Manual Keyword Search",
        "feature_flag": "ENABLE_AI_FAQ_RAG",
        "description": "Compare semantic search with vector embeddings vs simple keyword matching"
    }


@app.get("/health")
def health_check():
    """Health check endpoint."""
    ai_enabled = os.getenv("ENABLE_AI_FAQ_RAG", "false").lower() == "true"
    
    return {
        "status": "healthy",
        "service": "faq-expert",
        "lesson": "02",
        "ai_enabled": ai_enabled,
        "mode": "ai-rag" if ai_enabled else "manual"
    }


@app.post("/ask", response_model=FAQResponse)
def ask_question(request: FAQRequest):
    """
    Answer an FAQ question.
    
    Mode is controlled by ENABLE_AI_FAQ_RAG environment variable:
    - true: Use RAG with vector search and LLM generation
    - false: Use simple keyword matching
    
    Args:
        request: FAQ question request
        
    Returns:
        FAQ answer with metadata
    """
    if not request.question or not request.question.strip():
        raise HTTPException(status_code=400, detail="Question cannot be empty")
    
    # Check feature flag
    ai_enabled = os.getenv("ENABLE_AI_FAQ_RAG", "false").lower() == "true"
    
    try:
        if ai_enabled:
            # Use AI-powered RAG system
            result = process_faq_ai(request.question)
        else:
            # Use manual keyword matching
            result = process_faq_manual(request.question)
        
        return FAQResponse(**result)
    
    except Exception as e:
        print(f"[ERROR] Failed to process question: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/stats")
def get_stats():
    """
    Get system statistics and comparison metrics.
    
    Returns:
        Statistics about the FAQ system performance
    """
    ai_enabled = os.getenv("ENABLE_AI_FAQ_RAG", "false").lower() == "true"
    
    if ai_enabled:
        return {
            "mode": "ai-rag",
            "description": "RAG-powered semantic search with vector embeddings",
            "features": [
                "Vector similarity search with pgvector",
                "Semantic understanding of questions",
                "Context-aware answer generation",
                "Source citations with confidence scores",
                "Handles complex and varied phrasing"
            ],
            "typical_metrics": {
                "accuracy": "90%+",
                "response_time": "1-3 seconds",
                "coverage": "Entire knowledge base",
                "can_handle": "Natural language questions, synonyms, complex queries"
            }
        }
    else:
        return {
            "mode": "manual",
            "description": "Simple keyword-based FAQ matching",
            "features": [
                "Keyword matching in predefined FAQs",
                "Fast but limited understanding",
                "Fixed responses",
                "No context awareness"
            ],
            "typical_metrics": {
                "accuracy": "40-50%",
                "response_time": "0.1-0.2 seconds",
                "coverage": f"{len(process_faq_manual.__globals__['FAQ_DATABASE'])} predefined FAQs",
                "can_handle": "Only exact keyword matches"
            }
        }


if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", "8002"))
    uvicorn.run(app, host="0.0.0.0", port=port)
