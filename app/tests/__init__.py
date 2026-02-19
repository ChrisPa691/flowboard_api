"""Test package initialization.

This file should include:
- Test fixtures setup
- Common test utilities
- Test database configuration
- Test client factory
- Fixtures for test users, boards, etc.

Example (or use conftest.py):
    import pytest
    from fastapi.testclient import TestClient
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from app.main import app
    from app.db.base import Base
    from app.db.session import get_db
    
    # Test database setup
    SQLALCHEMY_DATABASE_URL = 'sqlite:///./test.db'
    engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    
    @pytest.fixture
    def db():
        Base.metadata.create_all(bind=engine)
        db = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close()
            Base.metadata.drop_all(bind=engine)
    
    @pytest.fixture
    def client(db):
        def override_get_db():
            try:
                yield db
            finally:
                db.close()
        
        app.dependency_overrides[get_db] = override_get_db
        return TestClient(app)
"""
