# Lesson 1: The Support Bot - First Line of Defense

## 🎯 Business Problem

TechFlow Solutions' support team receives **200+ daily tickets**, with 60% being repetitive questions about products, pricing, account management, and basic troubleshooting. Support agents spend significant time answering the same questions repeatedly, leading to:

- **Slow response times** (5-8 seconds per ticket with manual lookup)
- **Inconsistent answers** across different agents
- **Agent burnout** from repetitive work
- **High operational costs** (80+ hours/week on repetitive tickets)

## 💡 Solution

Build an AI-powered support bot that:
- Answers common questions instantly using intelligent conversation
- Understands context and intent (not just keywords)
- Provides consistent, accurate information
- Frees human agents to handle complex issues

## 📊 Expected Impact

| Metric | Before (Manual) | After (AI) | Improvement |
|--------|----------------|-----------|-------------|
| Average Response Time | 5.5 seconds | 1.2 seconds | **78% faster** |
| Accuracy Rate | 65% | 92% | **+27 points** |
| Tickets Requiring Escalation | 35% | 8% | **77% reduction** |
| Support Time Saved | - | 15 hours/week | **50% workload reduction** |

## 🏗️ Architecture

This lesson demonstrates the **feature flag architecture** - the cornerstone pattern you'll use throughout all lessons:

```
┌─────────────────────────────────────────┐
│   Support Ticket Request                │
│   "What are your pricing plans?"        │
└──────────────┬──────────────────────────┘
               │
               ▼
┌──────────────────────────────────────────┐
│   Feature Flag Check                     │
│   ENABLE_AI_SUPPORT_BOT = ?              │
└──────────────┬───────────────────────────┘
               │
       ┌───────┴────────┐
       │                │
       ▼                ▼
   false            true
       │                │
       ▼                ▼
┌──────────┐    ┌──────────┐
│  Manual  │    │    AI    │
│   Mode   │    │   Mode   │
└──────────┘    └──────────┘
       │                │
       ▼                ▼
  Rule-based      Context-aware
  Keyword Match   Understanding
  5.5s response   1.2s response
  65% accuracy    92% accuracy
```

### Manual Mode (AI Disabled)

When `ENABLE_AI_SUPPORT_BOT=false`:
- Uses **simple keyword matching** against knowledge base
- Simulates traditional rule-based support
- Slower response times (3-8 seconds)
- Lower accuracy (65%)
- Cannot understand context or complex queries

### AI Mode (AI Enabled)

When `ENABLE_AI_SUPPORT_BOT=true`:
- Uses **intelligent conversation** with context understanding
- Combines information from multiple sources
- Faster response times (0.5-2 seconds)
- Higher accuracy (92%)
- Handles complex, multi-part questions

## 📁 Project Structure

```
lesson-01-support-bot/
├── README.md                    # This file
├── Dockerfile                   # Container configuration
├── requirements.txt             # Python dependencies
└── src/
    ├── main.py                 # FastAPI application with feature flag logic
    ├── knowledge_base.py       # TechFlow product/support information
    ├── manual.py               # Manual processing (AI disabled)
    ├── agent.py                # AI processing (AI enabled)
    └── metrics.py              # Performance tracking and comparison
```

## 🚀 Quick Start

### Prerequisites

- Docker and Docker Compose installed
- `.env` file configured in repository root

### 1. Configure Feature Flag

Edit the root `.env` file:

```bash
# For manual mode (baseline)
ENABLE_AI_SUPPORT_BOT=false

# For AI mode (enhanced)
ENABLE_AI_SUPPORT_BOT=true
```

### 2. Start the Service

From the repository root:

```bash
# Start just the support bot
docker compose -f docker-compose.infrastructure.yml up support-bot --build

# Or start all infrastructure services
docker compose -f docker-compose.infrastructure.yml up --build
```

The support bot API will be available at: **http://localhost:8001**

### 3. Test the Bot

#### Using the API directly:

```bash
# Submit a support ticket
curl -X POST http://localhost:8001/ticket \
  -H "Content-Type: application/json" \
  -d '{"question": "What are your pricing plans?"}'

# Get performance metrics
curl http://localhost:8001/metrics

# Get example questions
curl http://localhost:8001/examples
```

#### Using the Interactive Portal:

1. Open http://localhost:3000/support
2. Toggle the AI feature flag
3. Ask questions and see real-time metrics

### 4. Compare Modes

**Test with AI Disabled:**
1. Set `ENABLE_AI_SUPPORT_BOT=false`
2. Restart the service
3. Submit several tickets
4. Note the response times and accuracy

**Test with AI Enabled:**
1. Set `ENABLE_AI_SUPPORT_BOT=true`
2. Restart the service
3. Submit the same tickets
4. Compare the improvements!

## 📚 What You'll Learn

### 1. Feature Flag Pattern
- How to implement before/after comparison in your code
- Using environment variables to control behavior
- Measuring impact of AI features

### 2. API Design
- Building REST APIs with FastAPI
- Handling requests and responses
- Error handling and validation

### 3. Metrics Collection
- Tracking performance metrics (response time, accuracy)
- Comparing manual vs AI processing
- Calculating ROI and business impact

### 4. Knowledge Base Integration
- Structuring domain knowledge
- Keyword matching vs context understanding
- Providing consistent answers

## 🧪 Testing Scenarios

