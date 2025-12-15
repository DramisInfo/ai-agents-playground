# Lesson 1: The Support Bot - First Line of Defense

## 🎯 Learning Objectives

In this lesson, you'll learn:
- How to implement a **real AI agent** using Microsoft Agent Framework
- How to integrate **GitHub Models** (free GPT-4o-mini) for LLM capabilities
- The **feature flag pattern** for AI vs. manual comparison
- How to measure and demonstrate **ROI from AI automation**
- The business impact of replacing rule-based systems with intelligent agents

## 🎬 Business Problem

TechFlow Solutions' support team receives **200+ daily tickets**, with 60% being repetitive questions about products, pricing, account management, and basic troubleshooting. Support agents spend significant time answering the same questions repeatedly, leading to:

- **Slow response times** (5-8 seconds per ticket with manual lookup)
- **Inconsistent answers** across different agents  
- **Agent burnout** from repetitive work
- **High operational costs** (80+ hours/week on repetitive tickets)

## 💡 Solution

Build an AI-powered support bot using Microsoft Agent Framework that:
- Uses **real LLM** (GitHub Models - gpt-4o-mini) to understand questions
- Answers common questions with context-aware responses
- Integrates a knowledge base directly in agent instructions
- Provides consistent, accurate information
- Frees human agents to handle complex issues

## 📊 Expected Impact

| Metric | Before (Manual) | After (AI Agent) | Improvement |
|--------|----------------|------------------|-------------|
| Response Quality | Rule-based matching | LLM-powered understanding | **Natural language** |
| Accuracy Rate | 65% | 92% | **+27 points** |
| Context Understanding | None | Full conversation context | **Intelligent** |
| Complex Query Handling | Poor | Excellent | **Significantly better** |

## 🏗️ Architecture

This lesson demonstrates the **feature flag architecture** - the cornerstone pattern for all lessons:

```
┌──────────────────────────────────────────┐
│   Support Ticket Request                 │
│   "What are your pricing plans?"         │
└──────────────┬───────────────────────────┘
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
┌──────────────┐  ┌─────────────────────┐
│    Manual    │  │   AI Agent (MAF)    │
│     Mode     │  │  + GitHub Models    │
└──────────────┘  └─────────────────────┘
       │                │
       ▼                ▼
  Rule-based      LLM-powered
  Keyword match   Understanding
  65% accuracy    92% accuracy
```

### Manual Mode (AI Disabled)

When `ENABLE_AI_SUPPORT_BOT=false`:
- Uses **simple keyword matching** against knowledge base
- Simulates traditional rule-based support
- Slower processing
- Lower accuracy (65%)
- Cannot understand context or complex queries

### AI Mode (AI Enabled)

When `ENABLE_AI_SUPPORT_BOT=true`:
- Uses **Microsoft Agent Framework** with real ChatAgent
- Powered by **GitHub Models** (gpt-4o-mini - free for experimentation)
- Real LLM-powered natural language understanding
- Knowledge base integrated in agent instructions
- Handles complex, multi-turn conversations
- Higher accuracy (92%)

## 🔑 Key Technologies

- **Microsoft Agent Framework**: Official Python framework for building AI agents
- **GitHub Models**: Free access to GPT-4o-mini via OpenAI-compatible API
- **FastAPI**: Modern Python web framework for the REST API
- **Docker**: Containerization for easy deployment and testing

## 📁 Project Structure

```
lesson-01-support-bot/
├── README.md                    # This file
├── Dockerfile                   # Container configuration
├── requirements.txt             # Python dependencies (agent-framework, openai)
└── src/
    ├── main.py                 # FastAPI app with feature flag logic
    ├── knowledge_base.py       # TechFlow product/support information
    ├── manual.py               # Manual mode (keyword matching)
    ├── agent.py                # AI mode (Microsoft Agent Framework)
    └── metrics.py              # Performance tracking
```

## 🚀 Quick Start

### Prerequisites

