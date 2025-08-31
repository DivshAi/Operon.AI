# AI Agentic Platform - Configuration
"""
Configuration loading and validation for the AI Agentic Platform.
"""

import os
from typing import Optional
from pydantic import BaseSettings, validator
from datetime import timedelta

class Settings(BaseSettings):
    # Database configuration
    database_url: str = "sqlite:///./ai_agentic_platform.db"
    
    # JWT configuration
    secret_key: str = "your-secret-key-here-change-this-in-production"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    
    # LLM configuration
    ollama_host: str = "http://localhost:11434"
    openai_api_key: Optional[str] = None
    anthropic_api_key: Optional[str] = None
    azure_openai_endpoint: Optional[str] = None
    azure_openai_api_key: Optional[str] = None
    
    # Application configuration
    app_name: str = "AI Agentic Platform"
    version: str = "1.0.0"
    
    # Environment
    environment: str = "development"  # development, staging, production
    
    # Logging
    log_level: str = "INFO"
    
    @validator("environment")
    def validate_environment(cls, v):
        if v not in ["development", "staging", "production"]:
            raise ValueError("Environment must be one of: development, staging, production")
        return v
    
    class Config:
        env_file = ".env"
        case_sensitive = True

# Load settings
settings = Settings()

# Export configuration values for use throughout the application
DATABASE_URL = settings.database_url
SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes
OLLAMA_HOST = settings.ollama_host