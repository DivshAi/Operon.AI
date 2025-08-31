# AI Agentic Platform - Agent Routes
"""
CRUD endpoints for managing AI agents.
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
import uuid

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
import uuid

from ..models import Agent, User, get_db, engine
from ..utils.logging import logger
from ..routes.auth import get_current_user_from_token, get_current_active_user

router = APIRouter()


@router.get("/", response_model=List[dict])
async def get_agents(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
) -> List[dict]:
    """Get all agents with pagination."""
    try:
        agents = db.query(Agent).offset(skip).limit(limit).all()
        return [
            {
                "id": agent.id,
                "name": agent.name,
                "description": agent.description,
                "config": agent.config,
                "status": agent.status,
                "last_executed": agent.last_executed,
                "performance_metrics": agent.performance_metrics,
                "mcp_tools": agent.mcp_tools,
                "owner_id": agent.owner_id,
                "created_at": agent.created_at,
                "updated_at": agent.updated_at
            }
            for agent in agents
        ]
    except Exception as e:
        logger.error(f"Error fetching agents: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while fetching agents"
        )

@router.post("/", response_model=dict)
async def create_agent(
    name: str,
    description: str = None,
    config: dict = None,
    mcp_tools: List[str] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
) -> dict:
    """Create a new agent."""
    try:
        new_agent = Agent(
            name=name,
            description=description,
            config=config or {},
            status="inactive",  # Default status for new agents
            last_executed=None,
            performance_metrics={},
            mcp_tools=mcp_tools or [],
            owner_id=current_user.id
        )
        
        db.add(new_agent)
        db.commit()
        db.refresh(new_agent)
        
        logger.info(f"New agent created: {new_agent.name}")
        
        return {
            "id": new_agent.id,
            "name": new_agent.name,
            "description": new_agent.description,
            "config": new_agent.config,
            "status": new_agent.status,
            "last_executed": new_agent.last_executed,
            "performance_metrics": new_agent.performance_metrics,
            "owner_id": new_agent.owner_id,
            "created_at": new_agent.created_at,
            "updated_at": new_agent.updated_at
        }
    except Exception as e:
        logger.error(f"Error creating agent: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while creating agent"
        )

@router.get("/{agent_id}", response_model=dict)
async def get_agent(agent_id: str, db: Session = Depends(get_db)) -> dict:
    """Get a specific agent by ID."""
    try:
        agent = db.query(Agent).filter(Agent.id == uuid.UUID(agent_id)).first()
        if not agent:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Agent not found"
            )
        
        return {
            "id": agent.id,
            "name": agent.name,
            "description": agent.description,
            "config": agent.config,
            "status": agent.status,
            "last_executed": agent.last_executed,
            "performance_metrics": agent.performance_metrics,
            "mcp_tools": agent.mcp_tools,
            "owner_id": agent.owner_id,
            "created_at": agent.created_at,
            "updated_at": agent.updated_at
        }
    except Exception as e:
        logger.error(f"Error fetching agent {agent_id}: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while fetching agent"
        )

@router.put("/{agent_id}", response_model=dict)
async def update_agent(
    agent_id: str,
    name: str = None,
    description: str = None,
    config: dict = None,
    status: str = None,
    last_executed: datetime = None,
    performance_metrics: dict = None,
    mcp_tools: List[str] = None,
    db: Session = Depends(get_db)
) -> dict:
    """Update an existing agent."""
    try:
        agent = db.query(Agent).filter(Agent.id == uuid.UUID(agent_id)).first()
        if not agent:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Agent not found"
            )
        
        # Update fields if provided
        if name is not None:
            agent.name = name
        if description is not None:
            agent.description = description
        if config is not None:
            agent.config = config
        if status is not None:
            agent.status = status
        if last_executed is not None:
            agent.last_executed = last_executed
        if performance_metrics is not None:
            agent.performance_metrics = performance_metrics
        if mcp_tools is not None:
            agent.mcp_tools = mcp_tools
            
        agent.updated_at = datetime.utcnow()
        
        db.commit()
        db.refresh(agent)
        
        logger.info(f"Agent updated: {agent.name}")
        
        return {
            "id": agent.id,
            "name": agent.name,
            "description": agent.description,
            "config": agent.config,
            "status": agent.status,
            "last_executed": agent.last_executed,
            "performance_metrics": agent.performance_metrics,
            "mcp_tools": agent.mcp_tools,
            "owner_id": agent.owner_id,
            "created_at": agent.created_at,
            "updated_at": agent.updated_at
        }
    except Exception as e:
        logger.error(f"Error updating agent {agent_id}: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while updating agent"
        )

@router.delete("/{agent_id}")
async def delete_agent(agent_id: str, db: Session = Depends(get_db)) -> None:
    """Delete an agent."""
    try:
        agent = db.query(Agent).filter(Agent.id == uuid.UUID(agent_id)).first()
        if not agent:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Agent not found"
            )
        
        db.delete(agent)
        db.commit()
        
        logger.info(f"Agent deleted: {agent.name}")
        
    except Exception as e:
        logger.error(f"Error deleting agent {agent_id}: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while deleting agent"
        )