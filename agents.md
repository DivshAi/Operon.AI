You are an expert full-stack engineer. Provide a detailed, step-by-step plan and code scaffolding to build a production-ready, scalable web platform that lets individual users and enterprise customers:

  • Create, configure, and version AI agents
  • Assemble agents into autonomous teams with orchestration rules
  • Store, manage, and evolve prompt libraries end-to-end
  • Execute multi-agent workflows emphasizing speed, efficiency, quality, scale, and continuous innovation

The platform must support:
  – Python FastAPI backend with RESTful endpoints
  – Next.js (React + TypeScript) frontend
  – Local LLMs via Ollama (ollama-py or subprocess)
  – Cloud-hosted LLMs (OpenAI, Anthropic, Azure) toggled via environment variables
  – SQLModel (SQLite for dev, PostgreSQL for prod)
  – JWT-based authentication
  – Prompt repository module with versioning, tagging, and audits
  – Containerization with Docker + docker-compose
  – Kubernetes manifests for production
  – CI/CD via GitHub Actions
  – Monitoring/logging (Prometheus, Grafana, Sentry)

User Personas:
  – Individual Developers: Focus on ease of use, rapid prototyping, and learning resources
  – Enterprise Teams: Emphasis on security, collaboration features, and scalability
  – DevOps Engineers: Prioritize deployment automation, monitoring, and performance optimization
  – Product Managers: Need dashboards, analytics, and workflow visualization tools
  – Platform Admin: Has functionality related to platform administration including user management, system configuration, and monitoring
  – Customer Admin: Has admin functionality specific to the customer's organization including team management, resource allocation, and access control

Customer Experience:
  – Interactive tutorials and guided setup for new users
  – Sample agents and templates to get started quickly
  – Visual agent configuration interfaces with drag-and-drop functionality
  – Real-time preview capabilities for agent behavior
  – Dashboard with performance metrics and health indicators
  – Comprehensive API documentation with interactive examples
  – SDKs for popular programming languages
  – Code snippets and examples for common use cases
  – Agent marketplace with ratings and reviews
  – Template library for common workflows
  – Community sharing features
  – Role-based access controls (RBAC)
  – Billing and subscription management
  – Usage analytics and reporting
  – Integration with popular business tools (Slack, GitHub, etc.)
  – Interactive tutorials and guided setup for new users
  – Sample agents and templates to get started quickly
  – Visual agent configuration interfaces with drag-and-drop functionality
  – Real-time preview capabilities for agent behavior
  – Dashboard with performance metrics and health indicators
  – Comprehensive API documentation with interactive examples
  – SDKs for popular programming languages
  – Code snippets and examples for common use cases
  – Agent marketplace with ratings and reviews
  – Template library for common workflows
  – Community sharing features
  – Role-based access controls (RBAC)
  – Billing and subscription management
  – Usage analytics and reporting
  – Integration with popular business tools (Slack, GitHub, etc.)

Platform Robustness Features:
  – Comprehensive error handling and recovery mechanisms
  – Data encryption at rest and in transit
  – Audit logging for compliance (GDPR, SOC2)
  – Regular security updates and vulnerability scanning
  – Backup and restore functionality
  – Resource usage monitoring and optimization
  – Load testing and performance optimization

Additional Security & Compliance Features:
  – Rate limiting and API throttling to prevent abuse
  – Secure credential storage and management
  – Input validation and sanitization for all endpoints
  – Data retention policies and automated cleanup
  – Audit trail requirements for different user roles
  – Compliance with GDPR, HIPAA, and other relevant frameworks

Operational Excellence Features:
  – Automated backup and restore strategies for all data
  – Data migration and versioning strategies
  – Disaster recovery planning and testing
  – Performance benchmarks and baseline monitoring

For each major step, include:
  1. Shell commands to run
  2. Folder structure and repo init
  3. All config files (Dockerfile, docker-compose.yml, k8s manifests, .env.example)
  4. Key source files with code and in-line comments
  5. Explanations of design decisions and best practices

Outline your response in these phases:

