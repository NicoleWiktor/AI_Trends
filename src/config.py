"""
Configuration module for AI News & Research Tracker with OpenAI Priority

This file should:
- Load environment variables from .env file
- Provide centralized configuration settings with OpenAI as primary LLM
- Include fallback options for free alternatives
- Validate required configuration values
- Handle different environments (dev, prod, test)
"""

import os
from typing import Optional
from pydantic_settings import BaseSettings
from pydantic import Field, validator

class Settings(BaseSettings):
    """Configuration settings for AI News & Research Tracker"""
    
    # AI API Keys
    openai_api_key: str = Field(..., description="OpenAI API key (required)")
    
    # LLM Configuration
    llm_provider: str = Field(default="openai", description="Primary LLM provider")
    llm_model: str = Field(default="gpt-4", description="OpenAI model to use")
    llm_temperature: float = Field(default=0.1, description="LLM creativity level (0.0-1.0)")
    
    # Database Configuration
    database_url: str = Field(default="sqlite:///./ai_news.db", description="Database connection string")
    
    # Application Settings
    app_name: str = Field(default="AI News & Research Tracker", description="Application name")
    debug: bool = Field(default=False, description="Enable debug mode")
    log_level: str = Field(default="INFO", description="Logging level")
    
    # Content Processing Settings
    chunk_size: int = Field(default=1000, description="Text chunk size for processing")
    embedding_model: str = Field(default="text-embedding-ada-002", description="OpenAI embedding model")
    
    # Web Scraping Settings
    user_agent: str = Field(default="AI-News-Tracker/1.0", description="User agent for web requests")
    request_timeout: int = Field(default=30, description="Request timeout in seconds")
    
    # RAG Settings
    retrieval_top_k: int = Field(default=5, description="Number of chunks to retrieve")
    similarity_threshold: float = Field(default=0.7, description="Minimum similarity score")
    
    # Processing Settings
    processing_frequency: str = Field(default="daily", description="Default processing frequency")
    web_search_enabled: bool = Field(default=True, description="Enable web search fallback")
    
    # Validation
    @validator('openai_api_key')
    def validate_openai_key(cls, v):
        if not v or v == "your_openai_api_key_here":
            raise ValueError("OpenAI API key is required")
        if not v.startswith('sk-'):
            raise ValueError("OpenAI API key must start with 'sk-'")
        return v
    
    @validator('llm_temperature')
    def validate_temperature(cls, v):
        if not 0.0 <= v <= 1.0:
            raise ValueError("Temperature must be between 0.0 and 1.0")
        return v
    
    @validator('chunk_size')
    def validate_chunk_size(cls, v):
        if v < 100 or v > 10000:
            raise ValueError("Chunk size must be between 100 and 10000")
        return v
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False

# Create global settings instance
settings = Settings()

# Configuration validation function
def validate_config():
    """Validate that all required configuration is present"""
    try:
        # Test OpenAI API key format
        if not settings.openai_api_key.startswith('sk-'):
            raise ValueError("Invalid OpenAI API key format")
        
        # Test database URL format
        if not settings.database_url.startswith(('sqlite:///', 'postgresql://', 'mysql://')):
            raise ValueError("Invalid database URL format")
        
        print("Configuration validation passed!")
        return True
        
    except Exception as e:
        print(f"Configuration validation failed: {e}")
        return False

# Validate configuration on module import
if __name__ == "__main__":
    validate_config()
else:
    # Only validate in debug mode to avoid startup delays
    if settings.debug:
        validate_config()
