"""
Shared Configuration Module

Loads and validates configuration from environment variables.
"""

import os
from typing import Optional
from dataclasses import dataclass


@dataclass
class DatabaseConfig:
    """PostgreSQL database configuration"""
    host: str
    port: int
    database: str
    user: str
    password: str
    
    @property
    def connection_string(self) -> str:
        return f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"


@dataclass
class RedisConfig:
    """Redis cache configuration"""
    host: str
    port: int
    password: Optional[str] = None
    
    @property
    def connection_string(self) -> str:
        if self.password:
            return f"redis://:{self.password}@{self.host}:{self.port}"
        return f"redis://{self.host}:{self.port}"


@dataclass
class QdrantConfig:
    """Qdrant vector database configuration"""
    host: str
    port: int
    api_key: Optional[str] = None
    
    @property
    def url(self) -> str:
        return f"http://{self.host}:{self.port}"


@dataclass
class GitHubConfig:
    """GitHub Copilot Models configuration"""
    token: str
    model: str = "gpt-4o"
    
    @property
    def is_configured(self) -> bool:
        return bool(self.token and self.token != "your_github_personal_access_token_here")


@dataclass
class AppConfig:
    """Complete application configuration"""
    database: DatabaseConfig
    redis: RedisConfig
    qdrant: QdrantConfig
    github: GitHubConfig
    log_level: str
    environment: str
    enable_metrics: bool
    
    @classmethod
    def from_env(cls) -> 'AppConfig':
        """Load configuration from environment variables"""
        return cls(
            database=DatabaseConfig(
                host=os.getenv('POSTGRES_HOST', 'postgres'),
                port=int(os.getenv('POSTGRES_PORT', 5432)),
                database=os.getenv('POSTGRES_DB', 'techflow'),
                user=os.getenv('POSTGRES_USER', 'techflow_user'),
                password=os.getenv('POSTGRES_PASSWORD', 'techflow_pass_change_in_production')
            ),
            redis=RedisConfig(
                host=os.getenv('REDIS_HOST', 'redis'),
                port=int(os.getenv('REDIS_PORT', 6379)),
                password=os.getenv('REDIS_PASSWORD')
            ),
            qdrant=QdrantConfig(
                host=os.getenv('QDRANT_HOST', 'qdrant'),
                port=int(os.getenv('QDRANT_PORT', 6333)),
                api_key=os.getenv('QDRANT_API_KEY')
            ),
            github=GitHubConfig(
                token=os.getenv('GITHUB_TOKEN', ''),
                model=os.getenv('GITHUB_MODEL', 'gpt-4o')
            ),
            log_level=os.getenv('LOG_LEVEL', 'INFO'),
            environment=os.getenv('ENVIRONMENT', 'development'),
            enable_metrics=os.getenv('ENABLE_METRICS', 'true').lower() == 'true'
        )
    
    def validate(self) -> list[str]:
        """Validate configuration and return list of issues"""
        issues = []
        
        if not self.github.is_configured:
            issues.append("GitHub token not configured in .env file")
        
        if not self.database.password or self.database.password == 'techflow_pass_change_in_production':
            issues.append("Using default database password - change for production")
        
        return issues


def load_config() -> AppConfig:
    """Load and validate application configuration"""
    config = AppConfig.from_env()
    
    issues = config.validate()
    if issues and config.environment == 'production':
        raise ValueError(f"Configuration issues in production: {', '.join(issues)}")
    
    return config
