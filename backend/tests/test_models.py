# AI Agentic Platform - Backend Tests
"""
Unit tests for backend components.
"""

import pytest
from sqlmodel import create_engine, Session
from sqlalchemy import text
from datetime import datetime

# Import our models
from ..models import User, Agent, Team, Prompt, get_db

def test_database_connection():
    """Test that we can connect to the database."""
    # This test will pass if the database connection is properly configured
    engine = create_engine("sqlite:///./test.db")
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        assert result.fetchone() is not None

def test_user_model():
    """Test User model creation."""
    user = User(
        email="test@example.com",
        hashed_password="hashed_password",
        full_name="Test User",
        user_persona="Individual Developer"
    )
    
    assert user.email == "test@example.com"
    assert user.full_name == "Test User"
    assert user.user_persona == "Individual Developer"
    assert user.is_active is True

def test_agent_model():
    """Test Agent model creation."""
    agent = Agent(
        name="Test Agent",
        description="A test agent",
        config={"model": "gpt-3.5-turbo"},
        status="active",
        last_executed=datetime.utcnow(),
        performance_metrics={"response_time": 0.5, "success_rate": 0.95}
    )
    
    assert agent.name == "Test Agent"
    assert agent.description == "A test agent"
    assert agent.config == {"model": "gpt-3.5-turbo"}
    assert agent.status == "active"
    assert agent.last_executed is not None
    assert agent.performance_metrics == {"response_time": 0.5, "success_rate": 0.95}

def test_team_model():
    """Test Team model creation."""
    team = Team(
        name="Test Team",
        description="A test team",
        members=["agent_1", "agent_2"],
        orchestration_rules={"rule1": "value1", "rule2": "value2"},
        last_workflow_execution=datetime.utcnow(),
        workflow_status="running"
    )
    
    assert team.name == "Test Team"
    assert team.description == "A test team"
    assert team.members == ["agent_1", "agent_2"]
    assert team.orchestration_rules == {"rule1": "value1", "rule2": "value2"}
    assert team.last_workflow_execution is not None
    assert team.workflow_status == "running"

def test_prompt_model():
    """Test Prompt model creation."""
    prompt = Prompt(
        body="This is a test prompt",
        version="1.0",
        tags=["test", "example"]
    )
    
    assert prompt.body == "This is a test prompt"
    assert prompt.version == "1.0"
    assert prompt.tags == ["test", "example"]

if __name__ == "__main__":
    pytest.main([__file__, "-v"])