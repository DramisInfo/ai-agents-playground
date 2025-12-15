"""
Knowledge base for TechFlow Solutions support bot.
Contains common questions and answers about products, policies, and procedures.
"""

KNOWLEDGE_BASE = {
    # Product Questions
    "product features": {
        "keywords": ["features", "capabilities", "what does", "can it", "does it support"],
        "answer": """TechFlow Solutions offers three main product lines:
        
1. **CloudSync Enterprise** - Cloud migration and synchronization platform
   - Real-time data synchronization across multiple clouds
   - Automated backup and disaster recovery
   - Enterprise-grade security and compliance
   
2. **DevOps Accelerator** - CI/CD pipeline automation tool
   - Automated testing and deployment
   - Integration with GitHub, GitLab, Azure DevOps
   - Container orchestration support
   
3. **DataInsight Pro** - Business intelligence and analytics platform
   - Real-time dashboards and reporting
   - ML-powered predictive analytics
   - Custom data visualization tools
   
For detailed specifications, please visit our documentation portal."""
    },
    
    "pricing": {
        "keywords": ["price", "cost", "pricing", "how much", "subscription", "plan"],
        "answer": """TechFlow Solutions offers flexible pricing plans:

**CloudSync Enterprise**
- Starter: $299/month (up to 100GB, 5 users)
- Professional: $799/month (up to 1TB, 25 users)
- Enterprise: Custom pricing (unlimited data and users)

**DevOps Accelerator**
- Team: $499/month (up to 10 users, 1000 builds/month)
- Business: $1,299/month (up to 50 users, 5000 builds/month)
- Enterprise: Custom pricing (unlimited)

**DataInsight Pro**
- Basic: $399/month (5 dashboards, 10 users)
- Advanced: $999/month (unlimited dashboards, 50 users)
- Enterprise: Custom pricing

All plans include 24/7 support and free updates. Annual billing receives 20% discount."""
    },
    
    "trial": {
        "keywords": ["trial", "demo", "test", "try", "evaluate", "free"],
        "answer": """Yes! We offer a 30-day free trial for all products with no credit card required.

To start your trial:
1. Visit https://techflow.com/trial
2. Create an account with your work email
3. Select the products you want to try
4. Receive instant access to full features

During the trial:
- Access to all premium features
- 24/7 email and chat support
- Sample datasets and templates included
- Optional 1-hour onboarding session with our team

Your trial can be extended by 15 days if you schedule a demo with our sales team."""
    },
    
    # Support & Account Questions
    "reset password": {
        "keywords": ["password", "reset", "forgot", "login", "can't access", "locked out"],
        "answer": """To reset your password:

1. Go to https://techflow.com/login
2. Click "Forgot Password?"
3. Enter your registered email address
4. Check your email for the reset link (arrives within 5 minutes)
5. Click the link and create a new password

Password requirements:
- Minimum 12 characters
- Must include uppercase, lowercase, number, and special character
- Cannot reuse last 5 passwords

Still having issues? Contact support@techflow.com with your account email."""
    },
    
    "support hours": {
        "keywords": ["support", "help", "contact", "hours", "available", "reach"],
        "answer": """TechFlow Solutions provides comprehensive support:

**24/7 Support Channels:**
- Live Chat: Available in the dashboard (instant response)
- Email: support@techflow.com (response within 2 hours)
- Phone: +1-800-TECHFLOW (24/7 emergency line)

**Business Hours Support (9 AM - 6 PM EST, Mon-Fri):**
- Video calls: Schedule at techflow.com/schedule
- Slack Connect: For Enterprise customers
- Dedicated account manager: For Enterprise customers

**Self-Service:**
- Documentation: docs.techflow.com
- Community Forum: community.techflow.com
- Video Tutorials: youtube.com/techflowsolutions
- Status Page: status.techflow.com"""
    },
    
    "upgrade plan": {
        "keywords": ["upgrade", "change plan", "more users", "increase", "downgrade"],
        "answer": """To upgrade or change your plan:

**Self-Service (for Team/Professional plans):**
1. Log into your dashboard at https://techflow.com/dashboard
2. Go to Settings > Billing > Change Plan
3. Select your new plan
4. Confirm the change

Changes take effect immediately. You'll be charged prorated amounts for upgrades, and receive credits for downgrades.

**Enterprise Plans:**
Contact your account manager or email sales@techflow.com for custom pricing and features.

**Common Upgrade Paths:**
- More users: Available instantly through dashboard
- More storage: Automatic scaling with usage-based pricing
- Additional features: Some require plan upgrade
- Custom integrations: Available in Enterprise plans"""
    },
    
    # Technical Issues
    "integration": {
        "keywords": ["integrate", "api", "connection", "connect", "webhook"],
        "answer": """TechFlow Solutions integrates with 200+ popular tools:

**Quick Integration Setup:**
1. Dashboard > Integrations > Browse Available
2. Search for your tool (Slack, Teams, Jira, Salesforce, etc.)
3. Click "Connect" and authorize access
4. Configure sync settings and notifications

**Custom API Integration:**
- REST API documentation: api.techflow.com
- API Keys: Dashboard > Settings > API Keys
- Rate Limits: 10,000 requests/hour (Professional), unlimited (Enterprise)
- Webhooks: Configure in Dashboard > Integrations > Webhooks

**Popular Integrations:**
- Communication: Slack, Microsoft Teams, Discord
- Project Management: Jira, Asana, Monday.com
- Version Control: GitHub, GitLab, Bitbucket
- CRM: Salesforce, HubSpot, Pipedrive
- Cloud: AWS, Azure, GCP

Need help? Check our integration guides at docs.techflow.com/integrations"""
    },
    
    "performance": {
        "keywords": ["slow", "performance", "lag", "loading", "timeout", "speed"],
        "answer": """If you're experiencing performance issues, try these steps:

**Immediate Fixes:**
1. Check status page: status.techflow.com
2. Clear browser cache and cookies
3. Try a different browser (Chrome, Firefox, Edge recommended)
4. Disable browser extensions temporarily
5. Check your internet connection speed

**Common Causes:**
- Large dataset loading: Use filters to reduce data volume
- Multiple dashboards open: Close unused tabs
- Browser extensions: May interfere with application
- Network issues: Check with your IT department

**Optimization Tips:**
- Use scheduled reports instead of live dashboards for large datasets
- Enable data caching in Settings > Performance
- Upgrade to Professional plan for priority processing
- Use our mobile app for better performance on tablets

Still experiencing issues? Contact support with:
- Your account email
- Browser and OS version
- Screenshot or screen recording
- Time when issue occurred"""
    },
    
    # Billing Questions
    "refund": {
        "keywords": ["refund", "cancel", "money back", "charge", "billing"],
        "answer": """TechFlow Solutions refund and cancellation policy:

**30-Day Money-Back Guarantee:**
- Full refund if you cancel within first 30 days
- No questions asked
- Refund processed within 5-7 business days

**Cancellation Process:**
1. Log into Dashboard > Settings > Billing
2. Click "Cancel Subscription"
3. Select reason (optional feedback)
4. Confirm cancellation

**After Cancellation:**
- Access continues until end of billing period
- Data available for download for 90 days
- Can reactivate anytime with same credentials

**Disputing Charges:**
If you see an unexpected charge:
1. Check billing@techflow.com for invoice details
2. Contact billing@techflow.com with transaction ID
3. Disputes resolved within 2 business days

**Pausing Service:**
Enterprise customers can pause service for up to 3 months while retaining all data."""
    },
    
    # General Company Info
    "company": {
        "keywords": ["about", "who", "company", "founded", "team", "contact"],
        "answer": """About TechFlow Solutions:

**Company Overview:**
TechFlow Solutions is a mid-sized software consulting company established in 2015, specializing in enterprise software solutions for cloud migration, DevOps automation, and business intelligence.

**Our Team:**
- 150+ employees across North America and Europe
- 50+ software engineers and solution architects
- 24/7 global support team
- 98% customer satisfaction rating

**Headquarters:**
TechFlow Solutions Inc.
1234 Innovation Drive
San Francisco, CA 94105
United States

**Contact:**
- General: info@techflow.com
- Sales: sales@techflow.com
- Support: support@techflow.com
- Phone: +1-800-TECHFLOW
- Careers: careers@techflow.com

**Certifications:**
- SOC 2 Type II Certified
- ISO 27001 Compliant
- GDPR Compliant
- HIPAA Compliant (Enterprise plans)

Learn more at www.techflow.com/about"""
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
