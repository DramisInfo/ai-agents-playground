"""
Shared utilities package for AI Agents Playground.

This package provides common functionality used across lessons and exercises.
"""

from .utils import (
    load_environment,
    get_auth_method,
    create_chat_client,
    print_response,
    print_section_header,
)

__all__ = [
    "load_environment",
    "get_auth_method",
    "create_chat_client",
    "print_response",
    "print_section_header",
]
