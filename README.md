# Flowboard API

FastAPI backend for the Flowboard Kanban application.

## Overview
This file should include:
- Project title and description
- Key features list
- Technology stack
- Prerequisites (Python version, PostgreSQL, etc.)
- Installation instructions
- Environment variables configuration
- Running the application (local and Docker)
- API documentation link (Swagger/ReDoc)
- Database migrations guide
- Testing instructions
- Project structure overview
- API endpoints documentation
- Authentication flow
- Deployment instructions
- Contributing guidelines
- License information
- Contact information

## Example Structure:

### Features
- JWT-based authentication with access and refresh tokens
- User registration and management
- Board, column, and task CRUD operations
- Real-time updates with WebSockets
- PostgreSQL database with SQLAlchemy ORM
- Alembic database migrations
- Docker containerization
- Comprehensive API documentation
- Unit and integration tests

### Tech Stack
- **Framework:** FastAPI
- **Database:** PostgreSQL + SQLAlchemy
- **Authentication:** JWT (python-jose + passlib)
- **Server:** Uvicorn
- **Testing:** Pytest
- **Containerization:** Docker & Docker Compose

### Installation
```powershell
# Clone repository
git clone <repository-url>
cd flowboard-api

# Create virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Setup environment variables
cp .env.example .env
# Edit .env with your configuration

# Run migrations
alembic upgrade head

# Start development server
uvicorn app.main:app --reload
```

### API Documentation
Once running, visit:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

### Docker Setup
```powershell
docker-compose up --build
```
app/
├── api/
│   └── v1/
├── core/
├── db/
├── models/
├── schemas/
├── services/
└── tests/
```

---

## ☁️ Deployment
- Docker image → AWS ECR  
- Deploy to ECS Fargate or EC2  
- Database → AWS RDS (PostgreSQL)  
- File storage → AWS S3  

---

## ✅ Roadmap
- [ ] Add OAuth (Google Login)
- [ ] Add rate limiting
- [ ] Improve unit tests coverage to 90%
