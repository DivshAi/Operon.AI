# AI Agentic Platform - API Endpoints Specification

## Overview
This document specifies the RESTful API endpoints for the AI Agentic Platform. All endpoints return JSON responses and follow consistent naming conventions.

## Authentication Endpoints

### Register User
- **POST** `/auth/register`
- **Description**: Register a new user with email and password
- **Request Body**:
  ```json
  {
    "email": "string",
    "password": "string",
    "full_name": "string",
    "user_persona": "string"
  }
  ```
- **Response**:
  ```json
  {
    "id": "uuid",
    "email": "string",
    "full_name": "string",
    "user_persona": "string",
    "is_active": true,
    "created_at": "datetime"
  }
  ```

### Login User
- **POST** `/auth/login`
- **Description**: Authenticate user and return JWT token
- **Request Body**:
  ```json
  {
    "email": "string",
    "password": "string"
  }
  ```
- **Response**:
  ```json
  {
    "access_token": "string",
    "token_type": "bearer"
  }
  ```

## Agent Endpoints

### Get All Agents
- **GET** `/agents`
- **Description**: Retrieve list of all agents
- **Query Parameters**:
  - `skip` (optional): Number of records to skip
  - `limit` (optional): Maximum number of records to return
- **Response**:
  ```json
  [
    {
      "id": "uuid",
      "name": "string",
      "description": "string",
      "config": "object",
      "owner_id": "uuid",
      "created_at": "datetime",
      "updated_at": "datetime"
    }
  ]
  ```

### Create Agent
- **POST** `/agents`
- **Description**: Create a new agent
- **Request Body**:
  ```json
  {
    "name": "string",
    "description": "string",
    "config": "object"
  }
  ```
- **Response**:
  ```json
  {
    "id": "uuid",
    "name": "string",
    "description": "string",
    "config": "object",
    "owner_id": "uuid",
    "created_at": "datetime",
    "updated_at": "datetime"
  }
  ```

### Get Agent by ID
- **GET** `/agents/{id}`
- **Description**: Retrieve specific agent details
- **Response**:
  ```json
  {
    "id": "uuid",
    "name": "string",
    "description": "string",
    "config": "object",
    "owner_id": "uuid",
    "created_at": "datetime",
    "updated_at": "datetime"
  }
  ```

### Update Agent
- **PUT** `/agents/{id}`
- **Description**: Update an existing agent
- **Request Body**:
  ```json
  {
    "name": "string",
    "description": "string",
    "config": "object"
  }
  ```
- **Response**:
  ```json
  {
    "id": "uuid",
    "name": "string",
    "description": "string",
    "config": "object",
    "owner_id": "uuid",
    "created_at": "datetime",
    "updated_at": "datetime"
  }
  ```

### Delete Agent
- **DELETE** `/agents/{id}`
- **Description**: Delete an agent
- **Response**: HTTP 204 No Content

## Team Endpoints

### Get All Teams
- **GET** `/teams`
- **Description**: Retrieve list of all teams
- **Query Parameters**:
  - `skip` (optional): Number of records to skip
  - `limit` (optional): Maximum number of records to return
- **Response**:
  ```json
  [
    {
      "id": "uuid",
      "name": "string",
      "description": "string",
      "members": ["uuid"],
      "owner_id": "uuid",
      "created_at": "datetime",
      "updated_at": "datetime"
    }
  ]
  ```

### Create Team
- **POST** `/teams`
- **Description**: Create a new team
- **Request Body**:
  ```json
  {
    "name": "string",
    "description": "string"
  }
  ```
- **Response**:
  ```json
  {
    "id": "uuid",
    "name": "string",
    "description": "string",
    "members": ["uuid"],
    "owner_id": "uuid",
    "created_at": "datetime",
    "updated_at": "datetime"
  }
  ```

### Get Team by ID
- **GET** `/teams/{id}`
- **Description**: Retrieve specific team details
- **Response**:
  ```json
  {
    "id": "uuid",
    "name": "string",
    "description": "string",
    "members": ["uuid"],
    "owner_id": "uuid",
    "created_at": "datetime",
    "updated_at": "datetime"
  }
  ```

### Update Team
- **PUT** `/teams/{id}`
- **Description**: Update an existing team
- **Request Body**:
  ```json
  {
    "name": "string",
    "description": "string"
  }
  ```
- **Response**:
  ```json
  {
    "id": "uuid",
    "name": "string",
    "description": "string",
    "members": ["uuid"],
    "owner_id": "uuid",
    "created_at": "datetime",
    "updated_at": "datetime"
  }
  ```

### Delete Team
- **DELETE** `/teams/{id}`
- **Description**: Delete a team
- **Response**: HTTP 204 No Content

## Prompt Endpoints

### Get All Prompts
- **GET** `/prompts`
- **Description**: Retrieve list of all prompts
- **Query Parameters**:
  - `skip` (optional): Number of records to skip
  - `limit` (optional): Maximum number of records to return
