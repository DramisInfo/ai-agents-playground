"""
Exercise 1.1: Build Your First AI Agents

Complete the functions below to create three specialized agents.
Each agent should have appropriate instructions for its domain.

Run `python test_agents.py` to validate your solution.
"""

import os
from dotenv import load_dotenv
from agent_framework import ChatAgent

# Load environment variables
load_dotenv()


def create_chat_client():
    """
    Creates and returns a chat client based on available authentication.
    
    This function is provided for you - no need to modify it.
    """
    github_token = os.getenv("GITHUB_TOKEN")
    azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    
    if github_token:
        # Use GitHub Models
        from agent_framework.openai import OpenAIChatClient
        return OpenAIChatClient(
            model_id="gpt-4o-mini",
            api_key=github_token,
            base_url="https://models.inference.ai.azure.com"
        )
    elif azure_endpoint:
        # Use Azure OpenAI
        from agent_framework.azure import AzureOpenAIChatClient
        from azure.identity import DefaultAzureCredential
        return AzureOpenAIChatClient(
            endpoint=azure_endpoint,
            credential=DefaultAzureCredential(),
            model_id=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME", "gpt-4o-mini")
        )
    else:
        raise ValueError(
            "No authentication configured. "
            "Please set GITHUB_TOKEN or AZURE_OPENAI_ENDPOINT in your .env file"
        )


def create_customer_service_agent(chat_client) -> ChatAgent:
    """
    Create a customer service agent.
    
    Requirements:
    - Name: "CustomerServiceAgent"
    - Professional, empathetic, solution-oriented personality
    - Should handle customer inquiries with patience
    - Offers helpful solutions and next steps
    
    Args:
        chat_client: The chat client to use for the agent
        
    Returns:
        ChatAgent: A configured customer service agent
    """
    # TODO: Implement this function
    # Create and return a ChatAgent with appropriate instructions
    
    agent = ChatAgent(
        chat_client=chat_client,
        name="CustomerServiceAgent",
        description="A professional customer service assistant",
        instructions="""
        # TODO: Write your instructions here
        # Think about:
        # - How should this agent greet customers?
        # - What tone should it use?
        # - How should it handle problems or complaints?
        # - What should it prioritize in responses?
        """
    )
    
    return agent


def create_data_analyst_agent(chat_client) -> ChatAgent:
    """
    Create a data analyst agent.
    
    Requirements:
    - Name: "DataAnalystAgent"
    - Analytical, precise, detail-oriented personality
    - Provides data-driven insights
    - Explains findings clearly with structure
    
    Args:
        chat_client: The chat client to use for the agent
        
    Returns:
        ChatAgent: A configured data analyst agent
    """
    # TODO: Implement this function
    # Create and return a ChatAgent with appropriate instructions
    
    agent = ChatAgent(
        chat_client=chat_client,
        name="DataAnalystAgent",
        description="An analytical data insights specialist",
        instructions="""
        # TODO: Write your instructions here
        # Think about:
        # - How should this agent approach questions?
        # - What structure should responses have?
        # - How should it present data and insights?
        # - What level of detail is appropriate?
        """
    )
    
    return agent


def create_marketing_agent(chat_client) -> ChatAgent:
    """
    Create a marketing and content creation agent.
    
    Requirements:
    - Name: "MarketingAgent"
    - Creative, persuasive, engaging personality
    - Creates compelling marketing copy
    - Generates innovative marketing ideas
    
    Args:
        chat_client: The chat client to use for the agent
        
    Returns:
        ChatAgent: A configured marketing agent
    """
    # TODO: Implement this function
    # Create and return a ChatAgent with appropriate instructions
    
    agent = ChatAgent(
        chat_client=chat_client,
        name="MarketingAgent",
        description="A creative marketing and content specialist",
        instructions="""
        # TODO: Write your instructions here
        # Think about:
        # - How should this agent approach creative tasks?
        # - What makes marketing copy compelling?
        # - How should it balance creativity with persuasion?
        # - What tone resonates with audiences?
        """
    )
    
    return agent


async def main():
    """
    Test your agents interactively.
    Run this to see how your agents respond!
    """
    print("Creating agents...")
    chat_client = create_chat_client()
    
    cs_agent = create_customer_service_agent(chat_client)
    da_agent = create_data_analyst_agent(chat_client)
    mk_agent = create_marketing_agent(chat_client)
    
    print("\n" + "="*60)
    print("Testing Customer Service Agent")
    print("="*60)
    response = await cs_agent.run("I received a damaged product. What should I do?")
    print(response.text)
    
    print("\n" + "="*60)
    print("Testing Data Analyst Agent")
    print("="*60)
    response = await da_agent.run("What trends should I look for in sales data?")
    print(response.text)
    
    print("\n" + "="*60)
    print("Testing Marketing Agent")
    print("="*60)
    response = await mk_agent.run("Create a tagline for an eco-friendly water bottle.")
    print(response.text)
    
    print("\n✅ Interactive testing complete!")
    print("Run 'python test_agents.py' for automated validation.")


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
