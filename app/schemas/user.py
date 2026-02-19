"""User Pydantic schemas for request/response validation.

This file should include:
- UserBase: Base schema with common fields
- UserCreate: Schema for user registration (email, username, password)
- UserUpdate: Schema for updating user data (all fields optional)
- UserResponse: Schema for API responses (excludes password)
- UserInDB: Schema with hashed_password (internal use)
- Email and password validation
- Config with from_attributes=True for ORM mode

Example structure:
    from pydantic import BaseModel, EmailStr, Field, ConfigDict, field_validator
    from datetime import datetime
    from typing import Optional
    
    class UserBase(BaseModel):
        email: EmailStr
        username: Optional[str] = Field(None, min_length=3, max_length=50)
    
    class UserCreate(UserBase):
        password: str = Field(min_length=8, max_length=100)
        
        @field_validator('password')
        def validate_password(cls, v):
            if not any(char.isdigit() for char in v):
                raise ValueError('Password must contain at least one digit')
            if not any(char.isupper() for char in v):
                raise ValueError('Password must contain at least one uppercase letter')
            return v
    
    class UserUpdate(BaseModel):
        email: Optional[EmailStr] = None
        username: Optional[str] = None
        password: Optional[str] = Field(None, min_length=8)
    
    class UserResponse(UserBase):
        id: int
        is_active: bool
        created_at: datetime
        
        model_config = ConfigDict(from_attributes=True)
    
    class UserInDB(UserResponse):
        hashed_password: str
"""

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: str


class UserOut(UserBase):
    id: int

    class Config:
        orm_mode = True
