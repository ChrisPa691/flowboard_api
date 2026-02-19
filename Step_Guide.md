# Flowboard API -- Step‑by‑Step Development Guide

> This guide defines exactly where to start and how to build your
> backend in the correct architectural order.

------------------------------------------------------------------------

# Phase 1 -- Make the API Boot (No Database Yet)

## Step 1: Application Entry

### Implement:

-   `app/main.py`
-   `app/api/v1/routes.py`

### Requirements:

-[x] Create FastAPI instance
-[x] Add `/healthz` endpoint
-[x] Include v1 router
-[x] Confirm `/docs` works

### Definition of Done:

-   `uvicorn app.main:app --reload` starts successfully

-   `GET /healthz` returns:

    ``` json
    {"status": "ok"}
    ```

-   Swagger UI loads at `/docs`

------------------------------------------------------------------------

# Phase 2 -- Configuration Layer

## Step 2: Centralized Settings

### Implement:

-   `app/core/config.py`

### Add environment variables:

-   DATABASE_URL
-   JWT_SECRET
-   JWT_ALGORITHM
-   ACCESS_TOKEN_EXPIRE_MIN
-   REFRESH_TOKEN_EXPIRE_DAYS
-   ENV

### Definition of Done:

-   App loads configuration cleanly
-   Missing required values raise clear errors

------------------------------------------------------------------------

# Phase 3 -- Database Infrastructure

## Step 3: Run PostgreSQL via Docker

### Update:

-   `docker-compose.yml`

### Include:

-   postgres service
-   volume for persistence
-   exposed port 5432

### Definition of Done:

-   `docker-compose up -d db` runs successfully
-   Database is reachable

------------------------------------------------------------------------

## Step 4: Database Session Setup

### Implement:

-   `app/db/session.py`
    -   SQLAlchemy engine
    -   SessionLocal
    -   get_db() dependency

### Definition of Done:

-   API starts without DB errors
-   DB connection established

------------------------------------------------------------------------

# Phase 4 -- First Real Model + Migrations

## Step 5: User Model

### Implement:

-   `app/models/user.py`
-   `app/db/base.py`

### Fields:

-   id (UUID or int primary key)
-   email (unique)
-   hashed_password
-   created_at

------------------------------------------------------------------------

## Step 6: Alembic Setup

### Steps:

-   Initialize Alembic

-   Configure DATABASE_URL

-   Create initial migration

-   Run:

        alembic upgrade head

### Definition of Done:

-   `users` table exists in PostgreSQL
-   Schema versioning works

------------------------------------------------------------------------

# Phase 5 -- Authentication System

## Step 7: Pydantic Schemas

### Implement:

-   `UserCreate`
-   `UserLogin`
-   `UserOut`
-   `Token`
-   `TokenPair`

### Rule:

-   Never return SQLAlchemy models directly

------------------------------------------------------------------------

## Step 8: Auth Service Logic

### Implement in `app/services/auth.py`:

-   hash_password()
-   verify_password()
-   create_access_token()
-   create_refresh_token()
-   decode_token()

### Definition of Done:

-   Password hashing + verification works
-   JWT tokens generated and decoded successfully

------------------------------------------------------------------------

## Step 9: Auth Routes

### Add endpoints:

-   POST `/auth/register`
-   POST `/auth/login`
-   POST `/auth/refresh`

### Add:

-   Protected test route

### Definition of Done:

-   User registers successfully
-   Login returns tokens
-   Protected route returns:
    -   401 without token
    -   200 with valid token

------------------------------------------------------------------------

# Phase 6 -- Testing

## Step 10: Expand Tests

### Add tests:

-   test_health.py
-   test_register.py
-   test_login.py
-   test_protected_route.py

### Definition of Done:

-   `pytest` runs successfully
-   All tests pass

------------------------------------------------------------------------

# Phase 7 -- Full Docker Integration

## Step 11: Finalize Docker

### Ensure:

-   API service defined
-   DB service defined
-   Environment variables wired
-   Proper ports exposed

### Definition of Done:

-   `docker-compose up --build` runs entire project
-   API accessible inside Docker

------------------------------------------------------------------------

# Phase 8 -- Flowboard Core Features

## Step 12: Board Entity

-   Model
-   Schemas
-   CRUD endpoints
-   Ownership validation

## Step 13: Column Entity

-   Relationship to Board
-   CRUD endpoints

## Step 14: Task Entity

-   Relationship to Column
-   Ordering field
-   Move-task logic

------------------------------------------------------------------------

# Phase 9 -- Advanced Improvements

## Step 15: Realtime

-   WebSockets
-   Authentication during connection
-   Broadcast task changes

## Step 16: Deployment

-   GitHub Actions CI
-   Linting
-   AWS deployment
-   Secure environment configuration

------------------------------------------------------------------------

# Architectural Rule (Never Break This)

    Route → Schema → Service → Model → Database

-   Routes contain no business logic
-   Services contain logic
-   Models define tables
-   Schemas validate I/O
-   Database layer handles persistence

------------------------------------------------------------------------

# Your First Work Session (Start Here)

1.  Implement `main.py` + `routes.py`
2.  Run server locally
3.  Verify `/healthz`
4.  Only then move to configuration

------------------------------------------------------------------------

This guide ensures your backend is built cleanly, professionally, and
portfolio-ready.
