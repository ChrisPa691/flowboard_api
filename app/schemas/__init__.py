"""Pydantic schemas package initialization.

This file should include:
- Exports of all Pydantic schemas
- Makes schemas easily importable

Example:
    from app.schemas.user import UserCreate, UserUpdate, UserResponse, UserInDB
    from app.schemas.board import BoardCreate, BoardUpdate, BoardResponse
    from app.schemas.column import ColumnCreate, ColumnUpdate, ColumnResponse
    from app.schemas.task import TaskCreate, TaskUpdate, TaskResponse
    from app.schemas.token import Token, TokenPayload, RefreshToken
    
    __all__ = [
        # User schemas
        'UserCreate', 'UserUpdate', 'UserResponse', 'UserInDB',
        # Board schemas
        'BoardCreate', 'BoardUpdate', 'BoardResponse',
        # Column schemas
        'ColumnCreate', 'ColumnUpdate', 'ColumnResponse',
        # Task schemas
        'TaskCreate', 'TaskUpdate', 'TaskResponse',
        # Token schemas
        'Token', 'TokenPayload', 'RefreshToken',
    ]
"""
