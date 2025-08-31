# AI Agentic Platform - Prompt Store Service
"""
Interfaces to store, tag, version, rollback prompts with backup capabilities.
"""

from typing import Dict, List, Any, Optional
from datetime import datetime
import json
import os

from ..models import Prompt
from ..utils.logging import logger

class PromptStoreService:
    """Service for managing prompt storage and versioning."""
    
    def __init__(self):
        """Initialize the prompt store service."""
        # In a real implementation, this would connect to a database or file system
        self.prompts = {}  # In-memory storage for demonstration
        self.version_history = {}  # Track version history
    
    def create_prompt(self, body: str, version: str = "1.0", tags: List[str] = None) -> Dict[str, Any]:
        """Create a new prompt with versioning."""
        try:
            prompt_id = f"prompt_{len(self.prompts) + 1}"
            
            prompt_data = {
                "id": prompt_id,
                "body": body,
                "version": version,
                "tags": tags or [],
                "created_at": datetime.utcnow().isoformat(),
                "updated_at": datetime.utcnow().isoformat(),
                "audit_log": [
                    {
                        "action": "create",
                        "timestamp": datetime.utcnow().isoformat(),
                        "version": version
                    }
                ]
            }
            
            self.prompts[prompt_id] = prompt_data
            
            # Initialize version history for this prompt
            self.version_history[prompt_id] = [prompt_data]
            
            logger.info(f"Created new prompt: {prompt_id}")
            return prompt_data
            
        except Exception as e:
            logger.error(f"Error creating prompt: {str(e)}")
            raise
    
    def get_prompt(self, prompt_id: str) -> Optional[Dict[str, Any]]:
        """Get a specific prompt by ID."""
        try:
            return self.prompts.get(prompt_id)
        except Exception as e:
            logger.error(f"Error fetching prompt {prompt_id}: {str(e)}")
            raise
    
    def update_prompt(self, prompt_id: str, body: str = None, version: str = None, tags: List[str] = None) -> Dict[str, Any]:
        """Update an existing prompt and create a new version."""
        try:
            if prompt_id not in self.prompts:
                raise ValueError(f"Prompt {prompt_id} not found")
            
            prompt_data = self.prompts[prompt_id]
            
            # Update fields if provided
            if body is not None:
                prompt_data["body"] = body
            if version is not None:
                prompt_data["version"] = version
            if tags is not None:
                prompt_data["tags"] = tags
                
            prompt_data["updated_at"] = datetime.utcnow().isoformat()
            
            # Add audit log entry
            audit_entry = {
                "action": "update",
                "timestamp": datetime.utcnow().isoformat(),
                "version": version or prompt_data["version"]
            }
            prompt_data["audit_log"].append(audit_entry)
            
            # Update version history
            self.version_history[prompt_id].append(prompt_data.copy())
            
            logger.info(f"Updated prompt: {prompt_id}")
            return prompt_data
            
        except Exception as e:
            logger.error(f"Error updating prompt {prompt_id}: {str(e)}")
            raise
    
    def delete_prompt(self, prompt_id: str) -> bool:
        """Delete a prompt."""
        try:
            if prompt_id in self.prompts:
                del self.prompts[prompt_id]
                if prompt_id in self.version_history:
                    del self.version_history[prompt_id]
                logger.info(f"Deleted prompt: {prompt_id}")
                return True
            return False
        except Exception as e:
            logger.error(f"Error deleting prompt {prompt_id}: {str(e)}")
            raise
    
    def get_prompt_versions(self, prompt_id: str) -> List[Dict[str, Any]]:
        """Get all versions of a specific prompt."""
        try:
            return self.version_history.get(prompt_id, [])
        except Exception as e:
            logger.error(f"Error fetching versions for prompt {prompt_id}: {str(e)}")
            raise
    
    def rollback_prompt(self, prompt_id: str, version: str) -> Dict[str, Any]:
        """Rollback a prompt to a specific version."""
        try:
            if prompt_id not in self.version_history:
                raise ValueError(f"Prompt {prompt_id} not found")
            
            # Find the version
            versions = self.version_history[prompt_id]
            target_version = next((v for v in versions if v["version"] == version), None)
            
            if not target_version:
                raise ValueError(f"Version {version} not found for prompt {prompt_id}")
            
            # Update current prompt to this version
            self.prompts[prompt_id] = target_version.copy()
            
            # Add audit log entry
            audit_entry = {
                "action": "rollback",
                "timestamp": datetime.utcnow().isoformat(),
                "version": version,
                "original_version": self.prompts[prompt_id]["version"]
            }
            self.prompts[prompt_id]["audit_log"].append(audit_entry)
            
            logger.info(f"Rolled back prompt {prompt_id} to version {version}")
            return self.prompts[prompt_id]
            
        except Exception as e:
            logger.error(f"Error rolling back prompt {prompt_id}: {str(e)}")
            raise
    
    def search_prompts(self, tags: List[str] = None, query: str = None) -> List[Dict[str, Any]]:
        """Search prompts by tags or text query."""
        try:
            results = []
            
            for prompt_data in self.prompts.values():
                # Check if tags match
                if tags:
                    if any(tag in prompt_data["tags"] for tag in tags):
                        results.append(prompt_data)
                # Check if query matches body or other fields
                elif query:
                    if query.lower() in prompt_data["body"].lower():
                        results.append(prompt_data)
                else:
                    results.append(prompt_data)
            
            return results
        except Exception as e:
            logger.error(f"Error searching prompts: {str(e)}")
            raise
    
    def backup_prompts(self, backup_path: str = None) -> bool:
        """Backup all prompts to a file."""
        try:
            if not backup_path:
                backup_path = f"prompts_backup_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.json"
            
            backup_data = {
                "prompts": self.prompts,
                "version_history": self.version_history,
                "backup_timestamp": datetime.utcnow().isoformat()
            }
            
            with open(backup_path, 'w') as f:
                json.dump(backup_data, f, indent=2)
            
            logger.info(f"Backed up prompts to {backup_path}")
            return True
            
        except Exception as e:
            logger.error(f"Error backing up prompts: {str(e)}")
            raise
    
    def restore_prompts(self, backup_path: str) -> bool:
        """Restore prompts from a backup file."""
        try:
            with open(backup_path, 'r') as f:
                backup_data = json.load(f)
            
            self.prompts = backup_data.get("prompts", {})
            self.version_history = backup_data.get("version_history", {})
            
            logger.info(f"Restored prompts from {backup_path}")
            return True
            
        except Exception as e:
            logger.error(f"Error restoring prompts: {str(e)}")
            raise

# Global prompt store instance
prompt_store = PromptStoreService()