# ADR-001: Adopt a Modular Monolith Architecture

## Status

Accepted — Initial architectural direction.

## Context

ReguGuard requires multiple business domains, including QMS management, document intelligence, audit management, CAPA workflows, CSV, and AI assurance.

The application also requires shared database access, authentication, AI services, and workflow orchestration.

Starting with microservices would introduce additional operational complexity before independent service boundaries and scaling requirements are established.

## Decision

Use a modular monolith architecture for the initial development.

The backend will use Python and FastAPI, with business capabilities separated into well-defined modules.

AI infrastructure will be organized separately from core business logic.

## Rationale

- Simpler initial development and deployment.
- Easier local development and debugging.
- Shared transaction management.
- Clear separation of business responsibilities.
- Lower infrastructure complexity.
- Ability to extract services later if justified.

## Consequences

### Positive

- Faster initial development.
- Easier integration testing.
- Reduced operational overhead.
- Clear module boundaries.

### Trade-offs

- Shared application deployment.
- Need to maintain strict module boundaries.
- Independent scaling of individual modules is limited.

## Future Review

Reconsider the architecture if particular modules develop independent scaling, deployment, availability, or operational requirements.