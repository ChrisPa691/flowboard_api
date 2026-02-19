"""Health check endpoint tests.

This file should include:
- Test for health endpoint availability
- Test for proper response format
- Test for response status code
- Test for response time (optional)
- Test database connectivity through health check (optional)

Example structure:
    import pytest
    from fastapi.testclient import TestClient
    from app.main import app
    
    client = TestClient(app)
    
    def test_health_check_returns_200():
        '''Test that health endpoint returns 200 OK'''
        response = client.get('/api/v1/health')
        assert response.status_code == 200
    
    def test_health_check_response_format():
        '''Test that health endpoint returns correct JSON format'''
        response = client.get('/api/v1/health')
        data = response.json()
        assert 'status' in data
        assert data['status'] in ['healthy', 'ok']
    
    def test_health_check_without_auth():
        '''Test that health endpoint doesn't require authentication'''
        response = client.get('/api/v1/health')
        assert response.status_code == 200
        # Should not return 401 Unauthorized
    
    def test_root_endpoint():
        '''Test root endpoint if it exists'''
        response = client.get('/')
        assert response.status_code in [200, 404]  # 404 if not implemented
"""

import pytest
from fastapi.testclient import TestClient
from app.main import app


def test_health_endpoint():
    client = TestClient(app)
    r = client.get("/healthz")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}
