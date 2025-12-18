# Lesson 2: FAQ Expert - Tool-Based RAG

## 🎯 Learning Objectives

Learn how to build an intelligent FAQ system using **Tool-Based Retrieval-Augmented Generation (RAG)** where the AI agent autonomously decides when and how to search the knowledge base. This lesson demonstrates the power of giving agents **tools** instead of pre-loading context, enabling more efficient and intelligent information retrieval.

## 📊 Business Impact

**Problem**: TechFlow's support team needs to answer 300+ unique questions daily from a 500-page knowledge base. Manual keyword search only works for exact matches, resulting in:
- ❌ 40-50% accuracy (misses synonyms and natural language variations)
- ❌ Limited coverage (only ~10 predefined FAQs)
- ❌ Requires constant manual updates to FAQ database

**Solution**: Tool-Based RAG FAQ Expert that:
- ✅ 90%+ accuracy with semantic understanding
- ✅ Agent decides when to search (not pre-loaded context)
- ✅ Can perform multiple searches to gather complete information
- ✅ Full knowledge base coverage (18 documents, 212 chunks)
- ✅ Handles natural language, synonyms, and complex queries
- ✅ Provides source citations with confidence scores
- ✅ Better token efficiency (only retrieves what's needed)

**Impact**: 
- **10x better coverage** - Entire knowledge base vs 10 FAQs
- **2x better accuracy** - 90% vs 45% success rate
- **Better UX** - Natural language understanding vs exact keyword matching
- **Agent autonomy** - Decides search strategy based on question complexity

---

## 🏗️ Architecture

### Traditional RAG (Context Injection)
```
User Question → Vector Search → Inject ALL Chunks into Prompt → LLM → Answer
                 (fixed)          (uses tokens)
```

### Tool-Based RAG (This Lesson)
```
User Question → Agent Thinks → Calls search_knowledge_base(query) → Results → Agent Reasons → Answer
                    ↓                                                           ↑
                Can search multiple times with different queries ──────────────┘
```

### RAG Pipeline (AI Enabled)
1. **Agent Receives Question**: Agent analyzes the user's question
2. **Autonomous Tool Decision**: Agent decides if/when/how to search
3. **Tool Call - Vector Search**: Agent calls `search_knowledge_base_tool(query, top_k)`
4. **Results Processing**: Agent receives search results as JSON
5. **Multi-Step Reasoning**: Agent can make additional searches if needed
6. **Answer Generation**: Agent synthesizes answer from tool results
7. **Source Citations**: Return sources with similarity scores and tool calls made

### Manual Fallback (AI Disabled)
1. **Keyword Matching**: Simple string matching in predefined FAQs
2. **Canned Responses**: Return pre-written answers
3. **No Context**: No understanding of synonyms or natural language

---

## 🔧 Feature Flag: `ENABLE_AI_FAQ_RAG`

Control the FAQ system mode with this environment variable in your `.env` file:

```bash
# Disable AI - Manual keyword matching (40-50% accuracy)
ENABLE_AI_FAQ_RAG=false

# Enable AI - RAG with vector search and LLM (90%+ accuracy)
ENABLE_AI_FAQ_RAG=true
```

---

## 🚀 Getting Started

### Prerequisites

1. **Completed Lesson 1** or understand basic MAF concepts
2. **GitHub Token** for Copilot Models (free):
   ```bash
   export GITHUB_TOKEN=ghp_your_token_here
   ```
3. **Docker and Docker Compose** installed

### Step 1: Index the Knowledge Base

First, run the indexer to process documents and create embeddings:

```bash
# Start infrastructure and run indexer
docker compose -f docker-compose.infrastructure.yml --profile lesson-02 up faq-indexer -d

# Wait for indexing to complete (check logs)
docker logs techflow-faq-indexer -f
```

The indexer will:
- Parse 18 markdown documents from `knowledge-base/`
- Split them into semantic chunks using Docling
- Generate embeddings for each chunk
- Store in PostgreSQL with pgvector

**Expected output**: "✅ Successfully indexed 18 documents with 212 chunks"

### Step 2: Start the FAQ Expert Service

```bash
# Start the FAQ Expert service
docker compose -f docker-compose.infrastructure.yml --profile lesson-02 up faq-expert -d

# Check service health
curl http://localhost:8002/health
```

### Step 3: Test Manual Mode (AI Disabled)

```bash
# Ensure AI is disabled
export ENABLE_AI_FAQ_RAG=false

# Restart service
docker compose -f docker-compose.infrastructure.yml --profile lesson-02 restart faq-expert

# Test with a question
curl -X POST http://localhost:8002/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "How do I reset my password?"}'
```

**Expected behavior**:
- Uses keyword matching
- Returns generic canned response
- Only works if exact keywords match
- No source citations

### Step 4: Test AI Mode (RAG Enabled)

```bash
# Enable AI
export ENABLE_AI_FAQ_RAG=true

# Restart service
docker compose -f docker-compose.infrastructure.yml --profile lesson-02 restart faq-expert

# Test with the same question
curl -X POST http://localhost:8002/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "How do I reset my password?"}'

# Try a natural language variation
curl -X POST http://localhost:8002/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "I forgot my login credentials, what should I do?"}'

# Try a complex question
curl -X POST http://localhost:8002/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "What are the steps to import a large CSV file with contacts?"}'
```

**Expected behavior**:
- Uses semantic search to find relevant content
- Generates contextual answer from knowledge base
- Works with synonyms and natural language
- Provides source citations with similarity scores

---

## 📁 Project Structure

```
lesson-02-faq-expert/
├── Dockerfile              # FAQ service container
├── Dockerfile.indexer      # Knowledge indexer container
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── knowledge-base/        # Knowledge base documents
│   ├── kb-001-flowcrm-overview.md
│   ├── kb-002-flowcrm-pricing.md
│   ├── kb-003-create-first-contact.md
│   └── ... (18 total documents)
└── src/
    ├── indexer.py         # Document indexing with embeddings
    ├── agent.py           # RAG-powered AI agent
    ├── manual.py          # Manual keyword matching fallback
    └── main.py            # FastAPI application
```

---

## 🧪 Testing Scenarios

### Scenario 1: Exact Keyword Match
**Question**: "How much does FlowCRM cost?"

| Mode | Result |
|------|--------|
| Manual | ✅ Works - Has "pricing" keyword |
| AI-RAG | ✅ Works - Better context and details |

### Scenario 2: Natural Language Variation
**Question**: "What's your pricing model?"

| Mode | Result |
|------|--------|
| Manual | ⚠️ Partial - May miss if keywords differ |
| AI-RAG | ✅ Works - Understands semantic meaning |

### Scenario 3: Synonym Usage
**Question**: "Tell me about your subscription plans"

| Mode | Result |
|------|--------|
| Manual | ❌ Fails - No "pricing" keyword |
| AI-RAG | ✅ Works - Understands synonyms |

### Scenario 4: Complex Multi-Part Question
**Question**: "How do I import contacts from a CSV and handle duplicates?"

| Mode | Result |
|------|--------|
| Manual | ❌ Fails - Tries to match one topic |
| AI-RAG-Tool | ✅ **Superior** - Agent can search multiple times for different aspects |

### Scenario 5: Out of Domain
**Question**: "What's the weather today?"

| Mode | Result |
|------|--------|
| Manual | ❌ Generic fallback message |
| AI-RAG | ✅ Politely indicates not in knowledge base |

---

## 📊 Metrics Comparison

### Manual Mode (ENABLE_AI_FAQ_RAG=false)
- **Accuracy**: 40-50%
- **Coverage**: 10 predefined FAQs
- **Response Time**: ~0.1-0.2 seconds
- **Handles**: Only exact keyword matches
- **Limitations**: No semantic understanding, no context

### AI-RAG-Tool Mode (ENABLE_AI_FAQ_RAG=true)
- **Accuracy**: 90%+
- **Coverage**: Entire knowledge base (18 docs, 212 chunks)
- **Response Time**: ~1-4 seconds (agent reasoning + tool calls)
- **Handles**: Natural language, synonyms, complex queries, multi-part questions
- **Advantages**:
  - Agent decides when/how to search (autonomous)
  - Can make multiple tool calls for complex questions
  - Better token efficiency (only searches what's needed)
  - Transparent (see what agent searched for)
- **Tool Calls**: Typically 1-3 searches per question depending on complexity
- **Benefits**: Context-aware, source citations, handles variations

---

## 🎓 Key Concepts Learned

### 1. Tool-Based RAG vs Context Injection
**Context Injection (Traditional RAG)**:
- Pre-retrieve all context before LLM call
- Inject chunks directly into prompt
- Fixed, single search
- Uses more tokens (all context loaded)

**Tool-Based RAG (This Lesson)**:
- Agent decides when to search
- Can make multiple tool calls
- Dynamic, adaptive retrieval
- More efficient token usage

### 2. Agent Tools
- Functions that agents can call autonomously
- Defined with clear docstrings (agent reads these!)
- Return structured data (JSON) for agent processing
- Enable multi-step reasoning and iteration

### 3. Vector Embeddings
- Convert text to numerical vectors that capture semantic meaning
- Similar concepts have similar vectors (cosine similarity)
- Enables semantic search beyond keyword matching

### 4. Vector Databases
- **pgvector** extension for PostgreSQL
- Efficient similarity search with indexes (HNSW, IVFFlat)
- Store embeddings alongside relational data

### 5. Retrieval-Augmented Generation (RAG)
- Retrieve relevant context before/during generation
- Grounds LLM responses in your data
- Reduces hallucinations and improves accuracy
- Tool-based RAG adds agent autonomy

### 6. Chunking Strategies
- Split documents into semantic chunks
- Balance between context and precision
- Use Docling's HybridChunker for smart splitting

### 7. Embedding Models
- **text-embedding-3-small** (GitHub Models) - 1536 dimensions
- **nomic-embed-text** (Ollama/LM Studio) - 768 dimensions
- Must use same model for indexing and querying

---

## 🔍 Code Walkthrough

### agent.py - Tool-Based RAG

```python
# Define the tool that agent can call
async def search_knowledge_base_tool(query: str, top_k: int = 3) -> str:
    """
    Search the FlowCRM/FlowAnalytics knowledge base.
    
    Use this tool when you need information about products, features, or support.
    Args:
        query: Search query with specific keywords
        top_k: Number of results (default: 3, max: 5)
    
    Returns:
        JSON with relevant documentation chunks
    """
    results = search_knowledge_base(query, top_k)
    return json.dumps({"results": [...], "count": len(results)})

# Create agent with the tool
agent = ChatAgent(
    chat_client=chat_client,
    instructions="""You are an FAQ assistant.
    
    To answer questions:
    1. Use search_knowledge_base tool to find relevant docs
    2. You can search multiple times if needed
    3. Only provide info from search results
    4. Cite your sources""",
    tools=[search_knowledge_base_tool]  # Register tool
)

# Agent autonomously decides when to call the tool
response = await agent.run(user_question)
```

### Vector Search Function

```python
def search_knowledge_base(query: str, top_k: int = 3) -> List[Dict]:
    """Search using vector similarity"""
    # 1. Generate embedding for query
    query_embedding = generate_embedding(query)
    
    # 2. Find top K similar chunks
    # Uses cosine distance operator: <=>
    cur.execute("""
        SELECT content, metadata, title, filename,
               1 - (embedding <=> %s::vector) as similarity
        FROM kb_chunks c
        JOIN kb_documents d ON c.document_id = d.id
        ORDER BY embedding <=> %s::vector
        LIMIT %s
    """, (query_embedding, query_embedding, top_k))
    
    return results
```

### main.py - Feature Flag Logic

```python
@app.post("/ask")
def ask_question(request: FAQRequest):
    """Route based on feature flag"""
    ai_enabled = os.getenv("ENABLE_AI_FAQ_RAG", "false").lower() == "true"
    
    if ai_enabled:
        return process_faq_ai(request.question)  # Tool-based RAG
    else:
        return process_faq_manual(request.question)  # Keyword matching
```

---

## 🐛 Troubleshooting

### Indexer Fails
```bash
# Check PostgreSQL is running
docker ps | grep postgres

# Check indexer logs
docker logs techflow-faq-indexer

# Verify tables exist
docker exec -it techflow-postgres psql -U techflow_user -d techflow -c "\dt"
```

### No Results from Vector Search
```bash
# Verify embeddings exist
docker exec -it techflow-postgres psql -U techflow_user -d techflow \
  -c "SELECT COUNT(*) FROM kb_chunks WHERE embedding IS NOT NULL;"

# Should return 212
```

### Service Not Responding
```bash
# Check service status
docker ps -a | grep faq-expert

# View logs
docker logs techflow-faq-expert -f

# Rebuild if needed
docker compose -f docker-compose.infrastructure.yml --profile lesson-02 up faq-expert --build -d
```

---

## 🎯 Next Steps

After mastering RAG with lesson-02, you're ready for:

**Lesson 3: Smart Router** - Add intelligent ticket routing with classification and function calling

**Advanced Topics**:
- Fine-tune chunking strategies for your documents
- Implement hybrid search (vector + keyword)
- Add query rewriting for better retrieval
- Implement caching for repeated questions
- Add conversation memory for follow-up questions

---

## 📚 Additional Resources

- [Microsoft Agent Framework Documentation](https://microsoft.github.io/agent-framework/)
- [RAG Best Practices](https://learn.microsoft.com/en-us/azure/developer/ai/augment-llm-rag-fine-tuning)
- [pgvector Documentation](https://github.com/pgvector/pgvector)
- [Docling Documentation](https://github.com/DS4SD/docling)
- [Vector Similarity Search](https://en.wikipedia.org/wiki/Cosine_similarity)

---

## 💡 Pro Tips

1. **Chunk Size Matters**: Too small = loss of context, too large = poor precision
2. **Top-K Selection**: Start with 3-5 chunks, adjust based on results
3. **Reranking**: Consider adding a reranking step for better accuracy
4. **Caching**: Cache embeddings and common queries to reduce costs
5. **Monitoring**: Track similarity scores to identify when knowledge base needs updates

---

**Ready to see AI transform FAQ handling? Start the service and toggle the feature flag!** 🚀
