# AI Agentic Platform - Developer Documentation

## Overview
This document serves as the complete developer guide for the AI Agentic Platform. It includes setup instructions, code structure, API documentation, and development best practices.

## Project Setup

### Prerequisites
- Python 3.8 or higher
- Node.js 16 or higher
- Docker and Docker Compose
- Git
- PostgreSQL (for production environment)
- SQLite (for development environment)

### Environment Setup

1. Clone the repository:
   ```
   git clone <repository-url>
   cd AI_Agentic_Platform
   ```

2. Create a virtual environment for backend development:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install Python dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Install frontend dependencies:
   ```
   cd frontend
   npm install
   ```

5. Set up environment variables:
   ```
   cp .env.example .env
   # Edit .env with appropriate values
   ```

### Running the Application

#### Development Mode
1. Start the database (PostgreSQL or SQLite for development):
   ```
   # For local PostgreSQL
   docker run -d --name postgres-db -e POSTGRES_PASSWORD=password -p 5432:5432 postgres:13
   
   # For development with SQLite, no additional setup needed
   ```

2. Start the backend server:
   ```
   cd backend
   uvicorn main:app --reload
   ```

3. Start the frontend development server:
   ```
   cd frontend
   npm run dev
   ```

## Code Structure

### Backend Structure
```
backend/
├── main.py              # Main FastAPI application
├── models.py            # SQLModel database schemas
├── routes/              # API endpoint handlers
│   ├── auth.py          # Authentication endpoints
│   ├── agents.py        # Agent CRUD endpoints
│   ├── teams.py         # Team CRUD endpoints
│   └── prompts.py       # Prompt CRUD and versioning endpoints
├── services/            # Business logic and service classes
│   ├── orchestrator.py  # Multi-agent execution logic
│   └── prompt_store.py  # Prompt storage and versioning
├── config.py            # Configuration loading and validation
├── utils/               # Utility functions
│   └── logging.py       # Structured logging setup
└── requirements.txt     # Python dependencies
```

### Frontend Structure
```
frontend/
├── pages/               # Next.js pages
│   ├── _app.tsx         # App context provider
│   ├── login.tsx        # Login page
│   ├── register.tsx     # Registration page
│   ├── dashboard.tsx    # Main dashboard
│   ├── agents/          # Agent-related pages
│   │   └── [id].tsx     # Agent detail page
│   ├── teams/           # Team-related pages
│   │   └── [id].tsx     # Team detail page
│   └── prompts/         # Prompt-related pages
│       ├── index.tsx    # Prompt list page
│       └── [promptId].tsx # Prompt detail page
├── components/          # Reusable UI components
│   ├── AgentCard.tsx
│   ├── TeamPanel.tsx
│   └── PromptCard.tsx
├── lib/                 # Library files
│   └── api.ts           # API client with JWT interceptor
├── public/              # Static assets
└── styles/              # CSS and styling files
```

## API Documentation

### Authentication Endpoints
- `POST /auth/register` - Register a new user
- `POST /auth/login` - Authenticate user and return JWT token

### Agent Endpoints
- `GET /agents` - List all agents
- `POST /agents` - Create a new agent
- `GET /agents/{id}` - Get specific agent details
- `PUT /agents/{id}` - Update an agent
- `DELETE /agents/{id}` - Delete an agent

### Team Endpoints
- `GET /teams` - List all teams
- `POST /teams` - Create a new team
- `GET /teams/{id}` - Get specific team details
- `PUT /teams/{id}` - Update a team
- `DELETE /teams/{id}` - Delete a team

### Prompt Endpoints
- `GET /prompts` - List all prompts
- `POST /prompts` - Create a new prompt
- `GET /prompts/{id}` - Get specific prompt details
- `PUT /prompts/{id}` - Update a prompt
- `DELETE /prompts/{id}` - Delete a prompt
- `GET /prompts/{id}/versions` - Get all versions of a prompt

## Development Best Practices

### Code Quality
- Follow PEP 8 style guide for Python code
- Use TypeScript for frontend code with strict typing
- Write comprehensive unit tests for all components
- Implement proper error handling and logging

### Security
- All passwords are hashed using secure hashing algorithms
- JWT tokens are used for authentication and authorization
- Input validation is performed on all endpoints
- Regular security updates and vulnerability scanning are implemented

### Performance
- Database connection pooling is used for efficient resource usage
- Caching strategies are implemented where appropriate
- Asynchronous operations are used for I/O-bound tasks
- Load testing and performance optimization are ongoing

## Testing

### Backend Tests
Backend tests are written using pytest and cover:
- Unit tests for individual functions
- Integration tests for API endpoints
- Database interaction tests
- Authentication and authorization tests

### Frontend Tests
Frontend tests use Jest and React Testing Library to ensure:
- Component rendering and behavior
- API integration testing
- User interface interactions
- Responsive design functionality

## Deployment

### Local Development
For local development, the application uses Docker containers for consistent environments.

### Production Deployment
Production deployment is handled through Kubernetes with:
- Horizontal pod autoscaling
- SSL termination at ingress level
- Persistent storage for PostgreSQL
- Monitoring and logging integration

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a pull request