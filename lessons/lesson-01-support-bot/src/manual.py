"""
Manual ticket handling system (AI disabled mode).
Simulates traditional rule-based support with keyword matching.
"""

import time
import random
from .knowledge_base import search_knowledge_base


def process_ticket_manual(ticket_id: str, question: str) -> dict:
    """
    Process a support ticket using manual/rule-based logic.
    Simulates slower response times and basic keyword matching.
    
    Args:
        ticket_id: Unique ticket identifier
        question: The user's question
        
    Returns:
        dict with response details and metrics
    """
    start_time = time.time()
    
    # Simulate manual processing delay (3-8 seconds)
    processing_delay = random.uniform(3.0, 8.0)
    time.sleep(processing_delay)
    
    # Simple keyword search in knowledge base
    result = search_knowledge_base(question)
    
    # Calculate metrics
    response_time = time.time() - start_time
    
    # Manual mode has lower accuracy for edge cases
    accuracy = 0.65 if result["found"] else 0.40
    
    # Add manual processing notes
    response = {
        "ticket_id": ticket_id,
        "question": question,
        "answer": result["answer"],
        "mode": "manual",
        "metrics": {
            "response_time_seconds": round(response_time, 2),
            "accuracy_score": accuracy,
            "matched_topic": result.get("topic", "unknown"),
            "confidence": result.get("confidence", 0),
            "processing_notes": "Processed using rule-based keyword matching"
        },
        "suggestions": [
            "For more accurate answers, consider enabling AI mode",
            "Complex queries may require human agent escalation"
        ]
    }
    
    # Log processing
    print(f"[MANUAL] Ticket {ticket_id} processed in {response_time:.2f}s - Topic: {result.get('topic', 'unknown')}")
    
    return response


def get_manual_stats() -> dict:
    """
    Return statistics about manual processing mode.
    
    Returns:
        dict with performance statistics
    """
    return {
        "mode": "manual",
        "average_response_time": "5.5 seconds",
        "accuracy_rate": "65%",
        "tickets_requiring_escalation": "35%",
        "method": "Rule-based keyword matching",
        "limitations": [
            "Cannot understand context or nuance",
            "Limited to predefined answers",
            "No learning from past interactions",
            "Struggles with complex or multi-part questions",
            "Higher false negative rate"
        ]
    }
