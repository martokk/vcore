# vCore Framework Cursor Rules

This directory contains comprehensive Cursor rules for working with the vCore Framework. These rules help ensure consistent patterns and best practices when developing with vCore.

## Created Rules

### 4100-4120: vCore Framework Rules

1. **4100-vcore-project-structure.mdc** - Establishes proper directory structure and file organization
2. **4101-vcore-crud-operations.mdc** - Defines BaseCRUD and BaseOrderedCRUD usage patterns
3. **4102-vcore-database-models.mdc** - Establishes SQLModel patterns with proper validation
4. **4103-vcore-api-endpoints.mdc** - Defines FastAPI endpoint structure and authentication
5. **4104-vcore-view-handlers.mdc** - Establishes web page handler patterns with templating
6. **4105-vcore-job-management.mdc** - Defines background job processing patterns
7. **4106-vcore-websocket-implementation.mdc** - Establishes real-time communication patterns
8. **4107-vcore-authentication.mdc** - Defines JWT authentication and security patterns
9. **4108-vcore-configuration.mdc** - Establishes settings and configuration management
10. **4109-vcore-template-system.mdc** - Defines Jinja2 template patterns and inheritance
11. **4110-vcore-services-logic.mdc** - Establishes service layer and business logic patterns
12. **4111-vcore-utilities.mdc** - Defines utility function organization and patterns
13. **4112-vcore-error-handling.mdc** - Establishes exception handling and error responses
14. **4113-vcore-logging.mdc** - Defines proper logging patterns and usage
15. **4114-vcore-testing.mdc** - Establishes testing patterns with fixtures and authentication
16. **4115-vcore-database-migrations.mdc** - Defines Alembic migration patterns
17. **4116-vcore-frontend-assets.mdc** - Establishes CSS/JS organization and Bootstrap integration
18. **4117-vcore-dependency-injection.mdc** - Defines FastAPI dependency patterns
19. **4118-vcore-validation-patterns.mdc** - Establishes Pydantic validation usage
20. **4119-vcore-quick-tools.mdc** - Defines Quick Tools development patterns
21. **4120-vcore-scripts-integration.mdc** - Establishes vCore Scripts patterns

## Coverage Areas

These rules comprehensively cover:

- **Architecture & Structure** - Project organization, layered architecture
- **Data Layer** - Models, CRUD operations, database migrations
- **API Layer** - REST endpoints, WebSocket connections, authentication
- **Business Logic** - Services, job processing, script execution
- **Presentation Layer** - Templates, views, frontend assets
- **Cross-cutting Concerns** - Logging, error handling, testing, validation
- **Development Workflow** - Configuration, utilities, dependency injection

## Usage

These rules will automatically be applied by Cursor when working with files matching their glob patterns. They provide:

- Consistent patterns for vCore Framework development
- Proper error handling and validation approaches
- Security best practices for authentication and data handling
- Performance guidelines for database and API operations
- Testing strategies for comprehensive coverage

## Rule Format

All rules follow the standard Cursor rule format:
- **Frontmatter** with description, globs, and alwaysApply
- **Context** section defining when to apply
- **Requirements** with actionable items
- **Examples** showing good and bad implementations
- **Critical Rules** highlighting the most important guidelines