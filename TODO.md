# TODO - Flowboard API

This file should include:
- Project roadmap and milestones
- Feature backlog
- Known bugs and issues
- Technical debt items
- Optimization opportunities
- Documentation tasks
- Testing coverage improvements

## Example Structure:

### Phase 1: Core Infrastructure
- [x] Set up project structure and dependencies
- [ ] Configure database connection and models
- [ ] Implement JWT authentication system
- [ ] Create user registration and login endpoints
- [ ] Set up database migrations with Alembic
- [x] Add health check endpoint
- [ ] Configure CORS and middleware

### Phase 2: Board Management
- [ ] Create Board model and schema
- [ ] Implement board CRUD endpoints
- [ ] Add board ownership and permissions
- [ ] Create Column model and endpoints
- [ ] Implement column ordering
- [ ] Add column CRUD operations

### Phase 3: Task Management
- [ ] Create Task model and schema
- [ ] Implement task CRUD endpoints
- [ ] Add task assignment to users
- [ ] Implement task ordering within columns
- [ ] Add task due dates and priorities
- [ ] Implement task search and filtering

### Phase 4: Advanced Features
- [ ] Real-time updates with WebSockets
- [ ] File attachments for tasks
- [ ] Comments on tasks
- [ ] Board sharing and collaboration
- [ ] User permissions and roles
- [ ] Activity logs and audit trail
- [ ] Email notifications
- [ ] Task labels and tags

### Phase 5: Testing & Quality
- [ ] Unit tests for services
- [ ] Integration tests for API endpoints
- [ ] Test authentication flows
- [ ] Test database operations
- [ ] Add test coverage reporting
- [ ] Performance testing
- [ ] Security testing

### Phase 6: DevOps & Deployment
- [ ] Set up CI/CD pipeline (GitHub Actions)
- [ ] Configure production environment
- [ ] AWS deployment setup (EC2, RDS, S3)
- [ ] Set up monitoring and logging
- [ ] Configure database backups
- [ ] SSL certificate setup
- [ ] Domain configuration
- [ ] Rate limiting implementation

### Technical Improvements
- [ ] Add Redis caching layer
- [ ] Implement background task processing with Celery
- [ ] Optimize database queries
- [ ] Add database indexing
- [ ] Implement API versioning
- [ ] Add request/response logging
- [ ] Improve error handling
- [ ] Add API rate limiting

### Documentation
- [ ] Complete API endpoint documentation
- [ ] Add architecture diagrams
- [ ] Write deployment guide
- [ ] Create contribution guidelines
- [ ] Add code examples and tutorials
- [ ] Document environment variables
- [ ] Create troubleshooting guide

### Bugs & Issues
- [ ] (Track bugs here as they are discovered)

### Completed ✓
- [x] Initial project structure created
- [x] Basic FastAPI setup
    -   [ ] ACCESS_TOKEN_EXPIRE_MIN
    -   [ ] REFRESH_TOKEN_EXPIRE_DAYS
-   [ ] Add `.env` file for local development
-   [ ] Ensure app fails clearly if required vars are missing

Definition of Done: - All configuration is centralized in config.py

------------------------------------------------------------------------

## Phase 2 -- Database Setup

### ☐ 3. Database Session

-   [ ] Create SQLAlchemy engine in `app/db/session.py`
-   [ ] Implement `SessionLocal`
-   [ ] Create `get_db()` dependency
-   [ ] Connect to PostgreSQL via Docker

Definition of Done: - App connects successfully to Postgres

------------------------------------------------------------------------

### ☐ 4. First Model + Migration

-   [ ] Create `User` model in `app/models/user.py`
    -   [ ] id (UUID or int primary key)
    -   [ ] email (unique)
    -   [ ] hashed_password
    -   [ ] created_at
-   [ ] Initialize Alembic
-   [ ] Create first migration
-   [ ] Run `alembic upgrade head`
-   [ ] Confirm `users` table exists in DB

Definition of Done: - Database schema is version controlled

------------------------------------------------------------------------

## Phase 3 -- Authentication System

### ☐ 5. Pydantic Schemas

-   [ ] Create `UserCreate`
-   [ ] Create `UserOut`
-   [ ] Create `Token`
-   [ ] Create `TokenPair`

Definition of Done: - No raw SQLAlchemy models returned in API responses

------------------------------------------------------------------------

### ☐ 6. Auth Service Layer

-   [ ] Implement password hashing (bcrypt)
-   [ ] Implement password verification
-   [ ] Implement access token generation
-   [ ] Implement refresh token generation
-   [ ] Implement token validation logic

Definition of Done: - Tokens can be generated and verified independently

------------------------------------------------------------------------

### ☐ 7. Auth Routes

-   [ ] POST `/auth/register`
-   [ ] POST `/auth/login`
-   [ ] POST `/auth/refresh`
-   [ ] Protect a sample route using JWT dependency

Definition of Done: - User can register and log in - Protected route
returns 401 without token

------------------------------------------------------------------------

## Phase 4 -- Testing

### ☐ 8. Testing Setup

-   [ ] Configure pytest
-   [ ] Write `test_health.py`
-   [ ] Write `test_register.py`
-   [ ] Write `test_login.py`
-   [ ] Write protected route test

Definition of Done: - All tests pass locally

------------------------------------------------------------------------

## Phase 5 -- Dockerization

### ☐ 9. Docker Setup

-   [ ] Complete Dockerfile
-   [ ] Complete docker-compose.yml
-   [ ] Add Postgres service
-   [ ] Add environment variable wiring
-   [ ] Verify `docker-compose up --build` works
-   [ ] Verify API reachable inside Docker

Definition of Done: - Entire project runs with one command

------------------------------------------------------------------------

## Phase 6 -- Core Flowboard Features

### ☐ 10. Board Entity

-   [ ] Create Board model
-   [ ] Create Board schemas
-   [ ] Implement CRUD endpoints
-   [ ] Add ownership validation

------------------------------------------------------------------------

### ☐ 11. Column Entity

-   [ ] Create Column model
-   [ ] Implement relationship to Board
-   [ ] Add CRUD endpoints

------------------------------------------------------------------------

### ☐ 12. Task Entity

-   [ ] Create Task model
-   [ ] Implement ordering field
-   [ ] Add CRUD endpoints
-   [ ] Add move-task logic

------------------------------------------------------------------------

## Phase 7 -- Advanced Features

### ☐ 13. Realtime Updates

-   [ ] Add WebSocket support
-   [ ] Broadcast task changes
-   [ ] Handle connection authentication

------------------------------------------------------------------------

### ☐ 14. Deployment

-   [ ] Add CI workflow (GitHub Actions)
-   [ ] Add linting
-   [ ] Deploy to AWS (EC2 or ECS)
-   [ ] Configure environment variables securely

------------------------------------------------------------------------

## Final Checklist

-   [ ] Clean README documentation
-   [ ] API documented via Swagger
-   [ ] No hardcoded secrets
-   [ ] Proper error handling
-   [ ] Logging configured
-   [ ] Code formatted with black
-   [ ] Project ready for portfolio

------------------------------------------------------------------------

### Progress Tracking Tip

Update this file regularly and commit changes as you complete sections:

    git add TODO.md
    git commit -m "Progress: Completed Phase X"
