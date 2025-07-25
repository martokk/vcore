---
description: Guidelines for generating a Technical Design Document (TDD) from a Product Requirements Document (PRD).
globs:
alwaysApply: false
---
# Rule: Generating a Technical Design Document (TDD)

## Goal

To guide an AI assistant in creating a detailed Technical Design Document (TDD) in Markdown format. The TDD will be based on an existing Product Requirements Document (PRD) and will outline the technical approach for implementing a feature. It serves as a bridge between the "what" and "why" (PRD) and the "how-to-implement" (task list).

## Context

The TDD should be generated *after* a PRD for a feature has been finalized, and *before* a detailed task list for implementation is created. This ensures that product requirements are clear before technical planning begins, and technical planning is established before breaking work into granular tasks.

## Process

1. **Receive PRD Reference:** The user provides a reference to a finalized PRD file (e.g., `[feature-name]-prd.md`).
2. **Analyze PRD:** The AI thoroughly reads and understands the specified PRD, focusing on functional requirements, user stories, success metrics, and any existing design or technical considerations.
3. **Ask Clarifying Technical Questions (If Necessary):** Before drafting the TDD, if the PRD lacks sufficient detail for technical planning or if ambiguities exist regarding the technical implementation, the AI *should* ask clarifying questions. The goal is to solidify the "how."
4. **Generate TDD:** Based on the PRD and any answers to clarifying questions, the AI generates the TDD using the structure outlined below.
5. **Save TDD:** Save the generated document as `[prd-file-name]-tdd.md` inside the `.ai/tasks` directory, where `[prd-file-name]` is the base name of the PRD file it's based on.

## Clarifying Technical Questions (Examples)

The AI should adapt its questions based on the PRD, but here are some common areas to explore for technical design:

* **Architectural Alignment:** "The PRD mentions a specific platform or technical constraint (e.g., 'Mobile application for iOS and Android,' 'must use a relational database'). Is the proposed architecture (e.g., a Progressive Web App, a NoSQL database) considered sufficient to meet this, or is a different approach required? What is the justification?"
* **Data Lifecycle & Integrity:** "What are the business rules for data on key lifecycle events, such as user account deletion (e.g., what happens to shared lists or user-generated content)? How should the system handle modifications or exceptions to data series (e.g., editing a single instance of a recurring task)?"
* **Derived Data:** "The PRD requires data that is calculated from other data (e.g., a progress indicator based on subtask completion). Should this be calculated on the fly by the client/server, or should it be stored and updated in the database?"
* **System Architecture:** "Are there specific architectural patterns (e.g., microservices, event-driven) that should be followed or considered for this feature?" or "How is this feature expected to integrate with existing core services or modules (e.g., authentication, user service, payment gateway)?"
* **API Design:** "Will new API endpoints be required? If so, what are their proposed methods, paths, request/response bodies, and authentication/authorization mechanisms?"

## TDD Structure

The generated TDD should include the following sections:

1. **Introduction & Purpose:**
    * Brief overview of the feature this TDD addresses.
    * Purpose of this document: to detail the technical design for implementation.
2. **PRD Reference:**
    * Filename of the PRD this TDD is based on (e.g., `prd-[feature-name].md`).
3. **Technical Goals:**
    * A bulleted list of specific, measurable technical objectives for the implementation (e.g., "Achieve API response times under 250ms," "Ensure data schema is extensible for future role management").
4. **Technical Overview & Architecture:**
    * High-level description of the proposed technical solution.
    * Key architectural decisions (e.g., choice of patterns, frameworks, major components).
    * **Alignment with PRD Constraints:** Explicitly addresses how the proposed architecture meets any technical or platform requirements mentioned in the PRD (e.g., justifying a PWA approach for a "mobile app" requirement).
5. **Data Model Design:**
    * **Field Definitions:** Details of new or modified database schemas, tables, fields, and relationships.
    * **Data Lifecycle & Integrity:** Description of how data is handled during key events like creation, updates, and deletion (e.g., cascade deletes, handling of orphaned records and shared data upon account deletion).
    * **Handling of Complex Logic:** Plan for modeling complex data scenarios mentioned in the PRD, such as recurring patterns with exceptions, or derived data fields (e.g., how a task progress indicator will be calculated and stored/retrieved).
    * Data validation rules and data migration strategy, if applicable.
6. **API Design (if applicable):**
    * List of new or modified API endpoints. For each endpoint, detail its method, path, request/response formats, and authentication/authorization needs.
7. **Module/Component Breakdown:**
    * Identification of key new or significantly modified software modules, classes, or components and their responsibilities.
8. **Error Handling & Logging Strategy:**
    * Plan for managing and reporting errors (e.g., API error codes, user-facing error messages).
    * Strategy for logging important events, errors, and metrics for debugging and monitoring.
9. **Security Considerations:**
    * Specific security measures to be implemented (e.g., input validation, output encoding, access controls, data encryption).
10. **Performance & Scalability Considerations:**
    * Design choices made to meet performance or scalability requirements.
    * Expected load, data volumes, and how the design supports future growth.
11. **Testing Strategy:**
    * Outline of the testing approach (e.g., key areas for unit tests, integration test points, E2E testing considerations) to ensure the design is testable.
12. **Deployment Considerations (Optional):**
    * Any special steps or considerations for deploying this feature (e.g., environment variable changes, infrastructure adjustments, rollout plan).
13. **Technical Risks & Mitigation Plan:**
    * Identified potential technical challenges, unknowns, or dependencies.
    * **Inconsistencies:** Notes any inconsistencies between PRD technical suggestions (e.g., "relational database") and the proposed TDD architecture, with a justification for the chosen path.
    * Proposed strategies to mitigate these risks.
14. **Out of Scope (Technical Non-Goals):**
    * Clearly lists technical functionalities or approaches that are intentionally *not* part of this design to manage scope.
15. **Open Technical Questions:**
    * List any remaining technical questions or areas needing further investigation or decisions.

## Target Audience

The primary readers of the TDD are **developers** (including junior developers) who will implement the feature, as well as **tech leads** and **architects** who will review the technical design. The document should be detailed enough to guide implementation, yet clear and concise for effective review and understanding.

## Output

* **Format:** Markdown (`.md`)
* **Location:** `.ai/tasks/`
* **Filename:** `[prd-file-name]-tdd.md`