- **Response**:
  ```json
  [
    {
      "id": "uuid",
      "body": "string",
      "version": "string",
      "tags": ["string"],
      "owner_id": "uuid",
      "created_at": "datetime",
      "updated_at": "datetime"
    }
  ]
  ```

### Create Prompt
- **POST** `/prompts`
- **Description**: Create a new prompt
- **Request Body**:
  ```json
  {
    "body": "string",
    "version": "string",
    "tags": ["string"]
  }
  ```
- **Response**:
  ```json
  {
    "id": "uuid",
    "body": "string",
    "version": "string",
    "tags": ["string"],
    "owner_id": "uuid",
    "created_at": "datetime",
    "updated_at": "datetime"
  }
  ```

### Get Prompt by ID
- **GET** `/prompts/{id}`
- **Description**: Retrieve specific prompt details
- **Response**:
  ```json
  {
    "id": "uuid",
    "body": "string",
    "version": "string",
    "tags": ["string"],
    "owner_id": "uuid",
    "created_at": "datetime",
    "updated_at": "datetime"
  }
  ```

### Update Prompt
- **PUT** `/prompts/{id}`
- **Description**: Update an existing prompt
- **Request Body**:
  ```json
  {
    "body": "string",
    "version": "string",
    "tags": ["string"]
  }
  ```
- **Response**:
  ```json
  {
    "id": "uuid",
    "body": "string",
    "version": "string",
    "tags": ["string"],
    "owner_id": "uuid",
    "created_at": "datetime",
    "updated_at": "datetime"
  }
  ```

### Delete Prompt
- **DELETE** `/prompts/{id}`
- **Description**: Delete a prompt
- **Response**: HTTP 204 No Content

### Get Prompt Versions
- **GET** `/prompts/{id}/versions`
- **Description**: Retrieve all versions of a specific prompt
- **Response**:
  ```json
  [
    {
      "version": "string",
      "body": "string",
      "created_at": "datetime"
    }
  ]
  ```

## MCP Endpoints

### Get All MCP Connections
- **GET** `/mcp/connections`
- **Description**: Retrieve list of all MCP connections
- **Response**:
  ```json
  [
    {
      "name": "string",
      "server_name": "string",
      "uri": "string",
      "type": "string",
      "is_connected": true
    }
  ]
  ```

### Create MCP Connection
- **POST** `/mcp/connections`
- **Description**: Create a new MCP connection
- **Request Body**:
  ```json
  {
    "name": "string",
    "server_name": "string",
    "uri": "string",
    "type": "string"
  }
  ```
- **Response**:
  ```json
  {
    "name": "string",
    "server_name": "string",
    "uri": "string",
    "type": "string",
    "is_connected": false
  }
  ```

### Get MCP Connection by Name
- **GET** `/mcp/connections/{connection_name}`
- **Description**: Retrieve specific MCP connection details
- **Response**:
  ```json
  {
    "name": "string",
    "server_name": "string",
    "uri": "string",
    "type": "string",
    "is_connected": true
  }
  ```

### Connect to MCP Server
- **POST** `/mcp/connections/{connection_name}/connect`
- **Description**: Connect to an MCP server
- **Response**:
  ```json
  {
    "message": "string",
    "connection_name": "string"
  }
  ```

### Get All MCP Tools
- **GET** `/mcp/tools`
- **Description**: Retrieve list of all available MCP tools
- **Response**:
  ```json
  [
    {
      "name": "string",
      "description": "string",
      "server": "string"
    }
  ]
  ```

### Create MCP Tool
- **POST** `/mcp/tools`
- **Description**: Create a new MCP tool definition
- **Request Body**:
  ```json
  {
    "name": "string",
    "description": "string",
    "input_schema": "object",
    "server_name": "string"
  }
  ```
- **Response**:
  ```json
  {
    "name": "string",
    "description": "string",
    "input_schema": "object",
    "server_name": "string"
  }
  ```

### Delete MCP Connection
- **DELETE** `/mcp/connections/{connection_name}`
- **Description**: Delete an MCP connection
- **Response**: HTTP 204 No Content

## Error Handling

All API endpoints follow consistent error response format:
```json
{
  "error": {
    "code": "string",
    "message": "string",
    "details": "object"
  }
}
```

### Common HTTP Status Codes
- `200 OK` - Successful GET, PUT, PATCH requests
- `201 Created` - Successful POST requests
- `204 No Content` - Successful DELETE requests
- `400 Bad Request` - Invalid request data
- `401 Unauthorized` - Authentication required
- `403 Forbidden` - Insufficient permissions
- `404 Not Found` - Resource not found
- `500 Internal Server Error` - Server error

## Authentication
All endpoints except `/auth/register` and `/auth/login` require a valid JWT token in the Authorization header:
```
Authorization: Bearer <access_token>
```

## Rate Limiting
The API implements rate limiting to prevent abuse:
- 100 requests per minute per IP address
- 1000 requests per hour per authenticated user