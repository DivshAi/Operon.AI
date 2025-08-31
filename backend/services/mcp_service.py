# AI Agentic Platform - MCP Service
"""
Service for managing Model Context Protocol (MCP) connections and tool execution.
"""

from typing import Dict, List, Any, Optional
import asyncio
import logging
from dataclasses import dataclass
from pydantic import BaseModel

try:
    # Try to import MCP libraries
    from mcp import Client, StdioClient, Server
    from mcp.types import ToolCall, ToolResult, TextContent, ImageContent
    HAS_MCP = True
except ImportError:
    HAS_MCP = False
    logging.warning("MCP libraries not available. MCP functionality will be limited.")

from ..utils.logging import logger

class MCPTool(BaseModel):
    """Data model for MCP tools."""
    name: str
    description: str
    input_schema: Dict[str, Any]
    server_name: str

class MCPConnection(BaseModel):
    """Data model for MCP server connections."""
    name: str
    server_name: str
    uri: str
    type: str  # 'stdio' or 'http'
    is_connected: bool = False

class MCPService:
    """Service for managing MCP connections and tool execution."""
    
    def __init__(self):
        """Initialize the MCP service."""
        self.connections: Dict[str, MCPConnection] = {}
        self.clients: Dict[str, Any] = {}
        self.tools: Dict[str, MCPTool] = {}
        
        if not HAS_MCP:
            logger.warning("MCP libraries not available. Some functionality will be disabled.")
    
    def add_connection(self, connection: MCPConnection) -> bool:
        """Add a new MCP server connection."""
        try:
            if not HAS_MCP:
                return False
                
            self.connections[connection.name] = connection
            logger.info(f"Added MCP connection: {connection.name}")
            return True
        except Exception as e:
            logger.error(f"Error adding MCP connection {connection.name}: {str(e)}")
            return False
    
    def remove_connection(self, connection_name: str) -> bool:
        """Remove an MCP server connection."""
        try:
            if connection_name in self.connections:
                del self.connections[connection_name]
                if connection_name in self.clients:
                    del self.clients[connection_name]
                logger.info(f"Removed MCP connection: {connection_name}")
                return True
            return False
        except Exception as e:
            logger.error(f"Error removing MCP connection {connection_name}: {str(e)}")
            return False
    
    async def connect_to_server(self, connection_name: str) -> bool:
        """Connect to an MCP server."""
        try:
            if not HAS_MCP:
                return False
                
            if connection_name not in self.connections:
                logger.error(f"MCP connection {connection_name} not found")
                return False
            
            connection = self.connections[connection_name]
            
            # Create client based on connection type
            if connection.type == "stdio":
                # For stdio connections, we assume the server is already running
                client = StdioClient(connection.uri)
            elif connection.type == "http":
                # For HTTP connections, we would use a different approach
                logger.warning("HTTP MCP connections not fully implemented yet")
                return False
            else:
                logger.error(f"Unsupported MCP connection type: {connection.type}")
                return False
            
            # Connect to the server
            await client.connect()
            
            # Store the client
            self.clients[connection_name] = client
            connection.is_connected = True
            
            # Fetch available tools from the server
            await self._fetch_tools_from_server(connection_name)
            
            logger.info(f"Connected to MCP server: {connection_name}")
            return True
            
        except Exception as e:
            logger.error(f"Error connecting to MCP server {connection_name}: {str(e)}")
            return False
    
    async def _fetch_tools_from_server(self, connection_name: str) -> None:
        """Fetch available tools from an MCP server."""
        try:
            if not HAS_MCP or connection_name not in self.clients:
                return
                
            client = self.clients[connection_name]
            
            # This would typically call the server's tool discovery API
            # For now, we'll simulate this with a placeholder
            logger.info(f"Fetching tools from MCP server: {connection_name}")
            
        except Exception as e:
            logger.error(f"Error fetching tools from MCP server {connection_name}: {str(e)}")
    
    async def execute_tool(self, tool_name: str, arguments: Dict[str, Any], 
                          connection_name: str = None) -> Dict[str, Any]:
        """Execute a tool with given arguments."""
        try:
            if not HAS_MCP:
                return {"error": "MCP libraries not available"}
            
            # Find the tool
            tool = self.tools.get(tool_name)
            if not tool:
                return {"error": f"Tool {tool_name} not found"}
            
            # If no connection specified, use the first available one
            if connection_name is None:
                if not self.clients:
                    return {"error": "No MCP connections available"}
                connection_name = next(iter(self.clients))
            
            # Check if we have a client for this connection
            if connection_name not in self.clients:
                return {"error": f"No client found for connection {connection_name}"}
            
            client = self.clients[connection_name]
            
            # Execute the tool call
            # This is a simplified version - actual implementation would depend on MCP protocol
            result = {
                "tool_name": tool_name,
                "arguments": arguments,
                "result": f"Executed {tool_name} with args: {arguments}",
                "connection": connection_name
            }
            
            logger.info(f"Executed tool {tool_name} via connection {connection_name}")
            return result
            
        except Exception as e:
            logger.error(f"Error executing tool {tool_name}: {str(e)}")
            return {"error": str(e)}
    
    async def list_available_tools(self) -> List[Dict[str, Any]]:
        """List all available tools."""
        try:
            tools_list = []
            for name, tool in self.tools.items():
                tools_list.append({
                    "name": name,
                    "description": tool.description,
                    "server": tool.server_name
                })
            return tools_list
        except Exception as e:
            logger.error(f"Error listing tools: {str(e)}")
            return []
    
    async def list_connections(self) -> List[Dict[str, Any]]:
        """List all MCP connections."""
        try:
            connections_list = []
            for name, connection in self.connections.items():
                connections_list.append({
                    "name": name,
                    "server_name": connection.server_name,
                    "uri": connection.uri,
                    "type": connection.type,
                    "is_connected": connection.is_connected
                })
            return connections_list
        except Exception as e:
            logger.error(f"Error listing connections: {str(e)}")
            return []

# Global MCP service instance
mcp_service = MCPService()