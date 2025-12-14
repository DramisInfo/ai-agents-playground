# Getting Started with Module 1, Lesson 1.1

Welcome to your first lesson! This guide will help you set up your environment and get started.

## Prerequisites

- Python 3.10 or later
- Git installed
- A text editor or IDE (VS Code recommended)

## Setup Steps

### 1. Clone the Repository (if you haven't already)

```bash
git clone <repository-url>
cd ai-agents-playground
```

### 2. Create a Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate it
# On Linux/Mac:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Authentication

Copy the example environment file:

```bash
cp .env.example .env
```

Then edit `.env` with your credentials. You have two options:

#### Option A: GitHub Models (Recommended for Free Access)

1. Go to [GitHub Settings > Tokens](https://github.com/settings/tokens)
2. Create a new token
3. Add it to `.env`:

```bash
GITHUB_TOKEN=your_token_here
```

#### Option B: Azure OpenAI

If you have Azure OpenAI access:

```bash
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_DEPLOYMENT_NAME=gpt-4o-mini
```

### 5. Start Jupyter

```bash
jupyter notebook
```

Navigate to `training-materials/module-1-foundations/lesson-1.1-first-agent.ipynb`

## What You'll Learn

- What AI agents are and how they differ from simple LLM calls
- How to create a ChatAgent with the Microsoft Agent Framework
- How to customize agent behavior with instructions
- How to test and interact with agents

## Need Help?

- Review the [main README](../../README.md)
- Check the [lesson notebook](lesson-1.1-first-agent.ipynb)
- Ensure your `.env` file is properly configured

---

**Ready?** Open the Jupyter notebook and start learning! 🚀
