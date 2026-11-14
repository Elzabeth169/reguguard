# ReguGuard

**AI-powered Quality Intelligence, Regulatory Compliance and AI Assurance Platform for Life Sciences.**

ReguGuard is a software engineering project exploring how AI can support quality management, regulatory compliance, audit preparation, and computerized system validation in pharmaceutical and biotechnology environments.

## Vision

Help life sciences organizations connect quality documentation, regulatory requirements, audit findings, corrective actions, and computerized system validation through an evidence-driven AI platform.

## Core Domains

### 1. QMS Intelligence & Audit Management
- Quality document management
- AI-powered document intelligence
- Regulatory requirement mapping
- Citation-backed compliance assessments
- Audit finding generation
- CAPA drafting and management
- Quality analytics

### 2. CSV & AI System Assurance
- Computerized system inventory
- Intended-use and risk assessment
- Requirements management
- Validation planning
- Test case generation
- Requirements traceability
- Validation evidence management
- AI system change assessment

## Technology Stack

| Component | Technology |
|---|---|
| Frontend | React, TypeScript |
| Backend | Python, FastAPI |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| Vector Search | pgvector |
| AI Integration | Azure OpenAI |
| AI Orchestration | LangGraph |
| Containerization | Docker |
| CI/CD | GitHub Actions |
| Cloud | Microsoft Azure |

## Architecture

ReguGuard follows a modular monolith architecture.

The frontend communicates with a FastAPI backend, which coordinates business modules, AI services, database operations, and document processing.

## Development Status

**Status: Initial project setup**

Planned development milestones:

- [ ] Backend foundation
- [ ] Document management and ingestion
- [ ] AI knowledge and retrieval engine
- [ ] Audit intelligence
- [ ] CAPA workflows
- [ ] CSV and AI assurance
- [ ] Enterprise security and deployment

Features will only be marked complete after implementation and testing.

## Project Documentation

- [Product Requirements](docs/product/PRODUCT_REQUIREMENTS.md)
- [System Architecture](docs/architecture/SYSTEM_ARCHITECTURE.md)
- [Architecture Decision Records](docs/decisions/ADR-001-modular-monolith.md)

## Important Disclaimer

ReguGuard is an experimental decision-support prototype. It is not a certified QMS, regulatory compliance system, or validated computerized system. AI-generated assessments and recommendations require qualified human review.

Development and testing should use synthetic or publicly available data. No confidential employer or customer information should be committed to this repository.

## License

To be determined.# reguguard
AI-powered Quality Management, Regulatory Compliance and AI Assurance Platform for Life Sciences.
