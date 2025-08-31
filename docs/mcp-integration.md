# AI Agentic Platform - MCP Integration

## Overview

The AI Agentic Platform now supports Model Context Protocol (MCP) integration, allowing AI agents to interact with external tools and services. This enables agents to perform actions beyond simple text generation by leveraging specialized tools available through MCP servers.

## What is MCP?

Model Context Protocol (MCP) is a protocol that allows LLMs to interact with external tools and services. It provides a standardized way for AI agents to discover, access, and execute tools from various sources.

## Features

- **Tool Discovery**: Agents can discover available tools from MCP servers
- **Tool Execution**: Execute tools with parameters through MCP connections
- **Connection Management**: Manage multiple MCP server connections
- **Agent Configuration**: Configure agents with specific MCP tools they should use
- **Integration with LLMs**: Seamless integration with local (Ollama) and cloud (OpenAI, Anthropic) LLMs

## Architecture

The MCP integration follows this architecture:

1. **MCP Service Layer** - Manages connections to MCP servers and tool execution
2. **Agent Configuration** - Agents can specify which MCP tools they should use
3. **Orchestrator Integration** - The orchestrator service can execute agents with MCP tools
4. **API Endpoints** - RESTful endpoints for managing MCP connections and tools

## API Endpoints

### MCP Connections

- `GET /mcp/connections` - List all MCP connections
- `POST /mcp/connections` - Create a new MCP connection
- `GET /mcp/connections/{connection_name}` - Get specific MCP connection details
- `POST /mcp/connections/{connection_name}/connect` - Connect to an MCP server
- `DELETE /mcp/connections/{connection_name}` - Delete an MCP connection

### MCP Tools

- `GET /mcp/tools` - List all available MCP tools
- `POST /mcp/tools` - Create a new MCP tool definition

## Agent Configuration

Agents can now be configured with MCP tools in their configuration:

```json
{
  "name": "Research Agent",
  "description": "Agent that researches topics using web search tools",
  "config": {
    "llm_type": "ollama",
    "model_name": "llama3"
  },
  "mcp_tools": [
    "web_search_tool",
    "data_analysis_tool"
  ]
}
```

## Usage Examples

### Creating an MCP Connection

```bash
curl -X POST "http://localhost:8000/mcp/connections" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "web-search-server",
    "server_name": "Web Search Server",
    "uri": "/path/to/web-search-server",
    "type": "stdio"
  }'
```

### Connecting to an MCP Server

```bash
curl -X POST "http://localhost:8000/mcp/connections/web-search-server/connect"
```

### Creating an Agent with MCP Tools

```bash
curl -X POST "http://localhost:8000/agents" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Research Agent",
    "description": "Agent that researches topics using web search tools",
    "config": {
      "llm_type": "ollama",
      "model_name": "llama3"
    },
    "mcp_tools": [
      "web_search_tool",
      "data_analysis_tool"
    ]
  }'
```

## Implementation Details

### MCP Service

The `MCPService` class in `backend/services/mcp_service.py` handles:

- Connection management to MCP servers
- Tool discovery and registration
- Tool execution with parameters
- Error handling for tool calls

### Integration with Orchestrator

The orchestrator service in `backend/services/orchestrator.py` now supports:

- Execution of agents configured with MCP tools
- Integration with local and cloud LLMs alongside MCP tools
- Proper error handling and logging for MCP operations

## Security Considerations

When using MCP integration, consider the following security aspects:

1. **Connection Security**: Ensure MCP server connections are secure (use HTTPS for HTTP connections)
2. **Tool Permissions**: Implement proper access controls for which tools agents can execute
3. **Input Validation**: Validate all inputs to MCP tools to prevent injection attacks
4. **Rate Limiting**: Implement rate limiting for tool execution to prevent abuse

## Future Enhancements

- Support for more MCP server types (HTTP, WebSocket)
- Advanced tool parameter validation and sanitization
- Tool execution monitoring and logging
- Integration with the platform's RBAC system for tool access control
- MCP tool marketplace for sharing and discovering tools