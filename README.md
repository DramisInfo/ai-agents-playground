# AI Agents Playground

A comprehensive, hands-on training program for learning to build AI-powered applications using the **Microsoft Agent Framework (MAF)** with Python.

## ⚡ Quick Start

**Ready to start immediately?** See the [Quick Start Guide](QUICK_START.md) to set up and begin learning in 5 minutes!

## 🎯 Training Objectives

By completing this training, you will:
- Understand foundational concepts of AI agents and agentic systems
- Build simple to complex agents using Microsoft Agent Framework
- Implement multi-agent systems with coordinated workflows
- Apply best practices for production-ready AI agent applications
- Master tools, memory management, and agent orchestration

## 📚 Learning Plan

### **Module 1: Foundations of AI Agents**
Build your understanding of AI agents and create your first working agent.

#### Lesson 1.1: Introduction to AI Agents & Your First Agent ✅ **Available Now**
- **Concepts**: What are AI agents? Agents vs. simple LLM calls
- **Practice**: Set up environment, create a basic ChatAgent
- **Exercise**: Build a custom agent with specific personality/instructions
- **Validation**: Automated tests verify agent creation and response patterns
- **📓 [Start Lesson 1.1](training-materials/module-1-foundations/lesson-1.1-first-agent.ipynb)**

#### Lesson 1.2: Agent Instructions and Prompting
- **Concepts**: Crafting effective instructions, system vs. user messages
- **Practice**: Experiment with different instruction patterns
- **Exercise**: Create agents for different domains (customer service, technical support, etc.)
- **Validation**: Tests verify instruction adherence and response quality

#### Lesson 1.3: Conversation Context and Memory
- **Concepts**: Stateful vs. stateless agents, conversation threads
- **Practice**: Implement multi-turn conversations with context retention
- **Exercise**: Build a conversational agent that remembers user preferences
- **Validation**: Tests verify context persistence across multiple interactions

---

### **Module 2: Adding Capabilities with Tools**
Extend your agents with function calling and external tool integration.

#### Lesson 2.1: Introduction to Function Calling
- **Concepts**: What are tools/functions? When to use function calling
- **Practice**: Create simple functions (calculator, weather lookup)
- **Exercise**: Build an agent with custom business logic functions
- **Validation**: Tests verify correct function registration and execution

#### Lesson 2.2: Advanced Tool Patterns
- **Concepts**: Async tools, error handling, tool selection strategies
- **Practice**: Implement real-world tools (API calls, database queries)
- **Exercise**: Create a research agent with web search and data processing
- **Validation**: Tests verify tool chaining and error recovery

#### Lesson 2.3: Tool Orchestration
- **Concepts**: Sequential vs. parallel tool execution, dependencies
- **Practice**: Build workflows with multiple coordinated tools
- **Exercise**: Create a data analysis agent with visualization capabilities
- **Validation**: Tests verify correct execution order and result aggregation

---

### **Module 3: Agent Communication Patterns**
Learn how agents interact with users and external systems.

#### Lesson 3.1: Streaming Responses
- **Concepts**: Real-time vs. batch responses, SSE (Server-Sent Events)
- **Practice**: Implement streaming with AG-UI protocol
- **Exercise**: Build a chatbot with live typing indicators
- **Validation**: Tests verify streaming functionality and event handling

#### Lesson 3.2: Multi-Modal Agents
- **Concepts**: Handling text, images, files, and structured data
- **Practice**: Process different input types and generate varied outputs
- **Exercise**: Create an agent that analyzes images and documents
- **Validation**: Tests verify multi-modal input/output handling

#### Lesson 3.3: Agent Hosting and Deployment
- **Concepts**: FastAPI integration, hosting patterns, scalability
- **Practice**: Deploy agent as HTTP service with AG-UI
- **Exercise**: Build production-ready agent service with health checks
- **Validation**: Tests verify service availability and response standards

---

### **Module 4: Retrieval-Augmented Generation (RAG)**
Learn to enhance agents with external knowledge through document retrieval.

#### Lesson 4.1: Introduction to RAG - Concepts and Use Cases
- **Concepts**: What is RAG? When to use RAG vs. fine-tuning vs. prompting
- **Practice**: Understand document chunking, embeddings, and semantic search
- **Exercise**: Build a simple document Q&A system
- **Validation**: Tests verify document loading and basic retrieval

#### Lesson 4.2: Building a Document Indexing System
- **Concepts**: Text splitting strategies, embedding models, vector stores
- **Practice**: Index documents with Azure AI Search or local vector DB
- **Exercise**: Create a document processing pipeline with metadata
- **Validation**: Tests verify indexing quality and search accuracy

#### Lesson 4.3: Implementing Semantic Search and Retrieval
- **Concepts**: Vector similarity, hybrid search, re-ranking strategies
- **Practice**: Build advanced retrieval with filtering and scoring
- **Exercise**: Implement multi-query retrieval with context fusion
- **Validation**: Tests verify retrieval relevance and ranking quality

#### Lesson 4.4: RAG Agent with Real-Time Knowledge
- **Concepts**: Integrating retrieval into agent workflows, citation handling
- **Practice**: Build an agent that retrieves and reasons over documents
- **Exercise**: Create a research assistant with source attribution
- **Validation**: Tests verify accurate retrieval-augmented responses

---

