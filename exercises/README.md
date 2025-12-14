# Exercises

This directory contains hands-on exercises to practice and validate your learning.

## 📋 Available Exercises

### ✅ Exercise 1.1: Build Your First AI Agents
**Module:** Foundations of AI Agents  
**Prerequisite:** Complete Lesson 1.1  
**Time:** 30-45 minutes

**What you'll build:**
- Customer Service Agent
- Data Analyst Agent  
- Creative Marketing Agent

**[Start Exercise 1.1 →](exercise-1.1/)**

---

### 🔜 Exercise 1.2: Advanced Agent Instructions
**Status:** Coming soon  
**Module:** Foundations of AI Agents  
**Prerequisite:** Complete Exercise 1.1

---

### 🔜 Exercise 1.3: Conversational Agents with Memory
**Status:** Coming soon  
**Module:** Foundations of AI Agents  
**Prerequisite:** Complete Exercise 1.2

---

## 🎯 How Exercises Work

1. **Read the README** - Understand requirements and objectives
2. **Complete the code** - Fill in TODOs in `solution.py`
3. **Test locally** - Run `pytest test_*.py -v`
4. **Iterate** - Refine based on test feedback
5. **Submit PR** - Get automated feedback from GitHub Actions
6. **Pass tests** - Advance to the next lesson!

## ✅ Exercise Checklist

Before submitting:
- [ ] Read the exercise README completely
- [ ] Understand acceptance criteria
- [ ] Complete all TODO sections
- [ ] Run tests locally and see them pass
- [ ] Review your code for quality
- [ ] Commit and push your changes

## 🧪 Running Tests

```bash
# Navigate to exercise directory
cd exercises/exercise-1.1

# Run tests with verbose output
pytest test_agents.py -v

# Run tests with detailed failure info
pytest test_agents.py -v --tb=short

# Run specific test
pytest test_agents.py::TestAgentCreation::test_customer_service_agent_name -v
```

## 📊 Test Output

Tests provide clear feedback:
- ✅ **PASSED** - Component works correctly
- ❌ **FAILED** - Review the error message for guidance
- ⚠️ **ERROR** - Check your code syntax and imports

## 💡 Tips for Success

### When Tests Fail:
1. **Read error messages carefully** - They tell you what's expected
2. **Check agent names** - Must match exactly (case-sensitive)
3. **Review instructions** - Should be detailed and domain-specific
4. **Test incrementally** - Fix one test at a time
5. **Compare with examples** - Review the lesson notebook

### Writing Good Instructions:
- Be specific about behavior and tone
- Include domain expertise expectations
- Mention how to structure responses
- Define what to prioritize
- Give examples when helpful

### Common Issues:
- **"ModuleNotFoundError"** - Activate virtual environment
- **"No authentication configured"** - Check your `.env` file
- **Instructions too short** - Add more detail (>50 characters)
- **Wrong agent behavior** - Refine your instructions

## 🆘 Getting Help

If you're stuck:
1. Review the lesson material
2. Read the test output carefully
3. Check the exercise README
4. Look at provided examples
5. Verify your environment setup
6. Use GitHub Discussions

## 📈 Progress Tracking

Your progress is automatically tracked through:
- ✅ Completed exercises in your Git history
- 🎯 GitHub Actions test results
- 📊 PR comments with feedback
- 🏆 Module completion badges

## 🎓 Learning Philosophy

Exercises are designed to:
- **Build on previous knowledge** - Each exercise uses prior concepts
- **Encourage experimentation** - Try different approaches
- **Provide immediate feedback** - Know if you're on track
- **Simulate real-world** - Use production patterns and tools
- **Foster independence** - Learn to debug and iterate

---

**Ready to practice?** Start with [Exercise 1.1](exercise-1.1/) ! 🚀
