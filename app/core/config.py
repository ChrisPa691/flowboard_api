"""Application configuration and settings management.

This file should include:
- Pydantic Settings class for environment variables
- Database connection settings (DATABASE_URL)
- JWT authentication settings (SECRET_KEY, ALGORITHM, TOKEN_EXPIRE_MINUTES)
- API keys for external services (AWS, email, etc.)
- CORS origins configuration
- Application environment (dev, staging, production)
- Logging configuration
- Feature flags
- Settings validation
- Global settings instance

Example structure:
    from pydantic_settings import BaseSettings
    
    class Settings(BaseSettings):
        # Database
        DATABASE_URL: str
        
        # JWT
        SECRET_KEY: str
        ALGORITHM: str = "HS256"
        ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
        
        # AWS
        AWS_ACCESS_KEY_ID: str | None = None
        AWS_SECRET_ACCESS_KEY: str | None = None
        
        class Config:
            env_file = ".env"
            case_sensitive = True
    
    settings = Settings()
"""
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Database
    DATABASE_URL: str
    
    # JWT
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # AWS
    AWS_ACCESS_KEY_ID: str | None = None
    AWS_SECRET_ACCESS_KEY: str | None = None
    
    class Config:
        env_file = ".env"
        case_sensitive = True