### **Module 5: Multi-Agent Systems**
Master coordinating multiple agents for complex workflows.

#### Lesson 5.1: Introduction to Multi-Agent Architectures
- **Concepts**: When to use multiple agents, coordination patterns
- **Practice**: Create two agents with distinct roles
- **Exercise**: Build a simple multi-agent system (researcher + writer)
- **Validation**: Tests verify agent coordination and role separation

#### Lesson 5.2: Agent Handoffs and Delegation
- **Concepts**: Delegation patterns, handoff protocols, context transfer
- **Practice**: Implement agent-to-agent communication
- **Exercise**: Create a customer service system with specialist agents
- **Validation**: Tests verify seamless handoffs and context preservation

#### Lesson 5.3: Orchestration Strategies
- **Concepts**: Sequential, parallel, hierarchical orchestration
- **Practice**: Build complex workflows with multiple coordination patterns
- **Exercise**: Create an autonomous research and reporting system
- **Validation**: Tests verify orchestration logic and workflow completion

---

### **Module 6: Advanced Topics**
Explore production-ready patterns and advanced agent capabilities.

#### Lesson 6.1: Agent Memory and State Management
- **Concepts**: Short-term vs. long-term memory, state persistence
- **Practice**: Implement vector stores and semantic memory
- **Exercise**: Build an agent with persistent learning capabilities
- **Validation**: Tests verify memory retrieval and state consistency

#### Lesson 6.2: Error Handling and Resilience
- **Concepts**: Retry strategies, fallback mechanisms, graceful degradation
- **Practice**: Implement robust error handling patterns
- **Exercise**: Create a resilient agent system with automatic recovery
- **Validation**: Tests verify error scenarios and recovery mechanisms

#### Lesson 6.3: Observability and Monitoring
- **Concepts**: Logging, tracing, metrics, debugging agent behavior
- **Practice**: Integrate Agent 365 observability SDK
- **Exercise**: Add comprehensive monitoring to multi-agent system
- **Validation**: Tests verify telemetry data collection and analysis

#### Lesson 6.4: Security and Authentication
- **Concepts**: API authentication, rate limiting, input validation
- **Practice**: Implement secure agent endpoints
- **Exercise**: Build a secure multi-tenant agent system
- **Validation**: Tests verify security controls and access policies

---

### **Module 7: Capstone Project**
Apply everything you've learned to build a production-ready multi-agent application.

#### Lesson 7.1: Project Planning and Design
- Design a complex multi-agent system from scratch
- Define agent roles, tools, and orchestration patterns
- Create architecture diagrams and implementation plan

#### Lesson 7.2: Implementation
- Build the complete multi-agent system
- Implement all agents, tools, and coordination logic
- Add observability, error handling, and security

#### Lesson 7.3: Testing and Refinement
- Write comprehensive tests for all components
- Validate system behavior under various scenarios
- Optimize performance and reliability

#### Lesson 7.4: Deployment and Documentation
- Deploy the system to a production environment
- Create user documentation and operational guides
- Present the final project and lessons learned

---

## 🛠️ Project Structure

```
ai-agents-playground/
├── training-materials/          # Lesson content and notebooks
│   ├── module-1-foundations/
│   ├── module-2-tools/
│   ├── module-3-communication/
│   ├── module-4-rag/
│   ├── module-5-multi-agent/
│   ├── module-6-advanced/
│   └── module-7-capstone/
├── exercises/                   # Hands-on exercises
│   ├── exercise-1.1/
│   ├── exercise-1.2/
│   └── ...
├── solutions/                   # Reference solutions
├── shared/                      # Reusable code across lessons
│   ├── utils/
│   └── common_agents/
├── tests/                       # Automated validation tests
└── .github/
    └── workflows/               # CI/CD for automated feedback
```

## 🚀 Getting Started

1. **Prerequisites**
   - Python 3.10 or later
   - Azure OpenAI access or compatible LLM endpoint
   - Git and basic terminal knowledge

2. **Environment Setup**
   ```bash
   # Clone the repository
   git clone <repository-url>
   cd ai-agents-playground
   
   # Create virtual environment
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   
   # Install dependencies
   pip install -r requirements.txt
   ```

3. **Start Learning**
   - Begin with Module 1, Lesson 1
   - Each lesson includes theory, practice, and exercises
   - Complete exercises to unlock the next lesson
   - GitHub Actions provides automated feedback

## 📖 How to Use This Training

1. **Read the lesson materials** in `training-materials/`
2. **Work through interactive notebooks** with guided examples
3. **Complete the exercise** in `exercises/`
4. **Run tests locally** to verify your solution
5. **Create a pull request** to get automated feedback
6. **Review feedback** and iterate until tests pass
7. **Move to the next lesson** once validated

## 🤝 Getting Help

- Each lesson includes troubleshooting guides
- Check the FAQ in lesson documentation
- Review reference solutions after completing exercises
- Use GitHub Discussions for questions

## 📊 Progress Tracking

Your progress is automatically tracked through completed exercises:
- ✅ Completed exercises show in your PR history
- 🎯 Badges awarded for module completion
- 📈 Track your learning journey through the dashboard

---

**Ready to build intelligent AI agents? Start with [Module 1, Lesson 1](training-materials/module-1-foundations/lesson-1.1-first-agent/README.md)!**