# AI Agentic Platform - Main Application
"""
Main FastAPI application with JWT middleware and role-based access controls.
"""

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from typing import Optional
import os
import uvicorn

# Import authentication utilities
from .routes.auth import get_current_user_from_token

# Import database models
from .models import Base, engine, get_db
from .routes import auth, agents, teams, prompts, mcp

# Create database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(
    title="AI Agentic Platform API",
    description="API for creating, configuring, and managing AI agents with orchestration capabilities",
    version="1.0.0"
)

# Include routers
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(agents.router, prefix="/agents", tags=["Agents"])
app.include_router(teams.router, prefix="/teams", tags=["Teams"])
app.include_router(prompts.router, prefix="/prompts", tags=["Prompts"])
app.include_router(mcp.router, prefix="/mcp", tags=["MCP"])

# Health check endpoint
@app.get("/")
async def root():
    return {"message": "AI Agentic Platform API is running"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

# OAuth2 scheme for JWT token authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

# Dependency to get current user from JWT token
async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    return get_current_user_from_token(token, db)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)