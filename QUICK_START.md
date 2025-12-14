# 🚀 Quick Start Guide

Get up and running with AI Agents Playground in 5 minutes!

## Step 1: Clone and Setup

```bash
# Clone the repository
git clone <repository-url>
cd ai-agents-playground

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Step 2: Configure Authentication

Choose one authentication method:

### Option A: GitHub Models (Free - Recommended for Learning)

1. Get a token: https://github.com/settings/tokens
2. Create `.env` file:

```bash
GITHUB_TOKEN=your_github_token_here
```

### Option B: Azure OpenAI

```bash
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_DEPLOYMENT_NAME=gpt-4o-mini
```

## Step 3: Verify Setup

```bash
# Test that everything works
python -c "from shared import create_chat_client; print('✅ Setup successful!')"
```

## Step 4: Start Learning!

### Option 1: Interactive Notebook

```bash
jupyter notebook
# Navigate to: training-materials/module-1-foundations/lesson-1.1-first-agent.ipynb
```

### Option 2: Jump to Exercise

```bash
cd exercises/exercise-1.1
python solution.py
```

## 📁 Project Structure

```
ai-agents-playground/
├── training-materials/        # Lesson notebooks
│   └── module-1-foundations/
│       └── lesson-1.1-first-agent.ipynb
├── exercises/                 # Hands-on exercises
│   └── exercise-1.1/
│       ├── README.md
│       ├── solution.py
│       └── test_agents.py
├── shared/                    # Reusable utilities
├── .github/workflows/         # Automated validation
├── requirements.txt           # Python dependencies
└── .env.example              # Configuration template
```

## 🎯 Your Learning Path

1. **Read** the lesson notebook
2. **Code** along with examples
3. **Complete** the exercise
4. **Test** your solution: `pytest test_agents.py -v`
5. **Submit** a PR for feedback
6. **Advance** to the next lesson!

## ⚡ Quick Commands

```bash
# Run tests for current exercise
pytest test_agents.py -v

# Run tests with detailed output
pytest test_agents.py -v --tb=short

# Start Jupyter
jupyter notebook

# Activate virtual environment
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

## 🆘 Troubleshooting

### "No authentication configured"
- Check that `.env` file exists
- Verify your token/credentials are set
- Ensure `.env` is in the project root

### "Module not found"
- Activate your virtual environment
- Run: `pip install -r requirements.txt`

### "Jupyter not found"
- Install: `pip install jupyter`
- Or use: `pip install -r requirements.txt`

### Tests failing
- Read test output carefully
- Review lesson examples
- Check agent instructions are detailed enough
- Verify agent names match exactly

## 📚 Resources

- [Full README](README.md)
- [Microsoft Agent Framework Docs](https://learn.microsoft.com/en-us/agent-framework/)
- [Module 1 Guide](training-materials/module-1-foundations/MODULE_README.md)

---

**Ready to build intelligent agents? Let's go! 🤖**
