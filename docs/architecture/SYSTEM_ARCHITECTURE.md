# ReguGuard — System Architecture

## 1. Architecture Overview

ReguGuard will initially use a modular monolith architecture.

The application will expose REST APIs through FastAPI and separate business functionality into independently organized modules.

## 2. High-Level Components

### Frontend
- React
- TypeScript
- API-driven communication

### Backend
- Python
- FastAPI
- Pydantic
- SQLAlchemy

### Business Modules
- Organizations and Users
- Document Management
- Knowledge Management
- Audit Management
- CAPA Management
- CSV and Validation
- AI System Assurance

### AI Services
- Document Processing
- Embedding Generation
- Retrieval and Search
- LLM Integration
- Structured Output Generation
- LangGraph Workflows
- AI Evaluation

### Data Layer
- PostgreSQL for relational data.
- pgvector for embedding storage and vector search.
- Object storage for uploaded documents and evidence.

### Cloud Infrastructure
- Microsoft Azure
- Containerized deployment
- GitHub Actions CI/CD

## 3. Core Data Flow

### Document Ingestion

1. User submits a document.
2. Backend validates the upload.
3. Document is stored in object storage.
4. Metadata is persisted in PostgreSQL.
5. Background processing extracts document content.
6. Extracted content is cleaned and chunked.
7. Embeddings are generated.
8. Chunks and embeddings are stored for retrieval.

### RAG Query

1. User submits a question.
2. Backend validates the request and permissions.
3. Retrieval searches relevant document chunks.
4. Relevant evidence is assembled.
5. LLM generates a structured response.
6. Citation references are validated against retrieved evidence.
7. Response is returned with source references.

### Audit Assessment

1. User selects documents and requirements.
2. Retrieval identifies relevant evidence.
3. AI generates potential findings.
4. Finding structure and evidence are validated.
5. Human reviewer evaluates the draft.
6. Approved findings are recorded.

## 4. Architectural Principles

- Modular monolith initially.
- Clear separation of business logic and AI services.
- API-first backend development.
- Organization-level data isolation.
- Evidence-backed AI outputs.
- Human approval for consequential actions.
- Versioned documents and regulatory references.
- Testable and maintainable components.

## 5. Security Considerations

- Authentication and authorization.
- Tenant-level access enforcement.
- Secure document storage.
- Input validation.
- Prompt-injection protection.
- Secrets management.
- Audit event recording.
- AI output validation.

## 6. Architecture Evolution

The application will evolve incrementally.

Microservices will only be considered if independent scaling, deployment, or operational requirements justify the additional complexity.