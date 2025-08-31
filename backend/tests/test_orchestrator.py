# AI Agentic Platform - Orchestrator Tests
"""
Unit tests for orchestrator service.
"""

import pytest
from unittest.mock import Mock, patch

# Import our orchestrator
from ..services.orchestrator import OrchestratorService

def test_orchestrator_initialization():
    """Test orchestrator service initialization."""
    orchestrator = OrchestratorService()
    
    # Test that the orchestrator was created successfully
    assert orchestrator is not None

def test_load_prompt_by_version():
    """Test loading a prompt by version."""
    orchestrator = OrchestratorService()
    
    # Test with default parameters
    result = orchestrator.load_prompt_by_version("test_prompt_id")
    assert "id" in result
    assert "version" in result
    assert "body" in result

def test_fetch_prompts_by_tags():
    """Test fetching prompts by tags."""
    orchestrator = OrchestratorService()
    
    # Test with default parameters
    result = orchestrator.fetch_prompts_by_tags(["test_tag"])
    assert isinstance(result, list)

if __name__ == "__main__":
    pytest.main([__file__, "-v"])