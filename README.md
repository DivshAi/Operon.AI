# AI Agentic Platform

An intelligent platform for creating, configuring, and managing AI agents with orchestration capabilities.

## Overview

The AI Agentic Platform is a comprehensive solution that enables users to:
- Create, configure, and version AI agents
- Assemble agents into autonomous teams with orchestration rules
- Store, manage, and evolve prompt libraries end-to-end
- Execute multi-agent workflows emphasizing speed, efficiency, quality, scale, and continuous innovation

## Features

- **Agent Management**: Create and configure individual AI agents with custom configurations
- **Team Orchestration**: Assemble agents into teams with defined collaboration rules
- **Prompt Repository**: Store, version, and manage prompt templates with tagging and audit trails
- **Multi-LLM Support**: Integration with both local LLMs (via Ollama) and cloud-hosted LLMs (OpenAI, Anthropic, Azure)
- **Role-Based Access Control**: Different user personas with appropriate permissions
- **Containerized Deployment**: Docker and Kubernetes support for easy deployment

## Technology Stack

### Backend
- Python FastAPI
- SQLModel (SQLite/PostgreSQL)
- JWT-based authentication
- Ollama-py or subprocess for local LLM integration
- OpenAI, Anthropic, Azure SDKs for cloud LLM integration

### Frontend
- Next.js (React + TypeScript)
- Tailwind CSS for styling
- Axios for HTTP requests
- SWR for data fetching and caching
- React Icons for UI components

### Infrastructure
- Docker and docker-compose for containerization
- Kubernetes manifests for production deployment
- GitHub Actions for CI/CD
- Prometheus, Grafana, Sentry for monitoring and logging

## Getting Started

### Prerequisites
- Python 3.8 or higher
- Node.js 16 or higher
- Docker and Docker Compose
- Git

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd AI_Agentic_Platform
   ```

2. Set up the backend:
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Set up the frontend:
   ```bash
   cd frontend
   npm install
   ```

4. Start the development servers:
   ```bash
   # In backend directory
   uvicorn main:app --reload
   
   # In frontend directory  
   npm run dev
   ```

## Project Structure

```
AI_Agentic_Platform/
├── backend/              # Python FastAPI backend
│   ├── main.py           # Main application file
│   ├── models.py         # Database models
│   ├── routes/           # API endpoint handlers
│   ├── services/         # Business logic and service classes
│   ├── config.py         # Configuration loading
│   └── utils/            # Utility functions
├── frontend/             # Next.js frontend
│   ├── pages/            # Next.js pages
│   ├── components/       # Reusable UI components
│   ├── lib/              # Library files
│   └── public/           # Static assets
└── deployment/           # Deployment configurations
    ├── docker-compose.yml
    ├── Dockerfile.backend
    ├── Dockerfile.frontend
    └── k8s/               # Kubernetes manifests
```

## Documentation

- [Architecture](docs/architecture.md)
- [Database Schema](docs/database-schema.md)
- [API Endpoints](docs/api-endpoints.md)
- [Developer Documentation](docs/developer-documentation.md)

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.