"""SQLAlchemy declarative base and model imports.

This file should include:
- SQLAlchemy declarative_base instance
- Import all models to ensure they're registered with Base.metadata
- This is used by Alembic for migrations

Example structure:
    from sqlalchemy.ext.declarative import declarative_base
    
    Base = declarative_base()
    
    # Import all models here for Alembic to detect them
    from app.models.user import User  # noqa: F401
    from app.models.board import Board  # noqa: F401
    from app.models.column import Column  # noqa: F401
    from app.models.task import Task  # noqa: F401
"""

from sqlalchemy.orm import declarative_base

Base = declarative_base()
