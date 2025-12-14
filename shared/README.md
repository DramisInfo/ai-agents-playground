# Shared Components

This directory contains reusable components shared across all lessons.

## Structure

```
shared/
├── db/
│   └── init/              # Database initialization scripts
│       └── 01-init.sql    # TechFlow schema with all tables
├── utils/                 # Common Python utilities
│   ├── config.py         # Configuration management
│   ├── metrics.py        # Metrics collection and display
│   └── README.md         # Utils documentation
├── tools/                 # Reusable agent tools (lessons will add these)
└── models/                # Shared data models and schemas (lessons will add these)
```

## Purpose

These shared components promote code reuse and demonstrate how to build maintainable AI agent systems. Each lesson leverages these shared resources, showing how foundational code evolves into more complex solutions.

## Current Components

### Database Initialization (`db/init/01-init.sql`)
- Creates PostgreSQL schema for all lessons
- Tables for tickets, leads, invoices, reports, etc.
- Sample data for testing
- Auto-runs when infrastructure starts

### Configuration Module (`utils/config.py`)
- Loads environment variables
- Validates configuration
- Provides typed config objects
- Handles all infrastructure connections

### Metrics Module (`utils/metrics.py`)
- Standardized metrics collection
- Before/after comparison support
- Feature flag helpers
- Display utilities

## Usage Example

```python
# In any lesson
from shared.utils.config import load_config
from shared.utils.metrics import MetricsCollector, get_feature_flag

# Load config
config = load_config()

# Check feature flag
ai_enabled = get_feature_flag('ENABLE_AI_SUPPORT_BOT')

# Collect metrics
metrics = MetricsCollector("lesson-01")
metrics.record_request(response_time=2.5, success=True, mode="AI")
```

## Adding New Components

When creating new lessons, consider if any functionality should be added to the shared directory for reuse in future lessons. This is particularly important for:

- Common database operations
- Reusable agent tools (API clients, parsers, etc.)
- Data models used across multiple lessons
- Utility functions used frequently

Place them in the appropriate subdirectory:
- **`tools/`** - Reusable agent tools and external integrations
- **`models/`** - Pydantic models, dataclasses, schemas
- **`utils/`** - Helper functions and utilities
