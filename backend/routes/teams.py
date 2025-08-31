# AI Agentic Platform - Team Routes
"""
CRUD endpoints for managing AI agent teams.
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional
import uuid

from ..models import Team, User, get_db, engine
from ..utils.logging import logger
from ..routes.auth import get_current_active_user
from datetime import datetime

router = APIRouter()


@router.get("/", response_model=List[dict])
async def get_teams(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
) -> List[dict]:
    """Get all teams with pagination."""
    try:
        teams = db.query(Team).offset(skip).limit(limit).all()
        return [
            {
                "id": team.id,
                "name": team.name,
                "description": team.description,
                "members": team.members,
                "owner_id": team.owner_id,
                "orchestration_rules": team.orchestration_rules,
                "last_workflow_execution": team.last_workflow_execution,
                "workflow_status": team.workflow_status,
                "created_at": team.created_at,
                "updated_at": team.updated_at
            }
            for team in teams
        ]
    except Exception as e:
        logger.error(f"Error fetching teams: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while fetching teams"
        )

@router.post("/", response_model=dict)
async def create_team(
    name: str,
    description: str = None,
    orchestration_rules: dict = None,
    last_workflow_execution: Optional[datetime] = None,
    workflow_status: Optional[str] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
) -> dict:
    """Create a new team."""
    try:
        new_team = Team(
            name=name,
            description=description,
            members=[],
            owner_id=current_user.id,
            orchestration_rules=orchestration_rules or {},
            last_workflow_execution=last_workflow_execution,
            workflow_status=workflow_status
        )
        
        db.add(new_team)
        db.commit()
        db.refresh(new_team)
        
        logger.info(f"New team created: {new_team.name}")
        
        return {
            "id": new_team.id,
            "name": new_team.name,
            "description": new_team.description,
            "members": new_team.members,
            "owner_id": new_team.owner_id,
            "orchestration_rules": new_team.orchestration_rules,
            "last_workflow_execution": new_team.last_workflow_execution,
            "workflow_status": new_team.workflow_status,
            "created_at": new_team.created_at,
            "updated_at": new_team.updated_at
        }
    except Exception as e:
        logger.error(f"Error creating team: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while creating team"
        )

@router.get("/{team_id}", response_model=dict)
async def get_team(team_id: str, db: Session = Depends(get_db)) -> dict:
    """Get a specific team by ID."""
    try:
        team = db.query(Team).filter(Team.id == uuid.UUID(team_id)).first()
        if not team:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Team not found"
            )
        
        return {
            "id": team.id,
            "name": team.name,
            "description": team.description,
            "members": team.members,
            "owner_id": team.owner_id,
            "orchestration_rules": team.orchestration_rules,
            "last_workflow_execution": team.last_workflow_execution,
            "workflow_status": team.workflow_status,
            "created_at": team.created_at,
            "updated_at": team.updated_at
        }
    except Exception as e:
        logger.error(f"Error fetching team {team_id}: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while fetching team"
        )

@router.put("/{team_id}", response_model=dict)
async def update_team(
    team_id: str,
    name: str = None,
    description: str = None,
    orchestration_rules: dict = None,
    last_workflow_execution: Optional[datetime] = None,
    workflow_status: Optional[str] = None,
    db: Session = Depends(get_db)
) -> dict:
    """Update an existing team."""
    try:
        team = db.query(Team).filter(Team.id == uuid.UUID(team_id)).first()
        if not team:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Team not found"
            )
        
        # Update fields if provided
        if name is not None:
            team.name = name
        if description is not None:
            team.description = description
        if orchestration_rules is not None:
            team.orchestration_rules = orchestration_rules
        if last_workflow_execution is not None:
            team.last_workflow_execution = last_workflow_execution
        if workflow_status is not None:
            team.workflow_status = workflow_status
                     
        team.updated_at = datetime.utcnow()
        
        db.commit()
        db.refresh(team)
        
        logger.info(f"Team updated: {team.name}")
        
        return {
            "id": team.id,
            "name": team.name,
            "description": team.description,
            "members": team.members,
            "owner_id": team.owner_id,
            "orchestration_rules": team.orchestration_rules,
            "last_workflow_execution": team.last_workflow_execution,
            "workflow_status": team.workflow_status,
            "created_at": team.created_at,
            "updated_at": team.updated_at
        }
    except Exception as e:
        logger.error(f"Error updating team {team_id}: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while updating team"
        )

@router.delete("/{team_id}")
async def delete_team(team_id: str, db: Session = Depends(get_db)) -> None:
    """Delete a team."""
    try:
        team = db.query(Team).filter(Team.id == uuid.UUID(team_id)).first()
        if not team:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Team not found"
            )
        
        db.delete(team)
        db.commit()
        
        logger.info(f"Team deleted: {team.name}")
        
    except Exception as e:
        logger.error(f"Error deleting team {team_id}: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while deleting team"
        )