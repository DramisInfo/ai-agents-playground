"""
Knowledge base for TechFlow Solutions support bot.
Contains common questions and answers about products and services.
"""

KNOWLEDGE_BASE = {
    "pricing": {
        "keywords": ["price", "cost", "pricing", "how much", "plan"],
        "answer": "TechFlow offers three plans: Starter ($299/mo), Professional ($799/mo), and Enterprise (custom pricing). All plans include 24/7 support."
    },
    
    "support": {
        "keywords": ["support", "help", "contact", "hours"],
        "answer": "We offer 24/7 support via email (support@techflow.com), live chat, and phone (+1-800-TECHFLOW). Documentation is at docs.techflow.com"
    },
    
    "password": {
        "keywords": ["password", "reset", "forgot", "login"],
        "answer": "To reset your password, visit techflow.com/login and click 'Forgot Password'. You'll receive a reset link via email within 5 minutes."
    },
}


def search_knowledge_base(query: str) -> dict:
    """
    Search the knowledge base for relevant answers.
    Returns the best matching answer based on keyword matching.
    
    Args:
        query: The user's question
        
    Returns:
        dict with 'found' (bool), 'answer' (str), and 'topic' (str)
    """
    query_lower = query.lower()
    
    # Score each topic based on keyword matches
    scores = {}
    for topic, data in KNOWLEDGE_BASE.items():
        score = sum(1 for keyword in data["keywords"] if keyword in query_lower)
        if score > 0:
            scores[topic] = score
    
    # Return the best match
    if scores:
        best_topic = max(scores, key=scores.get)
        return {
            "found": True,
            "answer": KNOWLEDGE_BASE[best_topic]["answer"],
            "topic": best_topic,
            "confidence": scores[best_topic]
        }
    
    return {
        "found": False,
        "answer": "I couldn't find a specific answer to your question in my knowledge base. Please contact our support team at support@techflow.com or call +1-800-TECHFLOW for assistance.",
        "topic": "unknown",
        "confidence": 0
    }
