"""Main application entry point for the Flowboard API.

This file should include:
- FastAPI application instance initialization
- Application metadata (title, description, version)
- CORS middleware configuration
- Include routers from api.v1
- Startup and shutdown event handlers
- Exception handlers
- Health check endpoint
- Root endpoint with API documentation

Example structure:
    from fastapi import FastAPI
    from fastapi.middleware.cors import CORSMiddleware
    from app.api.v1.routes import router as api_v1_router
    from app.core.config import settings
    
    app = FastAPI(
        title="Flowboard API",
        description="FastAPI backend for Kanban board application",
        version="1.0.0"
    )
    
    app.add_middleware(CORSMiddleware, ...)
    app.include_router(api_v1_router, prefix="/api/v1")
"""

from fastapi import FastAPI
from app.api.v1.routes import router as v1_router

app = FastAPI(
    title="Flowboard API",
    version="0.1.0",
    description="Kanban-style task management backend"
)

# Include v1 router with prefix
app.include_router(
    v1_router,
    prefix="/api/v1",
)

@app.get("/")
def root():
    return {"message": "Flowboard API running"}


