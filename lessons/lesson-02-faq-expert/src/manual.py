"""
Manual FAQ handling system (AI disabled mode).
Simple keyword-based search with pre-defined responses.
"""

import time
from typing import Dict, List


# Simple FAQ database with keyword matching
FAQ_DATABASE = {
    "pricing": {
        "keywords": ["price", "cost", "pricing", "payment", "subscription", "plan", "billing", "fee"],
        "answer": "FlowCRM offers flexible pricing plans: Starter ($29/month for 5 users), Professional ($79/month for 20 users), and Enterprise (custom pricing). Visit our pricing page for details.",
        "confidence": "low"
    },
    "import_contacts": {
        "keywords": ["import", "upload", "csv", "contacts", "bulk", "add contacts"],
        "answer": "To import contacts: Go to Contacts > Import > Upload your CSV file. Make sure your CSV has columns for name, email, phone. You can download a template from the import page.",
        "confidence": "medium"
    },
    "email_integration": {
        "keywords": ["email", "gmail", "outlook", "integration", "connect", "sync"],
        "answer": "FlowCRM integrates with Gmail and Outlook. Go to Settings > Integrations > Email and follow the setup wizard. You'll need to authorize access to your email account.",
        "confidence": "medium"
    },
    "duplicate_contacts": {
        "keywords": ["duplicate", "duplicates", "merge", "same contact"],
        "answer": "To handle duplicates: Go to Contacts > Duplicate Management. The system will automatically detect potential duplicates. You can merge or keep them separate as needed.",
        "confidence": "medium"
    },
    "password_reset": {
        "keywords": ["password", "reset", "forgot", "login", "access", "locked"],
        "answer": "To reset your password: Click 'Forgot Password' on the login page, enter your email, and follow the reset link sent to you. Links expire in 24 hours.",
        "confidence": "high"
    },
    "user_roles": {
        "keywords": ["user", "role", "permission", "access", "admin", "rights"],
        "answer": "FlowCRM has three user roles: Admin (full access), Manager (read/write, no billing), and User (read-only). Admins can manage roles in Settings > Team Management.",
        "confidence": "medium"
    },
    "custom_fields": {
        "keywords": ["custom field", "tag", "label", "category", "customize"],
        "answer": "To add custom fields: Go to Settings > Custom Fields > Add Field. Choose field type (text, number, date, etc.) and specify where it appears (contacts, deals, tasks).",
        "confidence": "medium"
    },
    "dashboard": {
        "keywords": ["dashboard", "report", "analytics", "metrics", "stats"],
        "answer": "Access your dashboard from the home page. It shows key metrics: open tickets, response times, and customer satisfaction. You can customize widgets in Settings > Dashboard.",
        "confidence": "low"
    },
    "flowanalytics": {
        "keywords": ["flowanalytics", "analytics", "data source", "visualization", "chart"],
        "answer": "FlowAnalytics is our business intelligence tool. Connect data sources in Settings > Data Connections, then create dashboards with custom visualizations and reports.",
        "confidence": "low"
    }
}


def search_faq_database(question: str) -> Dict:
    """
    Search FAQ database using simple keyword matching.
    
    Args:
        question: User's question
        
    Returns:
        Best matching FAQ entry or default response
    """
    question_lower = question.lower()
    
    # Count keyword matches for each FAQ
    matches = []
    for faq_id, faq_data in FAQ_DATABASE.items():
        match_count = sum(1 for keyword in faq_data["keywords"] if keyword in question_lower)
        if match_count > 0:
            matches.append({
                "id": faq_id,
                "match_count": match_count,
                "answer": faq_data["answer"],
                "confidence": faq_data["confidence"]
            })
    
    # Sort by match count
    matches.sort(key=lambda x: x["match_count"], reverse=True)
    
    if matches:
        return {
            "answer": matches[0]["answer"],
            "matched_faq": matches[0]["id"],
            "match_count": matches[0]["match_count"],
            "confidence": matches[0]["confidence"]
        }
    
    # No match found
    return {
        "answer": "I'm sorry, I couldn't find an answer to your question in our FAQ database. Please contact our support team for assistance, or try rephrasing your question with keywords like 'pricing', 'import', 'email', or 'password'.",
        "matched_faq": "none",
        "match_count": 0,
        "confidence": "none"
    }


def process_faq_manual(question: str) -> dict:
    """
    Process an FAQ question using simple keyword matching.
    
    Args:
        question: The user's question
        
    Returns:
        dict with response details
    """
    start_time = time.time()
    
    # Simple keyword search
    result = search_faq_database(question)
    
    # Simulate slower processing (manual systems are typically slower)
    time.sleep(0.1)  # 100ms delay to simulate manual lookup time
    
    response_time = time.time() - start_time
    
    print(f"[MANUAL] Question processed - Matched: {result['matched_faq']} ({result['match_count']} keywords)")
    
    return {
        "question": question,
        "answer": result["answer"],
        "mode": "manual",
        "matched_faq": result["matched_faq"],
        "match_count": result["match_count"],
        "confidence": result["confidence"],
        "response_time": round(response_time, 3)
    }
