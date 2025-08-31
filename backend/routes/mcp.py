# AI Agentic Platform - MCP Routes
"""
API endpoints for managing Model Context Protocol (MCP) connections and tools.
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import uuid
from typing import List

from ..models import User, get_db, engine
from ..services.mcp_service import mcp_service, MCPConnection, MCPTool
from ..utils.logging import logger
from ..routes.auth import get_current_active_user

router = APIRouter()


@router.get("/connections", response_model=List[dict])
async def get_mcp_connections(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
) -> List[dict]:
    """Get all MCP connections."""
    try:
        connections = await mcp_service.list_connections()
        return connections
    except Exception as e:
        logger.error(f"Error fetching MCP connections: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while fetching MCP connections"
        )

@router.post("/connections", response_model=dict)
async def create_mcp_connection(
    name: str,
    server_name: str,
    uri: str,
    type: str,  # 'stdio' or 'http'
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
) -> dict:
    """Create a new MCP connection."""
    try:
        connection = MCPConnection(
            name=name,
            server_name=server_name,
            uri=uri,
            type=type
        )
        
        success = mcp_service.add_connection(connection)
        if not success:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to add MCP connection"
            )
        
        logger.info(f"New MCP connection created: {name} by user: {current_user.email}")
        
        return {
            "name": name,
            "server_name": server_name,
            "uri": uri,
            "type": type,
            "is_connected": False
        }
    except Exception as e:
        logger.error(f"Error creating MCP connection: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while creating MCP connection"
        )

@router.get("/connections/{connection_name}", response_model=dict)
async def get_mcp_connection(
    connection_name: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
) -> dict:
    """Get a specific MCP connection."""
    try:
        connections = await mcp_service.list_connections()
        connection = next((conn for conn in connections if conn["name"] == connection_name), None)
        
        if not connection:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="MCP connection not found"
            )
        
        return connection
    except Exception as e:
        logger.error(f"Error fetching MCP connection {connection_name}: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while fetching MCP connection"
        )

@router.post("/connections/{connection_name}/connect", response_model=dict)
async def connect_to_mcp_server(
    connection_name: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
) -> dict:
    """Connect to an MCP server."""
    try:
        success = await mcp_service.connect_to_server(connection_name)
        if not success:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to connect to MCP server"
            )
        
        logger.info(f"Connected to MCP server: {connection_name} by user: {current_user.email}")
        
        return {
            "message": f"Successfully connected to MCP server {connection_name}",
            "connection_name": connection_name
        }
    except Exception as e:
        logger.error(f"Error connecting to MCP server {connection_name}: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while connecting to MCP server"
        )

@router.get("/tools", response_model=List[dict])
async def get_mcp_tools(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
) -> List[dict]:
    """Get all available MCP tools."""
    try:
        tools = await mcp_service.list_available_tools()
        return tools
    except Exception as e:
        logger.error(f"Error fetching MCP tools: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while fetching MCP tools"
        )

@router.post("/tools", response_model=dict)
async def create_mcp_tool(
    name: str,
    description: str,
    input_schema: dict,
    server_name: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
) -> dict:
    """Create a new MCP tool."""
    try:
        # In a real implementation, this would store the tool definition
        # For now, we'll just return a success response
        
        logger.info(f"New MCP tool created: {name} by user: {current_user.email}")
        
        return {
            "name": name,
            "description": description,
            "input_schema": input_schema,
            "server_name": server_name
        }
    except Exception as e:
        logger.error(f"Error creating MCP tool: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while creating MCP tool"
        )

@router.delete("/connections/{connection_name}")
async def delete_mcp_connection(
    connection_name: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
) -> None:
    """Delete an MCP connection."""
    try:
        success = mcp_service.remove_connection(connection_name)
        if not success:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="MCP connection not found"
            )
        
        logger.info(f"MCP connection deleted: {connection_name} by user: {current_user.email}")
        
    except Exception as e:
        logger.error(f"Error deleting MCP connection {connection_name}: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while deleting MCP connection"
        )