"""User database model.

This file should include:
- SQLAlchemy User model with columns:
  * id (Integer, primary key)
  * email (String, unique, indexed)
  * username (String, unique, indexed, optional)
  * hashed_password (String)
  * is_active (Boolean, default=True)
  * is_superuser (Boolean, default=False)
  * created_at (DateTime)
  * updated_at (DateTime)
- Relationships to boards, tasks, etc.
- Table name definition
- Indexes for performance

Example structure:
    from sqlalchemy import Boolean, Column, Integer, String, DateTime
    from sqlalchemy.orm import relationship
    from sqlalchemy.sql import func
    from app.db.base import Base
    
    class User(Base):
        __tablename__ = 'users'
        
        id = Column(Integer, primary_key=True, index=True)
        email = Column(String(255), unique=True, index=True, nullable=False)
        username = Column(String(50), unique=True, index=True)
        hashed_password = Column(String(255), nullable=False)
        is_active = Column(Boolean, default=True, nullable=False)
        is_superuser = Column(Boolean, default=False, nullable=False)
        created_at = Column(DateTime(timezone=True), server_default=func.now())
        updated_at = Column(DateTime(timezone=True), onupdate=func.now())
        
        # Relationships
        boards = relationship('Board', back_populates='owner', cascade='all, delete-orphan')
        tasks = relationship('Task', back_populates='assignee')
        comments = relationship('Comment', back_populates='author')
"""

from sqlalchemy import Column, Integer, String
from app.db.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
