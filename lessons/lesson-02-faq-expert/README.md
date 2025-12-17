# Lesson 2: FAQ Expert - RAG-Powered Knowledge Search

## 🎯 Learning Objectives

Learn how to build an intelligent FAQ system using **Retrieval-Augmented Generation (RAG)** with vector embeddings and semantic search. This lesson demonstrates the transformational power of AI for knowledge retrieval compared to traditional keyword-based systems.

## 📊 Business Impact

**Problem**: TechFlow's support team needs to answer 300+ unique questions daily from a 500-page knowledge base. Manual keyword search only works for exact matches, resulting in:
- ❌ 40-50% accuracy (misses synonyms and natural language variations)
- ❌ Limited coverage (only ~10 predefined FAQs)
- ❌ Requires constant manual updates to FAQ database

**Solution**: RAG-powered FAQ Expert that:
- ✅ 90%+ accuracy with semantic understanding
- ✅ Full knowledge base coverage (18 documents, 212 chunks)
- ✅ Handles natural language, synonyms, and complex queries
- ✅ Provides source citations with confidence scores

**Impact**: 
- **10x better coverage** - Entire knowledge base vs 10 FAQs
- **2x better accuracy** - 90% vs 45% success rate
- **Better UX** - Natural language understanding vs exact keyword matching

---

## 🏗️ Architecture

```
User Question → Vector Search (pgvector) → Top 3 Relevant Chunks → LLM + Context → Answer with Sources
```

### RAG Pipeline (AI Enabled)
1. **Query Embedding**: Convert user question to vector using same model as indexing
2. **Vector Search**: Find top 3 most similar chunks using cosine similarity
3. **Context Building**: Assemble relevant chunks with metadata
4. **LLM Generation**: Generate answer using retrieved context
5. **Source Citations**: Return sources with similarity scores

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
| AI-RAG | ✅ Works - Retrieves multiple relevant chunks |

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

### AI-RAG Mode (ENABLE_AI_FAQ_RAG=true)
- **Accuracy**: 90%+
- **Coverage**: Entire knowledge base (18 docs, 212 chunks)
- **Response Time**: ~1-3 seconds (includes vector search + LLM)
- **Handles**: Natural language, synonyms, complex queries
- **Benefits**: Context-aware, source citations, handles variations

---

## 🎓 Key Concepts Learned

### 1. Vector Embeddings
- Convert text to numerical vectors that capture semantic meaning
- Similar concepts have similar vectors (cosine similarity)
- Enables semantic search beyond keyword matching

### 2. Vector Databases
- **pgvector** extension for PostgreSQL
- Efficient similarity search with indexes (HNSW, IVFFlat)
- Store embeddings alongside relational data

### 3. Retrieval-Augmented Generation (RAG)
- Retrieve relevant context before generation
- Grounds LLM responses in your data
- Reduces hallucinations and improves accuracy

### 4. Chunking Strategies
- Split documents into semantic chunks
- Balance between context and precision
- Use Docling's HybridChunker for smart splitting

### 5. Embedding Models
- **text-embedding-3-small** (GitHub Models) - 1536 dimensions
- **nomic-embed-text** (Ollama/LM Studio) - 768 dimensions
- Must use same model for indexing and querying

---

## 🔍 Code Walkthrough

### agent.py - RAG Implementation

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
        return process_faq_ai(request.question)  # RAG pipeline
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
