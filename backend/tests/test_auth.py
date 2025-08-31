# AI Agentic Platform - Authentication Tests
"""
Unit tests for authentication endpoints.
"""

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

# Import our application
from ..main import app
from ..models import get_db

client = TestClient(app)

def test_register_user():
    """Test user registration endpoint."""
    response = client.post(
        "/auth/register",
        json={
            "email": "test@example.com",
            "password": "password123",
            "full_name": "Test User",
            "user_persona": "Individual Developer"
        }
    )
    
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "test@example.com"
    assert data["full_name"] == "Test User"

def test_login_user():
    """Test user login endpoint."""
    # First register a user
    client.post(
        "/auth/register",
        json={
            "email": "login_test@example.com",
            "password": "password123",
            "full_name": "Login Test User",
            "user_persona": "Individual Developer"
        }
    )
    
    # Then login
    response = client.post(
        "/auth/login",
        data={
            "username": "login_test@example.com",
            "password": "password123"
        }
    )
    
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

if __name__ == "__main__":
    pytest.main([__file__, "-v"])