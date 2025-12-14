# Quick Setup Guide

Get your AI Agents Playground environment ready in 5 minutes! This guide will help you set up all the infrastructure needed for the entire training program.

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

### Required Software

1. **Docker Desktop** (version 20.10 or later)
   - [Download for Windows](https://docs.docker.com/desktop/install/windows-install/)
   - [Download for Mac](https://docs.docker.com/desktop/install/mac-install/)
   - [Download for Linux](https://docs.docker.com/desktop/install/linux-install/)
   - Verify installation: `docker --version` and `docker-compose --version`

2. **Git** (version 2.30 or later)
   - [Download Git](https://git-scm.com/downloads)
   - Verify installation: `git --version`

3. **GitHub Account** (for free Copilot Models access)
   - [Sign up for GitHub](https://github.com/signup) if you don't have an account
   - [Get GitHub Copilot access](https://github.com/features/copilot)

### Optional (for local development)

- **Python 3.10+** - If you want to run code outside Docker
- **VS Code** - Recommended IDE with Docker and Python extensions

---

## 🚀 Step-by-Step Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-org/ai-agents-playground.git
cd ai-agents-playground
```

### Step 2: Configure Environment Variables

Create your `.env` file from the template:

```bash
cp .env.example .env
```

Edit the `.env` file and add your credentials:

```bash
# GitHub Copilot Models Configuration
GITHUB_TOKEN=your_github_personal_access_token_here
GITHUB_MODEL=gpt-4o  # or gpt-4o-mini for faster responses

# Database Configuration (auto-configured by Docker)
POSTGRES_HOST=postgres
POSTGRES_PORT=5432
POSTGRES_DB=techflow
POSTGRES_USER=techflow_user
POSTGRES_PASSWORD=techflow_pass_change_in_production

# Redis Configuration (auto-configured by Docker)
REDIS_HOST=redis
REDIS_PORT=6379

# Vector Database Configuration (auto-configured by Docker)
QDRANT_HOST=qdrant
QDRANT_PORT=6333

# Application Settings
LOG_LEVEL=INFO
ENVIRONMENT=development
```

#### Getting Your GitHub Token

1. Go to [GitHub Settings > Developer settings > Personal access tokens > Tokens (classic)](https://github.com/settings/tokens)
2. Click "Generate new token (classic)"
3. Give it a descriptive name like "AI Agents Playground"
4. Select scopes: `repo`, `read:org`, `read:user`
5. Click "Generate token"
6. Copy the token and paste it in your `.env` file

---

### Step 3: Start Shared Infrastructure

The training uses shared services across all lessons:

- **PostgreSQL** - Relational database for storing application data
- **Redis** - In-memory cache for session management and quick data access
- **Qdrant** - Vector database for RAG (Retrieval-Augmented Generation) lessons

Start all shared services with one command:

```bash
docker-compose -f docker-compose.infrastructure.yml up -d
```

Verify all services are running:

```bash
docker-compose -f docker-compose.infrastructure.yml ps
```

You should see:
```
NAME                STATUS              PORTS
postgres            Up                  5432->5432
redis               Up                  6379->6379
qdrant              Up                  6333->6333, 6334->6334
```

---

### Step 4: Verify Setup

Run the verification script to ensure everything is configured correctly:

```bash
docker-compose -f docker-compose.verify.yml up
```

This will:
✅ Test database connectivity  
✅ Verify Redis connection  
✅ Check Qdrant vector store  
✅ Validate GitHub token and Copilot Models access  
✅ Confirm all environment variables are set  

If all checks pass, you'll see:
```
✅ All systems operational! Ready to start learning.
```

---

## 🎓 You're Ready!

Your environment is now fully configured! Here's what you have:

| Service | Purpose | Access |
|---------|---------|--------|
| PostgreSQL | Application data storage | `localhost:5432` |
| Redis | Caching and sessions | `localhost:6379` |
| Qdrant | Vector storage for RAG | `localhost:6333` |
| Qdrant Dashboard | Vector DB management UI | `http://localhost:6334` |

---

## 📚 Next Steps

1. **Start with Lesson 1**: Navigate to `lessons/lesson-01-support-bot/`
2. **Read the lesson README**: Understand the business problem and solution
3. **Run the lesson**: Execute `docker-compose up` in the lesson folder
4. **Experiment**: Modify the code and see real-time results

---

## 🔧 Troubleshooting

### Docker Services Won't Start

**Problem**: Port conflicts or services not starting

**Solution**:
```bash
# Stop all running containers
docker-compose -f docker-compose.infrastructure.yml down

# Check for port conflicts
netstat -an | grep 5432  # PostgreSQL
netstat -an | grep 6379  # Redis
netstat -an | grep 6333  # Qdrant

# Remove any conflicting services or change ports in docker-compose.infrastructure.yml
```

### GitHub Token Authentication Fails

**Problem**: "Invalid credentials" or "Unauthorized" errors

**Solution**:
1. Verify your token is correctly copied in `.env` (no extra spaces)
2. Ensure token has required scopes (`repo`, `read:org`, `read:user`)
3. Check token hasn't expired in [GitHub Settings](https://github.com/settings/tokens)

### Database Connection Errors

**Problem**: Lessons can't connect to PostgreSQL

**Solution**:
```bash
# Restart infrastructure services
docker-compose -f docker-compose.infrastructure.yml restart

# Check PostgreSQL logs
docker-compose -f docker-compose.infrastructure.yml logs postgres

# Verify environment variables
docker-compose -f docker-compose.infrastructure.yml exec postgres env | grep POSTGRES
```

### Vector Database (Qdrant) Issues

**Problem**: RAG lessons fail to index or search documents

**Solution**:
```bash
# Check Qdrant is running
docker-compose -f docker-compose.infrastructure.yml ps qdrant

# View Qdrant dashboard
open http://localhost:6334

# Restart Qdrant
docker-compose -f docker-compose.infrastructure.yml restart qdrant
```

---

## 🛑 Stopping Services

When you're done for the day, stop the infrastructure services:

```bash
# Stop but keep data
docker-compose -f docker-compose.infrastructure.yml stop

# Stop and remove containers (keeps data volumes)
docker-compose -f docker-compose.infrastructure.yml down

# Stop and remove everything including data (fresh start)
docker-compose -f docker-compose.infrastructure.yml down -v
```

---

## 🔄 Updating

Pull the latest changes and restart services:

```bash
git pull origin main
docker-compose -f docker-compose.infrastructure.yml pull
docker-compose -f docker-compose.infrastructure.yml up -d
```

---

## 📞 Getting Help

- **Documentation Issues**: Check the README in each lesson folder
- **Setup Problems**: Review this guide's troubleshooting section
- **Technical Questions**: Open an issue on the GitHub repository
- **Community Support**: Join discussions in the repository

---

**Ready to transform TechFlow with AI agents?**  
**[Start with Lesson 1: The Support Bot →](../lessons/lesson-01-support-bot/README.md)**
