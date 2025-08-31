# AI Agentic Platform - Prompt Routes
"""
CRUD endpoints for managing prompt templates with versioning.
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
import uuid
from datetime import datetime

from ..models import Prompt, User, get_db, engine
from ..utils.logging import logger
from ..routes.auth import get_current_active_user

router = APIRouter()


@router.get("/", response_model=List[dict])
async def get_prompts(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
) -> List[dict]:
    """Get all prompts with pagination."""
    try:
        prompts = db.query(Prompt).offset(skip).limit(limit).all()
        return [
            {
                "id": prompt.id,
                "body": prompt.body,
                "version": prompt.version,
                "tags": prompt.tags,
                "owner_id": prompt.owner_id,
                "created_at": prompt.created_at,
                "updated_at": prompt.updated_at
            }
            for prompt in prompts
        ]
    except Exception as e:
        logger.error(f"Error fetching prompts: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while fetching prompts"
        )

@router.post("/", response_model=dict)
async def create_prompt(
    body: str,
    version: str = "1.0",
    tags: List[str] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
) -> dict:
    """Create a new prompt."""
    try:
        new_prompt = Prompt(
            body=body,
            version=version,
            tags=tags or [],
            owner_id=current_user.id
        )
        
        db.add(new_prompt)
        db.commit()
        db.refresh(new_prompt)
        
        logger.info(f"New prompt created: {new_prompt.id}")
        
        return {
            "id": new_prompt.id,
            "body": new_prompt.body,
            "version": new_prompt.version,
            "tags": new_prompt.tags,
            "owner_id": new_prompt.owner_id,
            "created_at": new_prompt.created_at,
            "updated_at": new_prompt.updated_at
        }
    except Exception as e:
        logger.error(f"Error creating prompt: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while creating prompt"
        )

@router.get("/{prompt_id}", response_model=dict)
async def get_prompt(prompt_id: str, db: Session = Depends(get_db)) -> dict:
    """Get a specific prompt by ID."""
    try:
        prompt = db.query(Prompt).filter(Prompt.id == uuid.UUID(prompt_id)).first()
        if not prompt:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Prompt not found"
            )
        
        return {
            "id": prompt.id,
            "body": prompt.body,
            "version": prompt.version,
            "tags": prompt.tags,
            "owner_id": prompt.owner_id,
            "created_at": prompt.created_at,
            "updated_at": prompt.updated_at
        }
    except Exception as e:
        logger.error(f"Error fetching prompt {prompt_id}: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while fetching prompt"
        )

@router.put("/{prompt_id}", response_model=dict)
async def update_prompt(
    prompt_id: str,
    body: str = None,
    version: str = None,
    tags: List[str] = None,
    db: Session = Depends(get_db)
) -> dict:
    """Update an existing prompt."""
    try:
        prompt = db.query(Prompt).filter(Prompt.id == uuid.UUID(prompt_id)).first()
        if not prompt:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Prompt not found"
            )
        
        # Update fields if provided
        if body is not None:
            prompt.body = body
        if version is not None:
            prompt.version = version
        if tags is not None:
            prompt.tags = tags
            
        prompt.updated_at = datetime.utcnow()
        
        db.commit()
        db.refresh(prompt)
        
        logger.info(f"Prompt updated: {prompt.id}")
        
        return {
            "id": prompt.id,
            "body": prompt.body,
            "version": prompt.version,
            "tags": prompt.tags,
            "owner_id": prompt.owner_id,
            "created_at": prompt.created_at,
            "updated_at": prompt.updated_at
        }
    except Exception as e:
        logger.error(f"Error updating prompt {prompt_id}: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while updating prompt"
        )

@router.delete("/{prompt_id}")
async def delete_prompt(prompt_id: str, db: Session = Depends(get_db)) -> None:
    """Delete a prompt."""
    try:
        prompt = db.query(Prompt).filter(Prompt.id == uuid.UUID(prompt_id)).first()
        if not prompt:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Prompt not found"
            )
        
        db.delete(prompt)
        db.commit()
        
        logger.info(f"Prompt deleted: {prompt.id}")
        
    except Exception as e:
        logger.error(f"Error deleting prompt {prompt_id}: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while deleting prompt"
        )

@router.get("/{prompt_id}/versions", response_model=List[dict])
async def get_prompt_versions(prompt_id: str, db: Session = Depends(get_db)) -> List[dict]:
    """Get all versions of a specific prompt."""
    try:
        # In a real implementation, this would query version history
        # For now, we'll return the prompt itself as it's the only version
        prompt = db.query(Prompt).filter(Prompt.id == uuid.UUID(prompt_id)).first()
        if not prompt:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Prompt not found"
            )
        
        # Return the current version (in a real implementation, this would be a history)
        return [
            {
                "version": prompt.version,
                "body": prompt.body,
                "created_at": prompt.created_at
            }
        ]
    except Exception as e:
        logger.error(f"Error fetching prompt versions {prompt_id}: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while fetching prompt versions"
        )