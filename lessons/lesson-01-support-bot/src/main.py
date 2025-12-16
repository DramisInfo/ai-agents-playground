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

from .manual import process_ticket_manual
from .agent import process_ticket_ai

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
    response_time: float


@app.get("/")
def root():
    """Root endpoint with API information."""
    ai_enabled = os.getenv("ENABLE_AI_SUPPORT_BOT", "false").lower() == "true"
    
    return {
        "service": "TechFlow Support Bot",
        "lesson": "01 - Introduction to AI Agents",
        "ai_enabled": ai_enabled,
        "mode": "AI-Powered" if ai_enabled else "Manual",
        "feature_flag": "ENABLE_AI_SUPPORT_BOT"
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
            return process_ticket_ai(ticket_id, request.question)
        else:
            # Manual rule-based processing
            return process_ticket_manual(ticket_id, request.question)
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing ticket: {str(e)}")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
