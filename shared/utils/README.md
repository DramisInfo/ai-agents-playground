# Shared Utilities

Common Python utilities used across all lessons.

## Available Modules

### `config.py`
Configuration management with environment variable loading.

```python
from shared.utils.config import load_config

config = load_config()
print(config.database.connection_string)
print(config.github.model)
```

### `metrics.py`
Standardized metrics collection for before/after comparison.

```python
from shared.utils.metrics import MetricsCollector, get_feature_flag, display_mode_banner

# Check feature flag
ai_enabled = get_feature_flag('ENABLE_AI_SUPPORT_BOT')

# Display mode
display_mode_banner("AI" if ai_enabled else "Manual", "Support Bot")

# Collect metrics
collector = MetricsCollector("lesson-01-support-bot")
collector.record_request(response_time=3.2, success=True, mode="AI")
collector.display_summary()
```

## Usage in Lessons

Each lesson imports these utilities to:
1. Load configuration consistently
2. Check feature flags
3. Collect and display metrics
4. Show mode banners

This ensures standardized behavior and easy before/after comparison across all lessons.