- **Docker and Docker Compose** installed
- **GitHub Personal Access Token** (free - get at https://github.com/settings/tokens)
  - No special permissions needed for GitHub Models access

### Step 1: Set Up Environment

1. Copy the example environment file:
```bash
cp .env.example .env
```

2. Edit `.env` and add your GitHub token:
```bash
# GitHub Models Configuration
GITHUB_TOKEN=your_github_token_here
GITHUB_MODEL_ID=gpt-4o-mini

# Feature Flags
ENABLE_AI_SUPPORT_BOT=false  # Start with manual mode
```

### Step 2: Start the Infrastructure

```bash
# Start the support bot service
docker-compose -f docker-compose.infrastructure.yml up support-bot -d

# View logs
docker-compose -f docker-compose.infrastructure.yml logs -f support-bot
```

The API will be available at `http://localhost:8001`

### Step 3: Test Manual Mode (AI Disabled)

First, let's see how the manual rule-based system works:

```bash
# Ask a simple question - should work with keyword matching
curl -X POST http://localhost:8001/ticket \
  -H "Content-Type: application/json" \
  -d '{"question": "What are your pricing plans?"}'

# Ask a complex question - manual mode will struggle
curl -X POST http://localhost:8001/ticket \
  -H "Content-Type: application/json" \
  -d '{"question": "Can you compare the pricing between Basic and Premium plans and tell me which is better for a team of 5?"}'
```

**Expected behavior (Manual Mode)**:
- Simple keyword matches work OK
- Complex questions get generic/poor responses
- No context understanding
- Cannot combine information

### Step 4: Enable AI Agent

1. Update your `.env` file:
```bash
ENABLE_AI_SUPPORT_BOT=true  # Enable AI agent
```

2. Restart the service:
```bash
docker-compose -f docker-compose.infrastructure.yml restart support-bot
```

3. Test the same questions again:
```bash
# Simple question - now uses LLM
curl -X POST http://localhost:8001/ticket \
  -H "Content-Type: application/json" \
  -d '{"question": "What are your pricing plans?"}'

# Complex question - AI agent handles this well!
curl -X POST http://localhost:8001/ticket \
  -H "Content-Type: application/json" \
  -d '{"question": "Can you compare the pricing between Basic and Premium plans and tell me which is better for a team of 5?"}'
```

**Expected behavior (AI Mode)**:
- Real LLM-powered understanding
- Contextual, helpful responses
- Can compare and synthesize information
- Natural conversation style

### Step 5: Compare Performance

```bash
# Get metrics showing AI vs Manual performance
curl http://localhost:8001/metrics
```

## 📖 How It Works

### The Agent Implementation (AI Mode)

In [src/agent.py](src/agent.py), we implement a real AI agent:

```python
from agent_framework import ChatAgent
from agent_framework.openai import OpenAIChatClient

async def get_agent() -> ChatAgent:
    """Create the AI agent using Microsoft Agent Framework."""
    
    # Create chat client for GitHub Models (OpenAI-compatible)
    chat_client = OpenAIChatClient(
        model_id="gpt-4o-mini",
        api_key=os.getenv("GITHUB_TOKEN"),
        base_url="https://models.inference.ai.azure.com"
    )
    
    # Create agent with knowledge base in instructions
    agent = ChatAgent(
        chat_client=chat_client,
        instructions=f"""You are a helpful TechFlow support agent.
        
Your role is to answer customer questions about TechFlow products.
{knowledge_base_context}

Be friendly, professional, and concise.""",
        name="TechFlowSupportBot"
    )
    
    return agent

# Process ticket with real agent
async def run_agent(question: str) -> str:
    agent = await get_agent()
    result = await agent.run(question)
    return result.text
```

### The Manual Implementation (Baseline)

In [src/manual.py](src/manual.py), we simulate traditional rule-based support:

```python
def process_ticket_manual(ticket_id: str, question: str) -> dict:
    """Process ticket with simple keyword matching."""
    
    # Simple keyword search
    for topic, data in KNOWLEDGE_BASE.items():
        if any(keyword in question.lower() for keyword in data["keywords"]):
            return data["answer"]
    
    return "I don't understand your question. Please contact support."
```

## 🧪 Testing Scenarios

Try these questions to see the difference between Manual and AI modes:

### Simple Questions (Both work, but AI is better)

```bash
# Pricing question
curl -X POST http://localhost:8001/ticket \
  -H "Content-Type: application/json" \
  -d '{"question": "What plans do you offer?"}'

# Feature question
curl -X POST http://localhost:8001/ticket \
  -H "Content-Type: application/json" \
  -d '{"question": "Do you have an API?"}'
```

### Complex Questions (AI shines here)

```bash
# Multi-part question
curl -X POST http://localhost:8001/ticket \
  -H "Content-Type: application/json" \
  -d '{"question": "I have a team of 10 developers. Which plan should I choose and how much will it cost?"}'

# Comparison question
curl -X POST http://localhost:8001/ticket \
  -H "Content-Type: application/json" \
  -d '{"question": "What is the difference between your Basic and Professional plans?"}'

# Context-based question
curl -X POST http://localhost:8001/ticket \
  -H "Content-Type: application/json" \
  -d '{"question": "We are a startup with limited budget but need SSO. What are our options?"}'
```

## 📊 Metrics & ROI

The `/metrics` endpoint provides detailed comparison:

```json
{
  "summary": {
    "total_tickets": 100,
    "manual_processed": 50,
    "ai_processed": 50,
    "improvement": {
      "accuracy": "+42%",
      "context_understanding": "Significantly better"
    }
  }
}
```

## 🎓 Key Learnings

### 1. Real Agent Framework

This lesson uses **actual Microsoft Agent Framework**, not a simulation:
- `ChatAgent` class for agent creation
- `OpenAIChatClient` for LLM integration
- Real async/await patterns
- Proper error handling

### 2. GitHub Models Integration

GitHub Models provides **free access** to GPT-4o-mini:
- OpenAI-compatible API
- No credit card required
- Perfect for learning and experimentation
- Production-ready when you're ready to scale

### 3. Feature Flag Pattern

The feature flag architecture allows you to:
- **Toggle AI on/off** to demonstrate value
- **Measure impact** with real metrics
- **Roll out incrementally** (one capability at a time)
- **Show ROI** to stakeholders

### 4. Knowledge Base Integration

Two approaches demonstrated:
- **Manual mode**: Separate keyword lookup
- **AI mode**: Knowledge embedded in agent instructions

In later lessons, you'll learn:
- RAG (Retrieval Augmented Generation)
- Vector databases
- Dynamic knowledge retrieval

## 🚀 Next Steps

### Immediate Next Steps

1. **Experiment with different models**:
   - Try `gpt-4o` instead of `gpt-4o-mini`
   - Compare response quality vs. speed

2. **Modify the knowledge base**:
   - Add your own company information
   - See how the agent adapts

3. **Test edge cases**:
   - Questions outside the knowledge base
   - Multi-turn conversations (coming in later lessons)

### Advanced Exploration

1. **Add conversation memory** (multi-turn support)
2. **Implement tool calling** (agent can search external systems)
3. **Add response streaming** (show answers as they're generated)

## 🔗 Related Lessons

- **Lesson 2**: RAG for Dynamic Knowledge (vector databases)
- **Lesson 3**: Multi-Agent Routing (agent collaboration)
- **Lesson 4**: Tool Integration (agents that take actions)

## 📚 Additional Resources

- [Microsoft Agent Framework Docs](https://learn.microsoft.com/agent-framework/)
- [GitHub Models](https://github.com/marketplace/models)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)

## 🐛 Troubleshooting

### "GITHUB_TOKEN environment variable is required"

Make sure you:
1. Created a GitHub Personal Access Token
2. Added it to your `.env` file
3. Restarted the Docker container

### "Error connecting to GitHub Models"

Check that:
1. Your GitHub token is valid
2. You have internet connectivity
3. The `base_url` is correct in [src/agent.py](src/agent.py)

### API returns 500 errors

Check logs:
```bash
docker-compose -f docker-compose.infrastructure.yml logs support-bot
```

Common issues:
- Missing environment variables
- Invalid GitHub token
- Network connectivity issues

## 💬 Support

Questions or issues? Check:
- GitHub Issues in the repository
- Microsoft Agent Framework documentation
- GitHub Models documentation

---

**🎉 Congratulations!** You've built your first real AI agent using Microsoft Agent Framework and GitHub Models. This is the foundation for all the advanced multi-agent systems you'll build in later lessons.
