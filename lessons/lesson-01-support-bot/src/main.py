"""
Main FastAPI application for Support Bot (Lesson 1).
Demonstrates AI vs Manual ticket processing with feature flag control.
"""

import os
import uuid
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv

from .manual import process_ticket_manual, get_manual_stats
from .agent import process_ticket_ai, get_ai_stats
from .metrics import record_ticket_metrics, get_metrics_summary, get_metrics_report

# Load environment variables
load_dotenv()

app = FastAPI(
    title="TechFlow Support Bot - Lesson 1",
    description="Compare AI-powered vs manual support ticket handling",
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


class TicketRequest(BaseModel):
    """Request model for creating a support ticket."""
    question: str
    user_email: str = "user@example.com"


class TicketResponse(BaseModel):
    """Response model for processed ticket."""
    ticket_id: str
    question: str
    answer: str
    mode: str
    metrics: dict


@app.get("/")
def root():
    """Root endpoint with API information."""
    ai_enabled = os.getenv("ENABLE_AI_SUPPORT_BOT", "false").lower() == "true"
    
    return {
        "service": "TechFlow Support Bot",
        "lesson": "01 - First Line of Defense",
        "version": "1.0.0",
        "ai_enabled": ai_enabled,
        "mode": "AI-Powered" if ai_enabled else "Manual",
        "endpoints": {
            "POST /ticket": "Submit a support ticket",
            "GET /metrics": "Get performance metrics",
            "GET /stats": "Get current mode statistics",
            "GET /health": "Health check"
        },
        "feature_flag": "ENABLE_AI_SUPPORT_BOT",
        "documentation": "/docs"
    }


@app.get("/health")
def health_check():
    """Health check endpoint."""
    ai_enabled = os.getenv("ENABLE_AI_SUPPORT_BOT", "false").lower() == "true"
    
    return {
        "status": "healthy",
        "service": "support-bot",
        "lesson": "01",
        "ai_enabled": ai_enabled,
        "mode": "ai" if ai_enabled else "manual"
    }


@app.post("/ticket", response_model=TicketResponse)
def create_ticket(request: TicketRequest):
    """
    Process a support ticket.
    
    Behavior depends on ENABLE_AI_SUPPORT_BOT feature flag:
    - false (disabled): Uses manual rule-based processing
    - true (enabled): Uses AI-powered agent
    """
    # Generate ticket ID
    ticket_id = f"TICKET-{uuid.uuid4().hex[:8].upper()}"
    
    # Check feature flag
    ai_enabled = os.getenv("ENABLE_AI_SUPPORT_BOT", "false").lower() == "true"
    
    try:
        if ai_enabled:
            # AI-powered processing
            result = process_ticket_ai(ticket_id, request.question)
        else:
            # Manual rule-based processing
            result = process_ticket_manual(ticket_id, request.question)
        
        # Record metrics
        record_ticket_metrics(result)
        
        return result
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing ticket: {str(e)}")


@app.get("/metrics")
def get_metrics():
    """
    Get performance metrics and comparison between modes.
    
    Returns summary statistics, response times, accuracy, and ROI calculations.
    """
    try:
        summary = get_metrics_summary()
        report = get_metrics_report()
        
        return {
            "summary": summary,
            "report": report
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving metrics: {str(e)}")


@app.get("/stats")
def get_stats():
    """
    Get statistics about the current processing mode.
    
    Returns capabilities and performance characteristics of active mode.
    """
    ai_enabled = os.getenv("ENABLE_AI_SUPPORT_BOT", "false").lower() == "true"
    
    if ai_enabled:
        stats = get_ai_stats()
    else:
        stats = get_manual_stats()
    
    stats["feature_flag_value"] = os.getenv("ENABLE_AI_SUPPORT_BOT", "false")
    
    return stats


@app.get("/examples")
def get_example_questions():
    """
    Get example questions to test the support bot.
    
    Returns a list of common support questions for testing.
    """
    return {
        "examples": [
            "What are the features of CloudSync Enterprise?",
            "How much does the DevOps Accelerator cost?",
            "Can I get a free trial?",
            "I forgot my password, how do I reset it?",
            "What are your support hours?",
            "How do I upgrade my plan?",
            "How do I integrate with Slack?",
            "The system is running slow, what should I do?",
            "What is your refund policy?",
            "Tell me about your company"
        ],
        "usage": "POST /ticket with { \"question\": \"<your question>\" }"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
