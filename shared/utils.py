"""
Shared utilities for AI Agents Playground training.

This module provides common functionality used across lessons and exercises.
"""

import os
from typing import Optional
from dotenv import load_dotenv


def load_environment() -> None:
    """
    Load environment variables from .env file.
    
    This function loads environment variables needed for authentication
    and configuration across the training materials.
    """
    load_dotenv()


def get_auth_method() -> Optional[str]:
    """
    Determine which authentication method is available.
    
    Returns:
        str: "github" if GitHub token is available
             "azure" if Azure OpenAI configuration is available
             None if no authentication is configured
    """
    github_token = os.getenv("GITHUB_TOKEN")
    azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    
    if github_token:
        return "github"
    elif azure_endpoint:
        return "azure"
    return None


def create_chat_client():
    """
    Create and return an appropriate chat client based on available authentication.
    
    This is a convenience function that automatically selects the right client
    based on environment variables.
    
    Returns:
        A configured chat client (OpenAIChatClient or AzureOpenAIChatClient)
        
    Raises:
        ValueError: If no authentication method is configured
    """
    load_environment()
    auth_method = get_auth_method()
    
    if auth_method == "github":
        from agent_framework.openai import OpenAIChatClient
        return OpenAIChatClient(
            model_id="gpt-4o-mini",
            api_key=os.getenv("GITHUB_TOKEN"),
            base_url="https://models.inference.ai.azure.com"
        )
    elif auth_method == "azure":
        from agent_framework.azure import AzureOpenAIChatClient
        from azure.identity import DefaultAzureCredential
        return AzureOpenAIChatClient(
            endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            credential=DefaultAzureCredential(),
            model_id=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME", "gpt-4o-mini")
        )
    else:
        raise ValueError(
            "No authentication configured. "
            "Please set GITHUB_TOKEN or AZURE_OPENAI_ENDPOINT in your .env file. "
            "See .env.example for reference."
        )


def print_response(response, prefix: str = "Agent") -> None:
    """
    Pretty print an agent response.
    
    Args:
        response: The agent response object
        prefix: Label to display before the response (default: "Agent")
    """
    print(f"\n{prefix}: {response.text}\n")


def print_section_header(title: str, char: str = "=") -> None:
    """
    Print a formatted section header.
    
    Args:
        title: The section title
        char: Character to use for the border (default: "=")
    """
    width = max(60, len(title) + 4)
    border = char * width
    print(f"\n{border}")
    print(f"{title:^{width}}")
    print(f"{border}\n")
