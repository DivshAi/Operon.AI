# AI Agentic Platform - Prompt Store Tests
"""
Unit tests for prompt store service.
"""

import pytest

# Import our prompt store
from ..services.prompt_store import PromptStoreService

def test_prompt_store_initialization():
    """Test prompt store service initialization."""
    prompt_store = PromptStoreService()
    
    # Test that the prompt store was created successfully
    assert prompt_store is not None

def test_create_and_get_prompt():
    """Test creating and retrieving a prompt."""
    prompt_store = PromptStoreService()
    
    # Create a prompt
    prompt_data = prompt_store.create_prompt(
        body="This is a test prompt",
        version="1.0",
        tags=["test", "example"]
    )
    
    assert prompt_data["body"] == "This is a test prompt"
    assert prompt_data["version"] == "1.0"
    assert prompt_data["tags"] == ["test", "example"]
    
    # Retrieve the prompt
    retrieved_prompt = prompt_store.get_prompt(prompt_data["id"])
    assert retrieved_prompt is not None
    assert retrieved_prompt["body"] == "This is a test prompt"

def test_update_prompt():
    """Test updating a prompt."""
    prompt_store = PromptStoreService()
    
    # Create a prompt
    prompt_data = prompt_store.create_prompt(
        body="Original prompt",
        version="1.0",
        tags=["original"]
    )
    
    # Update the prompt
    updated_prompt = prompt_store.update_prompt(
        prompt_id=prompt_data["id"],
        body="Updated prompt",
        version="1.1",
        tags=["updated", "test"]
    )
    
    assert updated_prompt["body"] == "Updated prompt"
    assert updated_prompt["version"] == "1.1"
    assert updated_prompt["tags"] == ["updated", "test"]

if __name__ == "__main__":
    pytest.main([__file__, "-v"])