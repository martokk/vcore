---
llm_doc: true
audience: LLM
maintainer: LLM
last_updated: 2025-07-23
project: vcore
purpose: Comprehensive documentation for the vCore Framework - a reusable FastAPI-based web application framework
---

# vCore Framework Documentation

## LLM Maintenance Notes

- After each commit, review code changes and update only the relevant sections.
- When adding new features, create a new section or subsection as appropriate.
- When removing features, mark the section as deprecated before deleting.
- Always update the Changelog with a summary of changes.
- Use explicit section boundaries (<!-- SECTION: ... -->) for each major section.
- Reference main codebase files for each feature or API.

## Changelog

### 2025-07-23

- Initial comprehensive documentation created
- Added complete feature coverage for vCore Framework v1.0.0-alpha.1
- Complete documentation review and accuracy update
- Corrected project structure to reflect actual implementation
- Fixed version number and file paths
- Updated API reference to match actual endpoints
- Corrected configuration settings structure

## Table of Contents

1. [Overview](#1-overview)
2. [Technology Stack](#2-technology-stack)
3. [Configuration](#3-configuration)
4. [Features & Usage](#4-features--usage)
5. [API Reference](#5-api-reference)
6. [Project Architecture](#6-project-architecture)
7. [Glossary](#7-glossary)

<!-- SECTION: 1. Overview -->
## 1. Overview

The vCore Framework is a comprehensive, reusable FastAPI-based web application framework designed to provide a solid foundation for building modern web applications. It provides a backend-only framework with built-in support for REST APIs, background job processing, user management, and real-time communication.

The vCore Framwork is meant to be used as a package. It works in conjunction with the Application Layer to create a complete web applciation. The vCore Framwework abstracts the re-usable components of the application, such as the backend, database, job processing, and authentication, allowing the application to focus on the business logic.

### Key Concepts

- **Backend Framework**: The framework (`/backend`) provides all backend functionality while applications can build their own frontend or use the provided template system
- **Job Processing**: Built-in background job processing with priority management and real-time monitoring using Huey
- **Authentication Ready**: Complete JWT-based authentication system with user management
- **Real-time Updates**: WebSocket integration for live updates of job status and system information
- **Production Ready**: Includes logging, security, database migrations, and monitoring capabilities

### Architecture Philosophy

The vCore Framework follows a modular, layered architecture:

- **Core Layer**: Database, security, logging, and basic services
- **Business Layer**: CRUD operations, job processing, and business logic
- **API Layer**: RESTful endpoints and WebSocket connections
- **Presentation Layer**: Jinja2 templates and static assets (optional)
- **Integration Layer**: External service connections and utilities

<!-- ENDSECTION -->

<!-- SECTION: 2. Technology Stack -->
## 2. Technology Stack

### Core Backend Framework

- **FastAPI**: High-performance async web framework with automatic OpenAPI documentation
- **SQLModel**: Modern ORM combining SQLAlchemy and Pydantic for type-safe database operations
- **Pydantic**: Data validation and serialization with Python type annotations
- **Uvicorn**: Lightning-fast ASGI server for production deployments

### Database & Storage

- **SQLAlchemy**: Powerful ORM with connection pooling and advanced querying
- **Alembic**: Database schema versioning and migration management
- **SQLite/PostgreSQL**: Support for both lightweight development and production databases
- **Connection Pooling**: QueuePool with configurable pool sizes for optimal performance

### Authentication & Security

- **JWT (PyJWT)**: Stateless authentication with access and refresh tokens
- **OAuth2**: Password flow implementation following industry standards
- **Passlib + bcrypt**: Secure password hashing with configurable complexity
- **CORS**: Cross-origin resource sharing with configurable policies
- **Input Validation**: Comprehensive request validation and sanitization

### Job Processing & Background Jobs

- **Huey**: Lightweight, Redis-compatible job queue with SQLite backend support
- **Priority Queues**: Five-level priority system (highest, high, normal, low, lowest)
- **Job Scheduling**: Cron-like job scheduling with repeat patterns
- **Real-time Monitoring**: Live job status updates via WebSockets
- **Multi-Queue Support**: Separate queues for different job types (default, reserved)

### Frontend & UI Framework

- **Jinja2**: Powerful templating engine with template inheritance and macros
- **Bootstrap 5**: Modern, responsive CSS framework with dark/light themes
- **Custom CSS System**: Modular CSS architecture with CSS custom properties
- **JavaScript Utilities**: Pre-built components for common UI patterns
- **Static Asset Management**: Organized asset structure with versioning support

### Real-time Communication

- **WebSockets**: Full-duplex communication for live updates
- **Connection Management**: Built-in connection pooling and management
- **Broadcasting**: Multi-client message broadcasting capabilities
- **Auto-reconnection**: Client-side reconnection handling

### Development & Deployment

- **Poetry**: Modern dependency management with lock files
- **Docker**: Containerization support with optimized images
- **Pre-commit Hooks**: Automated code quality checks
- **Comprehensive Testing**: Pytest with async support and coverage reporting
- **Code Quality Tools**: Ruff, MyPy, Bandit, Safety for code analysis
- **Makefile Automation**: Common development jobs automated

### Logging & Monitoring

- **Loguru**: Advanced logging with structured output and rotation
- **Request Logging**: Automatic API request/response logging
- **Job Execution Logging**: Detailed job execution tracking with file outputs
- **Error Handling**: Comprehensive exception handling and reporting

### External Integrations

- **LLM Support**: Built-in support for OpenAI, Anthropic, Google, and Groq APIs
- **Email Services**: SMTP integration with template support
- **Notification Systems**: Telegram and email notification support
- **HTTP Client**: AsyncIO-compatible HTTP client (HTTPX)

<!-- ENDSECTION -->

<!-- SECTION: 3. Configuration -->
## 3. Configuration

The vCore Framework uses environment-based configuration managed through Pydantic Settings. All configuration is centralized in `backend/models/settings.py`.

### Configuration Loading

Configuration is loaded in the following priority order:

1. Environment variables
2. `.env` file in project root or `data/.env`
3. Default values (where applicable)

### Core Configuration Categories

#### Environment & Debug Settings

```python
ENV_NAME: str           # Required: Environment identifier (dev, prod, staging)
DEBUG: bool = True      # Enable debug mode
LOG_LEVEL: str = "INFO" # Logging level (DEBUG, INFO, WARNING, ERROR)
```

#### Database Configuration

```python
DB_URL: str                    # Database connection string
DATABASE_ECHO: bool = False    # Enable SQLAlchemy query logging
```

#### Server Configuration

```python
SERVER_HOST: str = "0.0.0.0"          # Server bind address
SERVER_PORT: int = 5000                # Server port
BASE_DOMAIN: str = "localhost:5000"    # Base domain for URL generation
BASE_URL: str = "http://localhost:5000" # Complete base URL
PROXY_HOST: str = "127.0.0.1"          # Proxy host
UVICORN_RELOAD: bool = True            # Enable auto-reload in development
UVICORN_ENTRYPOINT: str = "app.app:app" # App entry point
UVICORN_WORKERS: int = 1               # Number of worker processes
```

#### Security Configuration

```python
JWT_ACCESS_SECRET_KEY: str             # Required: JWT access token signing key
JWT_REFRESH_SECRET_KEY: str            # Required: JWT refresh token signing key
ACCESS_TOKEN_EXPIRE_MINUTES: int = 30  # Access token expiration
REFRESH_TOKEN_EXPIRE_MINUTES: int = 10080 # Refresh token expiration (7 days)
ALGORITHM: str = "HS256"               # JWT signing algorithm
API_V1_PREFIX: str = "/api/v1"         # API version prefix
```

#### Job Queue Configuration

```python
HUEY_DEFAULT_SQLITE_PATH: str = "data/huey_consumer__default.db"
HUEY_RESERVED_SQLITE_PATH: str = "data/huey_consumer__reserved.db"
HUEY_DEFAULT_LOG_PATH: str = "data/logs/huey_consumer__default.log"
HUEY_RESERVED_LOG_PATH: str = "data/logs/huey_consumer__reserved.log"
```

#### User Management

```python
FIRST_SUPERUSER_USERNAME: str     # Required: Initial superuser username
FIRST_SUPERUSER_EMAIL: str        # Required: Initial superuser email
FIRST_SUPERUSER_PASSWORD: str     # Required: Initial superuser password
USERS_OPEN_REGISTRATION: bool = False # Allow open user registration
```

#### Email & Notifications

```python
SMTP_HOST: str                    # SMTP server hostname
SMTP_PORT: int                    # SMTP server port
SMTP_USER: str                    # SMTP username
SMTP_PASSWORD: str                # SMTP password
SMTP_TLS: bool = True            # Enable TLS encryption
EMAILS_FROM_EMAIL: str           # Default sender email
EMAILS_FROM_NAME: str            # Default sender name
EMAILS_ENABLED: bool = False     # Enable email functionality
EMAIL_RESET_TOKEN_EXPIRE_HOURS: int = 48 # Password reset token expiration

# Email notifications
NOTIFY_EMAIL_ENABLED: bool = False
NOTIFY_EMAIL_TO: str             # Email address for notifications
NOTIFY_TELEGRAM_ENABLED: bool = False
TELEGRAM_API_TOKEN: str = ""     # Telegram bot API token
TELEGRAM_CHAT_ID: int = 0        # Telegram chat ID for notifications
NOTIFY_ON_START: bool = False    # Send notification on startup
```

#### LLM API Keys

```python
OPENAI_API_KEY: str = ""         # OpenAI API key
ANTHROPIC_API_KEY: str = ""      # Anthropic Claude API key
GROQ_API_KEY: str = ""          # Groq API key
GOOGLE_API_KEY: str = ""        # Google Gemini API key
PHI_API_KEY: str = ""           # Phi API key
```

#### Project Settings

```python
PROJECT_NAME: str                # Required: Project name
PACKAGE_NAME: str               # Auto-generated from project name
PROJECT_DESCRIPTION: str        # Project description
VERSION: str                    # Project version
ACCENT: str = "#0000ff"         # Theme accent color
TIMEZONE: str = "America/Chicago" # Default timezone
```

### Configuration Validation

The framework includes comprehensive configuration validation:

- Required fields raise `ValueError` if not provided or set to "invalid_default_value"
- Email fields are validated using Pydantic's `EmailStr`
- Timezone validation with `ZoneInfo`
- Environment-specific validation logic

### Example .env File

```bash
# Core Settings
ENV_NAME=development
DEBUG=true
LOG_LEVEL=DEBUG

# Database
DB_URL=sqlite:///./data/database.sqlite3

# Security (Generate strong random keys)
JWT_ACCESS_SECRET_KEY=your-super-secret-access-key-here
JWT_REFRESH_SECRET_KEY=your-super-secret-refresh-key-here

# Initial User
FIRST_SUPERUSER_USERNAME=admin
FIRST_SUPERUSER_EMAIL=admin@example.com
FIRST_SUPERUSER_PASSWORD=changeme123

# Project
PROJECT_NAME=My vCore App
```

<!-- ENDSECTION -->

<!-- SECTION: 4. Features & Usage -->
## 4. Features & Usage

### User Management & Authentication

#### Features

- JWT-based stateless authentication
- User registration and login
- Role-based access control (superuser/regular user)
- Password reset functionality
- Email verification support

#### Key Files

- `backend/models/user.py` - User data models
- `backend/crud/user.py` - User CRUD operations  
- `backend/core/security.py` - Authentication logic
- `backend/routes/api/v1/endpoints/login.py` - Authentication endpoints

#### Usage Example

```python
# Create a new user
user_data = UserCreateWithPassword(
    username="newuser",
    email="user@example.com", 
    password="securepassword"
)
user = await crud.user.create_with_password(db, obj_in=user_data)

# Authenticate user
tokens = await get_tokens(user.id, fresh=True)
```

### Background Job Processing

#### Features

- Priority-based job queue (5 levels: highest to lowest)
- Support for command-line, script, and API POST jobs
- Real-time job monitoring via WebSockets
- Job retry mechanisms with configurable attempts
- Comprehensive job logging with individual log files
- Job scheduling with cron-like patterns
- Multiple queue support (default and reserved)

#### Job Types

1. **Command Jobs**: Execute shell commands with real-time output streaming
2. **Script Jobs**: Execute Python script classes with structured input/output
3. **API POST Jobs**: Make HTTP POST requests to external APIs
4. **Scheduled Jobs**: Recurring jobs based on cron patterns

#### Key Files

- `backend/models/job.py` - Job data models
- `backend/crud/job.py` - Job CRUD operations
- `backend/jobs/execute_job.py` - Job execution logic
- `backend/services/job_queue.py` - Job queue management
- `backend/routes/api/v1/endpoints/job_queue.py` - Job API endpoints

#### Usage Example

```python
# Create a command job
job_data = JobCreate(
    name="Backup Database",
    command="pg_dump mydb > backup.sql",
    type=JobType.command,
    priority=Priority.high,
    queue_name="default"
)
job = await crud.job.create(db, obj_in=job_data)
```

### CRUD Operations

#### Features

- Generic CRUD base classes with type safety
- Support for ordered models with position management
- Advanced querying with filtering and pagination
- Bulk operations support
- Soft delete capability
- Audit trail support

#### Base CRUD Operations

- `get()` - Retrieve single record by ID
- `get_or_none()` - Retrieve or return None
- `get_all()` - Retrieve all records
- `create()` - Create new record
- `update()` - Update existing record
- `remove()` - Delete record

#### Key Files

- `backend/crud/base.py` - Base CRUD implementation
- `backend/crud/base_ordered.py` - Ordered model CRUD
- `backend/crud/exceptions.py` - CRUD-specific exceptions

#### Usage Example

```python
# Generic CRUD usage
class ItemCrud(BaseCRUD[Item, ItemCreate, ItemUpdate]):
    pass

item_crud = ItemCrud(Item)

# Create item
new_item = await item_crud.create(db, obj_in=ItemCreate(name="Test"))

# Query with filters
items = await item_crud.get_multi(db, name="Test", active=True)
```

### Real-time WebSocket Communication

#### Features

- WebSocket connection management
- Multi-client broadcasting
- Automatic reconnection handling
- Job queue status updates
- System status monitoring

#### Key Files

- `backend/core/websocket.py` - WebSocket base classes
- `backend/services/job_queue_ws_manager.py` - Job queue WebSocket manager
- `backend/routes/api/v1/endpoints/job_queue_ws.py` - WebSocket endpoints
- `frontend/static/js/api_utils.js` - Client-side WebSocket handling

#### Usage Example

```javascript
// Client-side WebSocket connection
const ws = new WebSocket('ws://localhost:5000/api/v1/ws/job-queue');
ws.onmessage = function(event) {
    const data = JSON.parse(event.data);
    if (data.jobs) {
        updateJobsTable(data.jobs);
    }
};
```

### Frontend Templating System (Optional)

#### Features

- Jinja2 template inheritance
- Responsive Bootstrap 5 components
- Dark/light theme support
- Component-based template structure
- Form handling utilities
- JavaScript utility libraries

#### Template Structure

- `frontend/templates/base/` - Base templates and layout components
- `frontend/templates/errors/` - Error page templates
- `frontend/templates/login/` - Authentication templates
- `frontend/templates/jobs/` - Job management templates
- `frontend/templates/user/` - User management templates
- `frontend/templates/dashboard/` - Dashboard components

#### Key Files

- `backend/templating/` - Template configuration and filters
- `frontend/templates/` - Template files
- `frontend/static/` - Static assets (CSS, JS, images)

#### Usage Example

```html
<!-- Extend base template -->
{% extends "base/base.html" %}

<!-- Use template blocks -->
{% block content %}
<div class="container">
    <h1>{{ page_title }}</h1>
    {% include "_alerts.html" %}
</div>
{% endblock %}
```

### Database Migrations

#### Features

- Alembic-powered schema migrations
- Automatic model detection
- Environment-specific migrations
- Migration rollback support
- Initial data seeding

#### Key Files

- `migrations/` - Migration files and configuration
- `alembic.ini` - Alembic configuration
- `backend/core/db.py` - Database setup and initialization

#### Usage Commands

```bash
# Generate new migration
alembic revision --autogenerate -m "Add new table"

# Apply migrations
alembic upgrade head

# Rollback migration
alembic downgrade -1
```

### Utility Libraries

#### Available Utilities

- **DateTime Utilities** (`backend/utils/datetime.py`): Timezone-aware datetime operations
- **Form Utilities** (`backend/utils/form_utils.py`): Form processing helpers
- **Git Utilities** (`backend/utils/git.py`): Git repository operations
- **HTML Sanitization** (`backend/utils/html_sanitizer.py`): Safe HTML processing
- **IP Utilities** (`backend/utils/ip_utils.py`): IP address validation and manipulation
- **LLM Utilities** (`backend/utils/llm_utils.py`): Large Language Model integrations
- **System Status** (`backend/utils/system_status.py`): System monitoring utilities
- **UUID Utilities** (`backend/utils/uuid.py`): UUID generation and validation

<!-- ENDSECTION -->

<!-- SECTION: 4.7 Quick Tools -->
### Quick Tools

The vCore Framework includes a "Quick Tools" system for rapidly building and deploying small, self-contained utilities within your application. Quick Tools are ideal for admin helpers, data converters, or any workflow that benefits from a simple UI and fast iteration.

#### Features

- Rapid development of single-purpose tools
- Consistent UI/UX using a shared base template
- Easy integration into the main application
- Supports custom forms, logic, and result rendering

#### Key Files & Structure

- `frontend/templates/quick_tools/quick_tool_base.html` – The base Jinja2 template for all Quick Tools, providing a consistent card-based layout, input form, loading, error, and results sections.
- `frontend/templates/quick_tools/` – Directory containing all Quick Tool templates. Each tool typically has its own template extending the base.
- `@create_quick_tool.mdc` – The documented process or script for scaffolding a new Quick Tool, ensuring best practices and consistency.

#### How It Works

- Each Quick Tool is implemented as a Jinja2 template that extends `quick_tool_base.html` and overrides blocks for the tool name, description, input form, and results.
- Backend logic (if needed) is handled via dedicated endpoints or view handlers, following the same modular approach as other features.
- The UI provides built-in sections for loading, error handling, and displaying results, making it easy to deliver a polished user experience with minimal effort.

#### Example: Creating a New Quick Tool

1. **Scaffold the Tool**: Use the `@create_quick_tool.mdc` process to generate a new tool template and any required backend logic.
2. **Implement the Template**: Create a new file in `frontend/templates/quick_tools/`, extending `quick_tool_base.html` and filling in the relevant blocks:

    ```jinja
    {% extends "quick_tools/quick_tool_base.html" %}

    {% block quick_tool_name %}My Tool Name{% endblock %}
    {% block quick_tool_description %}Describe what this tool does.{% endblock %}
    {% block quick_tool_input_form %}
    <!-- Custom form fields here -->
    {% endblock %}
    {% block results_card_body %}
    <!-- Render results here -->
    {% endblock %}
    ```

3. **Add Backend Logic**: Implement any required backend handler to process the tool's input and return results.
4. **Register the Tool**: Add a route or menu entry so users can access the new Quick Tool from the UI.

#### Use Cases

- Data format converters
- Bulk admin actions
- One-off reporting tools
- Utility calculators

Quick Tools empower teams to deliver value quickly without the overhead of building full modules, while maintaining a consistent look and feel across the application.

<!-- ENDSECTION -->

<!-- SECTION: 5. API Reference -->
## 5. API Reference

The vCore Framework exposes a comprehensive RESTful API under the `/api/v1/` prefix with automatic OpenAPI documentation.

### Authentication Endpoints

#### POST `/api/v1/login/access-token`

Obtain JWT access and refresh tokens using username/password credentials.

**Request Body:**

```json
{
    "username": "string",
    "password": "string"
}
```

**Response:**

```json
{
    "access_token": "string",
    "refresh_token": "string"
}
```

#### POST `/api/v1/login/refresh-token`

Refresh an access token using a valid refresh token.

**Request Body:**

```json
{
    "refresh_token": "string"
}
```

#### POST `/api/v1/login/test-token`

Test access token validity.

#### POST `/api/v1/register`

Create new user (if open registration is enabled).

### User Management Endpoints

#### GET `/api/v1/users/me`

Retrieve current authenticated user information.

#### PUT `/api/v1/users/me`

Update current user profile.

#### GET `/api/v1/users/`

List all users (superuser only).

#### POST `/api/v1/users/`

Create new user (superuser only).

#### GET `/api/v1/users/{user_id}`

Retrieve specific user by ID.

#### DELETE `/api/v1/users/{user_id}`

Delete user (superuser only).

### Job Queue Management Endpoints

#### GET `/api/v1/jobs/`

Retrieve all jobs.

**Query Parameters:**

- `status`: Filter by job status (pending, queued, running, done, failed)
- `queue_name`: Filter by queue name
- `priority`: Filter by job priority
- `limit`: Maximum number of results
- `offset`: Pagination offset

#### POST `/api/v1/jobs/`

Create a new job.

**Request Body:**

```json
{
    "name": "string",
    "command": "string", 
    "type": "command|script|api_post",
    "priority": "highest|high|normal|low|lowest",
    "queue_name": "default|reserved",
    "meta": {}
}
```

#### GET `/api/v1/jobs/{job_id}`

Retrieve specific job details.

#### PUT `/api/v1/jobs/{job_id}`

Update job details.

#### DELETE `/api/v1/jobs/{job_id}`

Delete a job.

#### PUT `/api/v1/jobs/{job_id}/status`

Update job status.

#### POST `/api/v1/jobs/{job_id}/kill`

Kill a running job process.

#### GET `/api/v1/jobs/{job_id}/log`

Retrieve job execution logs.

#### POST `/api/v1/jobs/start-consumer`

Start Huey consumer process.

#### POST `/api/v1/jobs/stop-consumer`

Stop Huey consumer process.

#### POST `/api/v1/jobs/push-jobs-to-websocket`

Manually trigger WebSocket broadcast with current jobs.

### Job Scheduler Endpoints

#### GET `/api/v1/job-schedulers/`

List all scheduled jobs.

#### POST `/api/v1/job-schedulers/`

Create a new scheduled job.

**Request Body:**

```json
{
    "env_name": "string",
    "name": "string",
    "description": "string",
    "trigger_type": "on_start" | "repeat",
    "repeat_every_seconds": 3600,
    "job_template": {
        "name": "string",
        "command": "string",
        "type": "command"
    },
    "enabled": true
}
```

#### GET `/api/v1/job-schedulers/{scheduler_id}`

Retrieve scheduler details.

#### PUT `/api/v1/job-schedulers/{scheduler_id}`

Update scheduler configuration.

#### DELETE `/api/v1/job-schedulers/{scheduler_id}`

Delete scheduler.

#### POST `/api/v1/job-schedulers/{scheduler_id}/toggle`

Toggle scheduler enabled/disabled status.

### WebSocket Endpoints

#### WS `/api/v1/ws/job-queue`

Real-time job queue updates. Sends job list updates and log updates whenever jobs change status or logs are updated.

### Response Format

API responses vary by endpoint:

- Most endpoints return Pydantic models directly as JSON
- Some endpoints return `{ "success": true/false, "message": "..." }` for status updates
- Error responses are returned as HTTP status codes with a `detail` field:

```json
{
  "detail": "Error message"
}
```

### Error Codes

Standard HTTP status codes are used:

- 422 Unprocessable Entity: Request validation failed
- 401 Unauthorized: Valid authentication token required
- 403 Forbidden: Insufficient permissions
- 404 Not Found: Requested resource doesn't exist
- 500 Internal Server Error: Unexpected server error

### Authentication

Most endpoints require authentication via JWT Bearer token:

```http
Authorization: Bearer <access_token>
```

<!-- ENDSECTION -->

<!-- SECTION: 6. Project Architecture -->
## 6. Project Architecture

The vCore Framework follows a clean, modular architecture that separates concerns and promotes code reusability.

### Directory Structure

```text
vcore/
├── backend/                     # vCore backend framework
│   ├── core/                    # Core services (DB, security, config, etc.)
│   │   ├── __init__.py
│   │   ├── api_key.py           # API key management
│   │   ├── db.py                # Database configuration
│   │   ├── env.py               # Environment helpers
│   │   ├── hooks.py             # vCore hooks
│   │   ├── huey.py              # Huey queue config
│   │   ├── logger.py            # Logging setup
│   │   ├── security.py          # Auth & password logic
│   │   ├── server.py            # Uvicorn server config
│   │   ├── settings.py          # Settings loader, vCoreBaseSettings
│   │   └── websocket.py         # WebSocket base classes
│   ├── crud/                    # CRUD operations
│   │   ├── __init__.py
│   │   ├── base.py              # Generic CRUD base
│   │   ├── base_ordered.py      # Ordered CRUD base
│   │   ├── exceptions.py        # CRUD-specific exceptions
│   │   ├── job.py               # Job CRUD
│   │   ├── job_scheduler.py     # Job scheduler CRUD
│   │   └── user.py              # User CRUD
│   ├── handlers/                # Backend handlers
│   │   └── __init__.py
│   ├── logic/                   # Business logic modules
│   │   ├── __init__.py
│   │   └── jobs.py              # Job-related logic
│   ├── middleware/              # ASGI/FastAPI middleware
│   │   └── __init__.py
│   ├── models/                  # Data models
│   │   ├── __init__.py
│   │   ├── alerts.py            # Alert models
│   │   ├── base.py              # Base model classes
│   │   ├── common.py            # Common model utilities
│   │   ├── job.py               # Job models
│   │   ├── job_scheduler.py     # Job scheduler models
│   │   ├── msg.py               # Message models
│   │   ├── tokens.py            # Token models
│   │   └── user.py              # User models
│   ├── paths.py                 # Backend path definitions
│   ├── routes/                  # API and view routes
│   │   ├── api/                 # REST API endpoints
│   │   │   ├── __init__.py
│   │   │   ├── deps.py          # API dependencies
│   │   │   └── v1/              # Versioned API
│   │   │       ├── __init__.py
│   │   │       └── endpoints/   # API endpoint modules
│   │   │           ├── __init__.py
│   │   │           ├── job_queue.py
│   │   │           ├── job_queue_ws.py
│   │   │           ├── job_scheduler.py
│   │   │           ├── login.py
│   │   │           └── users.py
│   │   ├── restrict_to_env.py   # Env restriction decorator
│   │   └── views/               # Web view handlers
│   │       ├── __init__.py
│   │       ├── jobs/
│   │       │   ├── job_scheduler.py # Job scheduler View/Page Handler
│   │       │   └── jobs.py # Job View/Page Handler
│   │       ├── login/
│   │       │   └── login.py # Login View/Page Handler
│   │       ├── root/
│   │       │   └── root.py # Root View/Page Handler
│   │       └── user/
│   │           └── user.py # User View/Page Handler
│   ├── scripts/                  # vCore Scripts
│   │   ├── __init__.py
│   │   └── example.py
│   ├── services/                # External/internal services
│   │   ├── __init__.py
│   │   ├── job_queue.py         # Job queue management
│   │   ├── job_queue_ws_manager.py # WebSocket job queue manager
│   │   ├── notify.py            # Notification services
│   │   └── scripts.py           # vCore scripts execution
│   ├── jobs/                   # Background job processing
│   │   ├── __init__.py
│   │   ├── execute_scheduler.py # Scheduler execution logic
│   │   └── execute_tasks.py     # Job execution logic
│   ├── templating/              # Template config & filters (optional)
│   │   ├── __init__.py
│   │   ├── context.py           # Template context helpers
│   │   ├── deps.py              # Template dependencies
│   │   ├── env.py               # Jinja2 environment setup
│   │   └── filters.py           # Jinja2 filters
│   ├── utils/                   # Utility functions
│   │   ├── __init__.py
│   │   ├── datetime.py          # Datetime utilities
│   │   ├── debug_helpers.py     # Debugging helpers
│   │   ├── form_utils.py        # Form processing
│   │   ├── git.py               # Git utilities
│   │   ├── html_sanitizer.py    # HTML sanitization
│   │   ├── ip_utils.py          # IP address utilities
│   │   ├── llm_utils.py         # LLM integration
│   │   ├── system_status.py     # System monitoring
│   │   └── uuid.py              # UUID helpers
│   └── __init__.py
├── frontend/                    # Frontend assets (optional)
│   ├── static/                  # Static files (CSS, JS, images)
│   │   ├── css/
│   │   ├── icons/
│   │   ├── images/
│   │   └── js/
│   └── templates/               # Jinja2 templates (optional)
│       ├── base/                # Base layout templates
│       ├── dashboard/           # Dashboard templates
│       ├── errors/              # Error page templates
│       ├── jobs/                # Job management templates
│       ├── login/               # Auth templates
│       ├── logs/                # Log viewer templates
│       ├── quick_tools/         # Quick tool templates
│       ├── scripts/             # vCore scripts templates
│       │   └── modals/          # vCore scripts modal view
│       └── user/                # User management templates
├── migrations/                  # Database migrations
├── tests/                       # Test suites
├── docs/                        # Project documentation
├── data/                        # Unversioned, uncommitted data files
├── .ai/                         # AI rules and configuration
├── .cursor/                     # Cursor rules and configuration
├── alembic.ini                  # Alembic configuration
├── pyproject.toml               # Poetry project configuration
└── Makefile                     # Development commands

```

### Layer Architecture

#### 1. Core Layer (`backend/core/`)

The foundation layer providing essential services:

- **Database Management**: Connection pooling, session management, initialization
- **Security**: JWT authentication, password hashing, authorization
- **Configuration**: Environment-based settings with validation
- **Logging**: Structured logging with multiple outputs and levels
- **WebSocket**: Real-time communication infrastructure

#### 2. Data Layer (`backend/models/` & `backend/crud/`)

Data persistence and manipulation:

- **Models**: SQLModel-based data structures with validation
- **CRUD**: Generic CRUD operations with type safety
- **Migrations**: Database schema versioning with Alembic

#### 3. Business Logic Layer (`backend/services/` & `backend/jobs/`)

Core business functionality:

- **Job Processing**: Background job execution and monitoring
- **Notifications**: Multi-channel notification system  
- **Script Management**: Dynamic script loading and execution
- **Queue Management**: Priority-based job scheduling

#### 4. API Layer (`backend/routes/api/`)

External interface for applications:

- **REST Endpoints**: CRUD operations and business logic exposure
- **WebSocket Endpoints**: Real-time data streaming
- **Authentication**: Token-based API security
- **Documentation**: Automatic OpenAPI spec generation

#### 5. Presentation Layer (`backend/routes/views/` & `frontend/`)

Web user interface:

- **View Controllers**: Server-side rendering with Jinja2
- **Templates**: Component-based template structure
- **Static Assets**: Optimized CSS, JavaScript, and media files
- **Responsive Design**: Bootstrap 5-based responsive layouts

#### 6. Utility Layer (`backend/utils/`)

Utility helpers:

- **LLM Clients**: Multi-provider AI service integration
- **System Utilities**: OS-level operations and monitoring
- **Form Processing**: Request handling and validation
- **Data Transformation**: Serialization and formatting

### Data Flow Architecture

#### Request Processing Flow

1. **HTTP Request** → FastAPI router
2. **Authentication** → JWT token validation
3. **Route Handler** → Business logic execution
4. **CRUD Operations** → Database interaction
5. **Response Formation** → JSON or HTML response
6. **Response Delivery** → Client

#### Job Processing Flow

1. **Job Creation** → API endpoint or scheduler
2. **Queue Management** → Priority-based queueing
3. **Huey Consumer** → Background job pickup
4. **Job Execution** → Command/script/API execution
5. **Status Updates** → Database and WebSocket broadcasting
6. **Logging** → File-based job logs

#### WebSocket Communication Flow

1. **Client Connection** → WebSocket handshake
2. **Connection Manager** → Client registration
3. **Event Trigger** → Job status change or system event
4. **Broadcasting** → Message sent to all connected clients
5. **Client Update** → UI refresh with new data

### Database Schema

#### Core Tables

- **users**: User accounts and authentication
- **jobs**: Background job definitions and status  
- **job_schedulers**: Recurring job schedules

#### Relationships

- Users can create multiple jobs
- Schedulers generate jobs based on trigger patterns
- Jobs belong to specific queues and environments

### Scalability Considerations

#### Horizontal Scaling

- Stateless application design enables load balancing
- WebSocket connections can be distributed across instances
- Job processing can run on separate worker nodes

#### Vertical Scaling

- Connection pooling optimizes database performance
- Async/await patterns maximize resource utilization
- Configurable worker counts for CPU-bound jobs

#### Caching Strategy

- JWT tokens provide stateless authentication
- Database query optimization with SQLAlchemy
- Static asset caching with proper headers

### Security Architecture

#### Authentication & Authorization

- JWT-based stateless authentication
- Role-based access control (RBAC)
- Password hashing with bcrypt
- Token expiration and refresh mechanisms

#### Input Validation

- Pydantic model validation for all inputs
- SQL injection prevention via ORM
- HTML sanitization for user content
- CORS policy configuration

#### Audit & Monitoring

- Comprehensive request logging
- Job execution tracking
- Error reporting and alerting
- Security event monitoring

<!-- ENDSECTION -->

<!-- SECTION: 7. Glossary -->
## 7. Glossary

| Term | Definition |
| :--- | :--- |
| **vCore Framework** | The complete reusable FastAPI-based web application framework contained in the `/backend` directory, when used as package, it is contained in the `/vcore/backend` directory for the project |
| **vCore Scripts** | vCore Scripts used to help automate tasks, jobs, and other needed tasks |
| **vCore Quick Tools** | vCore Quick Tools is scaffolding allowing developers to quickly create simple tools |
| **FastAPI** | Modern Python web framework for building APIs with automatic documentation and type checking |
| **SQLModel** | Database ORM that combines SQLAlchemy and Pydantic for type-safe database operations |
| **JWT (JSON Web Token)** | Stateless authentication tokens used for API security |
| **CRUD** | Create, Read, Update, Delete - the four basic database operations |
| **Huey** | Lightweight Python job queue used for background job processing |
| **Job Queue** | Background job processing system with priority management and real-time monitoring |
| **WebSocket** | Full-duplex communication protocol enabling real-time data updates between client and server |
| **Alembic** | Database migration tool for SQLAlchemy, used to manage schema changes |
| **Pydantic** | Data validation library using Python type annotations |
| **ASGI** | Asynchronous Server Gateway Interface - the async successor to WSGI |
| **Uvicorn** | Lightning-fast ASGI server implementation |
| **Jinja2** | Modern templating engine for Python with template inheritance |
| **Bootstrap** | Popular CSS framework for responsive web design |
| **Poetry** | Modern Python dependency management and packaging tool |
| **Docker** | Containerization platform for consistent application deployment |
| **Loguru** | Advanced Python logging library with structured output |
| **OpenAPI** | Specification for REST APIs, automatically generated by FastAPI |
| **CORS** | Cross-Origin Resource Sharing - web security feature for API access |
| **OAuth2** | Industry-standard authorization framework |
| **bcrypt** | Cryptographic hash function optimized for password hashing |
| **Priority Queue** | Job queue system with five priority levels (highest to lowest) |
| **Environment Configuration** | Settings loaded from environment variables or `.env` files |
| **Session Management** | Database session handling with connection pooling |
| **Template Inheritance** | Jinja2 feature allowing templates to extend base templates |
| **Static Assets** | CSS, JavaScript, images, and other files served directly by the web server |
| **Migration** | Database schema change managed through version control |
| **Dependency Injection** | Design pattern used by FastAPI for providing dependencies to endpoints |
| **Async/Await** | Python asynchronous programming pattern for non-blocking operations |
| **Connection Pooling** | Database connection reuse mechanism for improved performance |
| **Real-time Updates** | Immediate data synchronization across connected clients |

<!-- ENDSECTION -->
