"""API package initialization.

This file should include:
- API router aggregation from versioned routes
- API-wide dependencies
- Common API middleware
- Version management

Example:
    from fastapi import APIRouter
    from app.api.v1.routes import router as v1_router
    
    router = APIRouter()
    router.include_router(v1_router, prefix='/v1', tags=['v1'])
    
    __all__ = ['router']
"""
