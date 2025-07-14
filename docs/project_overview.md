---
llm_doc: true
audience: LLM
maintainer: LLM
last_updated: 2025-07-08
project: risa
purpose: High-level, living documentation for LLM understanding and maintenance
---

# Project Documentation

## LLM Maintenance Notes

- After each commit, review code changes and update only the relevant sections.
- When adding new features, create a new section or subsection as appropriate.
- When removing features, mark the section as deprecated before deleting.
- Always update the Changelog with a summary of changes.
- Use explicit section boundaries (<!-- SECTION: ... -->) for each major section.
- Reference main codebase files for each feature or API.

## Changelog

## Table of Contents

1. Overview
2. Technology Stack
3. Configuration
4. Features & Usage
5. API Reference
6. Project Architecture
7. Glossary

<!-- SECTION: 1. Overview -->
## 1. Overview

### Key Concepts

<!-- ENDSECTION -->

<!-- SECTION: 2. Technology Stack -->
## 2. Technology Stack

### Backend

- **FastAPI**: High-performance Python web framework providing both REST API and web UI
- **SQLModel**: SQLAlchemy-based ORM for database operations with Pydantic integration
- **SQLite**: Lightweight database for local storage and development
- **Alembic**: Database migration management and version control

### Authentication & Security

- **JWT**: JSON Web Tokens for stateless authentication
- **OAuth2**: Password flow implementation for secure API access
- **bcrypt**: Password hashing and verification
- **CORS**: Cross-origin resource sharing configuration

### Job/Task Processing

- **Huey**: Lightweight task queue for background job processing
- **Redis**: Optional message broker for distributed job queues
- **Priority Queues**: Job prioritization system (highest to lowest)

### Frontend & UI

- **Jinja2**: Server-side templating engine for dynamic HTML generation
- **Bootstrap 5**: CSS framework for responsive, modern UI components
- **JavaScript**: Client-side interactivity and real-time updates
- **WebSockets**: Real-time communication for job status and app manager updates

### Development & Deployment

- **Poetry**: Dependency management and packaging
- **Docker**: Containerization support for consistent deployments
- **Uvicorn**: ASGI server for running FastAPI applications
- **Loguru**: Advanced logging with structured output

### External Integrations

- **rsync**: File synchronization between environments

<!-- ENDSECTION -->

<!-- SECTION: 3. Configuration -->
## 3. Configuration

Application behavior is controlled by environment variables defined in `app/models/settings.py`. These can be set in an `.env` file.

**Key Environment Variables:**

| Variable | Description | Default / Example |
| :--- | :--- | :--- |
| `ENV_NAME` | The name of the current environment. **Required**. | `dev`, `local`, `host`, `playground` |
| `DB_URL` | The SQLAlchemy database connection string. | `sqlite:///./app/data/database.sqlite3` |
| `PROJECT_NAME` | The name of the project. | `vcore-app` |
| `FIRST_SUPERUSER_USERNAME` | Username for the initial superuser account. | `admin` |
| `FIRST_SUPERUSER_PASSWORD` | Password for the initial superuser account. | `changeme` |
| `FIRST_SUPERUSER_EMAIL` | Email for the initial superuser account. | `admin@example.com` |
| `JWT_ACCESS_SECRET_KEY` | Secret key for JWT access tokens. **Required**. | A long, random string. |
| `JWT_REFRESH_SECRET_KEY`| Secret key for JWT refresh tokens. **Required**. | A long, random string. |
<!-- ENDSECTION -->

<!-- SECTION: 4. Features & Usage -->
## 4. Features & Usage

<!-- ENDSECTION -->

<!-- SECTION: 5. API Reference -->
## 5. API Reference

This application exposes a RESTful API under the `/api/v1/` prefix.

### Key Endpoints

- **Authentication**:
    - `POST /login/access-token`: Obtain JWT tokens using username and password.
    - `POST /login/refresh-token`: Refresh an access token.

- **CRUD Operations**: Standard `GET`, `POST`, `PUT`, `DELETE` endpoints are available for:

<!-- ENDSECTION -->

<!-- SECTION: 6. Project Architecture -->
## 6. Project Architecture

The application is logically divided into two main parts: `backend` and `frontend`.

<!-- ENDSECTION -->

<!-- SECTION: 7. Glossary -->
## 7. Glossary

| Term | Definition |
| :--- | :--- |
| Job Queue | Background task system powered by Huey. |
| Huey | Python task queue used for background jobs. |
| CRUD | Create, Read, Update, Delete operations. |
| WebSocket | Real-time communication protocol used for job/app updates. |
| Settings | Settings loaded from environment variables or .env file on startup. |
| Config | Configurable configuration loaded from config file on each request. |

<!-- ENDSECTION -->
