"""
Manual ticket handling system (AI disabled mode).
Simple rule-based support with keyword matching.
"""

import time
from .knowledge_base import search_knowledge_base


def process_ticket_manual(ticket_id: str, question: str) -> dict:
    """
    Process a support ticket using simple keyword matching.
    
    Args:
        ticket_id: Unique ticket identifier
        question: The user's question
        
    Returns:
        dict with response details
    """
    start_time = time.time()
    
    # Simple keyword search in knowledge base
    result = search_knowledge_base(question)
    response_time = time.time() - start_time
    
    print(f"[MANUAL] Ticket {ticket_id} - Matched: {result.get('topic', 'none')}")
    
    return {
        "ticket_id": ticket_id,
        "question": question,
        "answer": result["answer"],
        "mode": "manual",
        "matched_topic": result.get("topic", "unknown"),
        "response_time": round(response_time, 2)
    }
