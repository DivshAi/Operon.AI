# Contributing to AI Agentic Platform

Thank you for considering contributing to the AI Agentic Platform! We welcome contributions from everyone.

## Code of Conduct

This project adheres to a Code of Conduct that we expect contributors to follow. Please read [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) before contributing.

## How to Contribute

### Reporting Bugs

1. Ensure the bug was not already reported by searching on GitHub under [Issues](https://github.com/your-username/ai-agentic-platform/issues)
2. If you're unable to find an open issue addressing the problem, open a new one
3. Include a clear title and description with as much relevant information as possible

### Suggesting Enhancements

1. Open a new issue with a clear title and detailed description
2. Explain why this enhancement would be useful
3. Provide examples if possible

### Pull Request Process

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a pull request

## Development Setup

### Prerequisites

- Python 3.8 or higher
- Node.js 16 or higher
- Docker and Docker Compose
- Git

### Backend Development

1. Clone the repository
2. Create a virtual environment:
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Frontend Development

1. Navigate to frontend directory:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```

## Code Style Guidelines

### Python (Backend)

- Follow PEP 8 style guide
- Use type hints for all functions and methods
- Write docstrings for all public functions and classes
- Keep functions small and focused on a single responsibility

### TypeScript (Frontend)

- Follow TypeScript best practices
- Use strict typing
- Write JSDoc comments for complex functions
- Maintain consistent naming conventions

## Testing

### Backend Tests

All backend code should be tested with pytest:
```bash
cd backend
pytest
```

### Frontend Tests

All frontend components should be tested with Jest and React Testing Library:
```bash
cd frontend
npm test
```

## Documentation

All new features must include documentation updates. Please ensure:

- API endpoints are documented in [docs/api-endpoints.md](docs/api-endpoints.md)
- Database schema changes are reflected in [docs/database-schema.md](docs/database-schema.md)
- Architecture decisions are documented in [docs/architecture.md](docs/architecture.md)

## License

By contributing, you agree that your contributions will be licensed under the MIT License.