Phase 1: Monorepo Setup
  • Create root folder, initialize Git, configure .gitignore
  • Define /backend, /frontend, /deployment directories
  • Include documentation templates for user guides and API references
  • Set up initial project structure with README.md, CONTRIBUTING.md, CODE_OF_CONDUCT.md

Phase 2: Backend Scaffolding
  2.1 Virtual environment, install dependencies (fastapi, uvicorn, sqlmodel, python-jose, ollama-py, openai, etc.)
  2.2 backend/main.py: FastAPI app, JWT middleware with role-based access controls
  2.3 backend/models.py: User, Agent, Team, Prompt SQLModel classes (fields: body, version, tags, audit_log)
  2.4 backend/routes/auth.py: register/login with JWT and user persona management
  2.5 backend/routes/agents.py & teams.py: CRUD endpoints with validation and error handling
  2.6 backend/routes/prompts.py: CRUD and version endpoints for prompt repository with tagging and audit trails
  2.7 backend/services/orchestrator.py: multi-agent execution logic, local vs cloud model loader, fetch prompts by version with performance monitoring
  2.8 backend/services/prompt_store.py: interfaces to store, tag, version, rollback prompts with backup capabilities
  2.9 backend/config.py: load environment variables, database URL, LLM credentials with configuration validation
  2.10 backend/utils/logging.py: structured logging for monitoring and debugging

Phase 3: Frontend Scaffolding
  3.1 npx create-next-app --ts, install axios, swr, tailwindcss, react-icons
  3.2 pages/_app.tsx: AuthContext provider with user persona detection and role-based UI components
  3.3 pages/login.tsx & register.tsx: JWT auth forms with personalized onboarding flows based on user personas
  3.4 pages/dashboard.tsx: overview of agents, teams, health, prompt repo status with performance metrics and quick actions
  3.5 pages/agents/[id].tsx & teams/[id].tsx: configuration UIs with drag-and-drop interfaces for agent assembly
  3.6 pages/prompts/index.tsx: list, search, filter prompts by tag/version with version comparison tools
  3.7 pages/prompts/[promptId].tsx: view/edit versions, change tags, audit history with real-time preview capabilities
  3.8 components/AgentCard.tsx, TeamPanel.tsx, PromptCard.tsx: reusable UI with responsive design and accessibility features
  3.9 lib/api.ts: Axios instance with JWT interceptor, error handling, and retry mechanisms
  3.10 pages/tutorial.tsx: Interactive tutorial for new users with guided setup based on user persona

Phase 4: Containerization
  • Dockerfile.backend, Dockerfile.frontend with multi-stage builds for optimization
  • docker-compose.yml: backend, frontend, postgres services with health checks and resource limits
  • .env.example with comprehensive environment variable documentation
  • Include backup and restore scripts for containerized environments
  • Implement caching strategies (Redis/Memcached) for performance optimization

Phase 5: Kubernetes Deployment
  • deployment/backend-deployment.yaml & service.yaml with horizontal pod autoscaling
  • deployment/frontend-deployment.yaml & ingress.yaml with SSL termination and rate limiting
  • deployment/postgres-statefulset.yaml with persistent volumes and backup strategies
  • Include monitoring and logging configurations for Kubernetes environments
  • Implement service mesh patterns for better observability and security

Phase 6: CI/CD with GitHub Actions
  • .github/workflows/ci.yml: lint, test, build images with security scanning and code coverage reports
  • .github/workflows/cd.yml: push to container registry, kubectl apply with rollback capabilities
  • Include automated performance testing and security checks in CI pipeline
  • Implement blue-green deployment strategies for zero-downtime releases

Phase 7: Monitoring & Logging
  • Expose Prometheus metrics in FastAPI with custom metrics for agent performance
  • Grafana dashboard JSON snippet with pre-configured panels for key metrics
  • Sentry initialization in both backend and frontend with error grouping and alerting
  • Include structured logging with correlation IDs for distributed tracing
  • Implement centralized logging with ELK stack or similar

Begin by showing the exact shell commands and file-tree for Phase 1. Then for each subsequent phase, display all required files with full contents and explanatory comments.
