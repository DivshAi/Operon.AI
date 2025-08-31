# AI Agentic Platform - Database Models
"""
SQLModel database schemas for the AI Agentic Platform.
"""

from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime
from uuid import UUID, uuid4

# Base class for all models
class BaseModel(SQLModel):
    id: Optional[UUID] = Field(default_factory=uuid4, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

# User Model
class User(BaseModel):
    email: str = Field(unique=True, index=True)
    hashed_password: str
    full_name: str
    user_persona: str  # Individual Developer, Enterprise Team, DevOps Engineer, Product Manager, Platform Admin, Customer Admin
    is_active: bool = True
    is_superuser: bool = False
    
    # Billing and subscription fields
    subscription_tier: Optional[str] = None
    subscription_expiry: Optional[datetime] = None
    
    # Usage analytics tracking fields
    usage_quota: Optional[int] = None
    usage_reset_date: Optional[datetime] = None
    last_accessed: Optional[datetime] = None
    
    # Relationship to agents, teams, and prompts (one-to-many)
    agents: List["Agent"] = Relationship(back_populates="owner")
    teams: List["Team"] = Relationship(back_populates="owner")
    prompts: List["Prompt"] = Relationship(back_populates="owner")

# Agent Model
class Agent(BaseModel):
    name: str
    description: Optional[str] = None
    config: dict  # JSON configuration for the agent
    status: str  # Tracks the agent's current status (active, inactive, error, etc.)
    last_executed: Optional[datetime] = None  # Tracks when the agent was last executed
    performance_metrics: dict = Field(default={}, sa_column_kwargs={"type_": "json"})  # Stores key performance metrics for the agent
    
    # MCP tool configuration
    mcp_tools: List[str] = Field(default=[], sa_column_kwargs={"type_": "json"})  # JSON array of MCP tool names
    
    # Foreign key to User (owner)
    owner_id: UUID = Field(foreign_key="user.id")
    
    # Relationship to user
    owner: User = Relationship(back_populates="agents")

# Team Model
class Team(BaseModel):
    name: str
    description: Optional[str] = None
    members: List[UUID] = Field(default=[], sa_column_kwargs={"type_": "json"})  # JSON array of agent IDs
    orchestration_rules: dict = Field(default={}, sa_column_kwargs={"type_": "json"})  # JSON rules for agent coordination
    last_workflow_execution: Optional[datetime] = None  # Tracks when the team's workflow was last executed
    workflow_status: Optional[str] = None  # Tracks the current status of the team's workflow execution
    
    # Foreign key to User (owner)
    owner_id: UUID = Field(foreign_key="user.id")
    
    # Relationship to user
    owner: User = Relationship(back_populates="teams")

# Prompt Model
class Prompt(BaseModel):
    body: str
    version: str
    tags: List[str] = Field(default=[], sa_column_kwargs={"type_": "json"})  # JSON array of tags
    
    # Foreign key to User (owner)
    owner_id: UUID = Field(foreign_key="user.id")
    
    # Audit log for tracking changes
    audit_log: dict = Field(default={}, sa_column_kwargs={"type_": "json"})
    
    # Relationship to user
    owner: User = Relationship(back_populates="prompts")

# Database setup
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Get database URL from environment variable or use SQLite for development
DATABASE_URL = "sqlite:///./ai_agentic_platform.db"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()