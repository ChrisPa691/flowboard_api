"""API v1 routes and endpoints.

This file should include:
- FastAPI APIRouter instance
- All API endpoints organized by resource:
  * /health - Health check endpoint
  * /auth - Authentication endpoints (login, register, refresh)
  * /users - User management endpoints
  * /boards - Board CRUD endpoints
  * /columns - Column CRUD endpoints
  * /tasks - Task CRUD endpoints
- Request validation using Pydantic schemas
- Response models
- Dependency injection for authentication
- Proper HTTP status codes
- Error handling

Example structure:
    from fastapi import APIRouter, Depends, HTTPException, status
    from sqlalchemy.orm import Session
    from app.db.session import get_db
    from app.schemas.user import UserCreate, UserResponse
    from app.services.auth import get_current_user
    
    router = APIRouter()
    
    @router.get('/health')
    def health_check():
        return {'status': 'healthy', 'version': '1.0.0'}
    
    @router.post('/auth/register', response_model=UserResponse, status_code=status.HTTP_201_CREATED)
    async def register(user: UserCreate, db: Session = Depends(get_db)):
        # Implementation here
        pass
    
    @router.post('/auth/login')
    async def login(credentials: LoginRequest, db: Session = Depends(get_db)):
        # Implementation here
        pass
    
    @router.get('/users/me', response_model=UserResponse)
    async def get_current_user_info(
        current_user: User = Depends(get_current_user)
    ):
        return current_user
"""

from fastapi import APIRouter

router = APIRouter()

@router.get("/healthz", tags=["Health"])
def health_check():
    return {"status": "ok"}
