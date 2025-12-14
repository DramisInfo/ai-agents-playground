# Exercise 1.1: Build Your First AI Agents

## 🎯 Objective

Apply your knowledge from Lesson 1.1 to create specialized AI agents with distinct personalities and purposes. You'll demonstrate understanding of agent construction, instruction design, and testing.

## 📋 Requirements

Create three specialized agents, each with:

1. **Customer Service Agent**
   - Name: `CustomerServiceAgent`
   - Domain: Customer support and assistance
   - Personality: Professional, empathetic, solution-oriented
   - Should handle inquiries with patience and offer helpful solutions

2. **Data Analyst Agent**
   - Name: `DataAnalystAgent`  
   - Domain: Data analysis and insights
   - Personality: Analytical, precise, detail-oriented
   - Should provide data-driven insights and explain findings clearly

3. **Creative Marketing Agent**
   - Name: `MarketingAgent`
   - Domain: Marketing and content creation
   - Personality: Creative, persuasive, engaging
   - Should create compelling copy and marketing ideas

## 🎓 Learning Goals

- Practice creating ChatAgents with specific purposes
- Write effective instructions that shape agent behavior
- Test agents to validate they meet requirements
- Understand how instructions influence agent responses

## 📝 Instructions

1. Open `solution.py` and complete the three agent creation functions
2. Each function should return a properly configured ChatAgent
3. Write clear, specific instructions that guide agent behavior
4. Run `python test_agents.py` to validate your solution
5. Iterate on your instructions until all tests pass

## ✅ Acceptance Criteria

Your solution must:

- [ ] Create all three agents with correct names
- [ ] Each agent must have appropriate instructions for its domain
- [ ] Agents must respond appropriately to domain-specific questions
- [ ] Customer Service Agent shows empathy and offers solutions
- [ ] Data Analyst Agent provides structured, analytical responses
- [ ] Marketing Agent generates creative and engaging content
- [ ] All automated tests pass

## 🧪 Testing Your Solution

Run the test suite:

```bash
# From the exercise-1.1 directory
python test_agents.py
```

The tests will verify:
- Agent creation with correct names
- Instruction quality and relevance
- Response patterns match expected behavior
- Domain-specific knowledge and tone

## 💡 Tips

- **Be Specific**: Clear, detailed instructions produce better results
- **Test Iteratively**: Run tests frequently as you develop
- **Read Test Output**: Failed tests provide hints about what to improve
- **Think About Tone**: Instructions should define not just what to do, but *how* to respond
- **Use Examples**: Include example behaviors in instructions when helpful

## 🚀 Bonus Challenges (Optional)

If you finish early, try these enhancements:

1. Add a fourth custom agent of your own design
2. Create instructions that make agents collaborate
3. Test your agents with edge cases and tricky questions
4. Experiment with different instruction formats (bullets, narrative, examples)

## 📚 Resources

- [Lesson 1.1 Notebook](../../training-materials/module-1-foundations/lesson-1.1-first-agent.ipynb)
- [ChatAgent Documentation](https://learn.microsoft.com/en-us/python/api/agent-framework-core/agent_framework.chatagent)
- [Effective Prompting Guide](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/prompt-engineering)

## 🆘 Getting Help

If you're stuck:
1. Review the lesson notebook for examples
2. Check that your `.env` file is configured correctly
3. Read the test failure messages carefully
4. Try simpler instructions first, then refine

---

**Good luck! Remember: The key to great agents is great instructions. 🚀**
