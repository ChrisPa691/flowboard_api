"""Database session management and connection.

This file should include:
- SQLAlchemy engine creation
- SessionLocal factory for database sessions
- get_db dependency for FastAPI dependency injection
- Database connection configuration
- Connection pooling settings

Example structure:
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker, Session
    from typing import Generator
    from app.core.config import settings
    
    engine = create_engine(
        settings.DATABASE_URL,
        pool_pre_ping=True,
        pool_size=5,
        max_overflow=10,
        echo=settings.DEBUG  # Log SQL queries in debug mode
    )
    
    SessionLocal = sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine
    )
    
    def get_db() -> Generator[Session, None, None]:
        '''Database session dependency for FastAPI routes.'''
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

engine = create_engine(settings.database_url, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