Try these questions to see the difference:

### Simple Questions (Both modes handle well)
- "What are your pricing plans?"
- "How do I reset my password?"
- "What are your support hours?"

### Complex Questions (AI excels)
- "I need pricing info and want to know if you offer a trial"
- "How does your DevOps tool integrate with our existing Slack and GitHub setup?"
- "We're a team of 15, which plan is best and can we upgrade later?"

### Edge Cases (Shows AI advantage)
- Questions with typos or informal language
- Multi-part questions
- Questions requiring synthesis of multiple topics

## 📈 Expected Results

After processing 10 tickets with each mode:

### Manual Mode Metrics:
```
Average Response Time: 5.5 seconds
Accuracy Rate: 65%
Escalation Rate: 35%
Processing: Simple keyword matching
```

### AI Mode Metrics:
```
Average Response Time: 1.2 seconds
Accuracy Rate: 92%
Escalation Rate: 8%
Processing: Context-aware understanding
```

### Business Impact:
```
Daily Time Saved: 10 hours (based on 200 tickets/day)
Weekly Time Saved: 50 hours
Monthly Cost Savings: $10,000 (at $50/hour)
Workload Reduction: 50%
```

## 🔧 API Endpoints

### `POST /ticket`
Submit a support ticket for processing.

**Request:**
```json
{
  "question": "What are your pricing plans?",
  "user_email": "customer@example.com"
}
```

**Response:**
```json
{
  "ticket_id": "TICKET-A1B2C3D4",
  "question": "What are your pricing plans?",
  "answer": "TechFlow Solutions offers flexible pricing plans...",
  "mode": "ai",
  "metrics": {
    "response_time_seconds": 1.2,
    "accuracy_score": 0.92,
    "context_understanding": true
  }
}
```

### `GET /metrics`
Get performance metrics and comparison.

**Response:**
```json
{
  "summary": {
    "total_tickets": 20,
    "by_mode": {"manual": 10, "ai": 10},
    "improvement": {
      "speed_improvement": {
        "percentage": 78.2,
        "time_saved_per_ticket": 4.3
      },
      "business_impact": {
        "weekly_time_saved_hours": 50,
        "monthly_savings": "$10,000"
      }
    }
  }
}
```

### `GET /stats`
Get statistics about the current mode.

### `GET /examples`
Get example questions for testing.

### `GET /health`
Health check endpoint.

## 🎓 Key Concepts

### 1. Feature Flags for AI Impact Demonstration

The feature flag pattern allows you to:
- **Compare before and after** in the same codebase
- **Demonstrate ROI** with real metrics
- **Roll out gradually** by enabling for specific users
- **Roll back instantly** if issues occur

```python
if os.getenv('ENABLE_AI_SUPPORT_BOT') == 'true':
    # AI-powered logic - fast, accurate, context-aware
    result = process_ticket_ai(ticket_id, question)
else:
    # Manual fallback - slower, simpler, keyword-based
    result = process_ticket_manual(ticket_id, question)
```

### 2. Measuring AI Impact

Always collect metrics for both modes:
- **Response time**: How fast can we answer?
- **Accuracy**: How often is the answer correct?
- **Escalation rate**: How often do we need human help?
- **User satisfaction**: How happy are customers?

### 3. Knowledge Base Design

Structure your knowledge base for both modes:
- **Keywords**: For simple matching (manual mode)
- **Full content**: For context understanding (AI mode)
- **Related topics**: For comprehensive answers
- **Escalation paths**: When to hand off to humans

## 🔜 Next Steps

Once you've completed this lesson:

1. **Experiment** with different questions
2. **Analyze** the metrics to understand AI impact
3. **Modify** the knowledge base with your own content
4. **Proceed** to Lesson 2: The FAQ Expert (adding RAG)

## 💡 Tips for Production

While this lesson uses simulated AI responses, in production you would:

1. **Use Microsoft Agent Framework** with real AI models:
   ```python
   from agent_framework import ChatAgent
   from agent_framework.openai import OpenAIChatClient
   
   agent = ChatAgent(
       chat_client=OpenAIChatClient(model_id="gpt-4o"),
       instructions="You are a helpful support agent...",
       tools=[search_knowledge_base]
   )
   ```

2. **Integrate with your ticketing system** (Jira, ServiceNow, Zendesk)

3. **Add authentication and rate limiting**

4. **Implement proper error handling and fallbacks**

5. **Monitor and log all interactions** for quality assurance

6. **Continuously update** the knowledge base based on new questions

## 🐛 Troubleshooting

### Service won't start
- Check Docker is running: `docker ps`
- Verify `.env` file exists in repository root
- Check port 8001 is not in use: `lsof -i :8001`

### Feature flag not working
- Ensure `.env` value is exactly `true` or `false` (lowercase)
- Restart the Docker container after changing `.env`
- Check environment variables: `docker exec support-bot env | grep ENABLE`

### Slow response times
- This is expected in manual mode (demonstrates the problem!)
- AI mode should be much faster
- Check Docker resource allocation if both modes are slow

## 📞 Support

Questions about this lesson? 
- Check the [main README](../../README.md)
- Review the [Setup Guide](../../docs/setup-guide.md)
- Explore the [Feature Flags documentation](../../docs/feature-flags.md)

---

**Ready to see AI in action?** Toggle that feature flag and watch the magic happen! ✨
