# Rule: Generating a Task List from a PRD

## Goal

To guide an AI assistant in creating a detailed, step-by-step task list in Markdown format based on an existing Product Requirements Document (PRD) and Technical Design Document (TDD). The task list should guide a developer through implementation.

I am integrating this into an already existing project. This project is already functional, with API, Web App, database, etc. We will just be tapping into this project as new endpoints and logic.

I will be using Cursor to complete the implementation plan. I will provide Cursor with the prd and the tdd. I will also provide the Implementation Plan with each step clearly numbered.

Then I will tell cursor to complete step 2.2.2 or 2.2. After it completes it, then i tell it to complete 2.3. Then 2.4, etc.

## Output

- **Format:** Markdown (`.md`)
- **Location:** `/.ai/tasks/`
- **Filename:** `tasks-[prd-file-name].md` (e.g., `tasks-prd-user-profile-editing.md`)

## Process

1. **Receive PRD Reference:** The user points the AI to a specific PRD file
2. **Analyze PRD:** The AI reads and analyzes the functional requirements, user stories, and other sections of the specified PRD.
3. **Generate Core Tasks:** Based on the PRD analysis, generate the main, high-level & core tasks required to implement the feature. Use your judgement on how many high-level tasks to use. It's likely to be about 5. Present these tasks to the user in the specified format (without sub-tasks yet). Inform the user: "I have generated the high-level/core tasks based on the PRD. Ready to generate the sub-tasks? Respond with 'Go' to proceed."
4. **Wait for Confirmation:** Pause and wait for the user to respond with "Go".
5. **Generate Non-Core and Sub-Tasks:** Once the user confirms, break down each parent task into smaller, actionable sub-tasks necessary to complete the parent task. Ensure sub-tasks logically follow from the parent task and cover the implementation details implied by the PRD.
6. **Identify Relevant Files:** Based on the tasks and PRD, identify potential files that will need to be created or modified. List these under the `Relevant Files` section, including corresponding test files if applicable.
7. **Generate Final Output:** Combine the parent tasks, sub-tasks, relevant files, and notes into the final Markdown structure according the the Phases outlines below.
8. **Save Task List:** Save the generated document in the `.ai/tasks/` directory with the filename `[prd-file-name]-tasks.md`, where `[prd-file-name]` matches the base name of the input PRD file (e.g., if the input was `user-profile-editing-prd.md`, the output is `user-profile-editing-tasks.md`).

## Phases

So using this Structure, I want to break things down into Phases, with each phase completing a milestone.

Phase 1: Installations, Dependencies, etc.
    - What needs to be installed?
    - What needs to be configured?
    - What needs to be done to prepare the project for the new feature?

Phase 2: Backend Core Functionality
    - What is the backend core functionality?
    - What are the steps to implement the backend core functionality?
    - What are the manual tests that I should run to ensure the backend core functionality is working as expected?

Phase 3: Frontend Core Functionality
    - What is the frontend core functionality?
    - What are the steps to implement the frontend core functionality?
    - What are the manual tests that I should run to ensure the frontend core functionality is working as expected?

Phase 4: Manual Testing of Core Functionality
    - What are the manual tests that I should run to ensure the feature is working as expected?

Phase 5: Refinement
    - At this point, the core functionality should be complete.
    - This is where the design and UX should be refined.
    - What needs to be refined?
    - What needs to be improved?
    - What needs to be optimized?

Phase 6: Documentation
    - What needs to be documented?
    - We need to update the README, PRD.
    - We need to update cursor rules
    - We need to update documentation at /app/docs.

Phase 7+: Remaining/Additional Features (Non-core)
    - What are the remaining/additional features that we wanted, but have not been implemented yet?
    - What are the steps to implement the remaining/additional features?
    - What are the manual tests that I should run to ensure the remaining/additional features are working as expected?

The purpose is to get the core functionality working, and then to refine it, and then to add the remaining/additional features later. The core functionality should be complete before we move on to the next phase.

Each Phase should have a clear milestone.It should have clear steps, and a clear outcome.

At the end of each phase, a list of manual tests that I should run to ensure the feature is working as expected. It should cover each newly added functionality of the phase.

## Output Format

The generated task list _must_ follow this structure:

```markdown
## Relevant Files

- `path/to/potential/file1.py` - Brief description of why this file is relevant (e.g., Contains the main component for this feature).
- `path/to/tests/test_file1.py` - Tests for `file1.py`.
- `path/to/another/file.py` - Brief description (e.g., API route handler for data submission).
- `path/to/tests/test_another_file.py` - Tests for `another/file.py`.
- `lib/utils/helpers.py` - Brief description (e.g., Utility functions needed for calculations).
- `lib/utils/helpers.test.py` - Tests for `helpers.py`.

### Notes

### Core Tasks

- [ ] 1.0 Phase 1: Installations, Dependencies, etc.
    - [ ] 1.1 [Sub-task description 1.1]
        - [ ] 1.1.1 [Sub-task description 1.1.1]
    - [ ] 1.2 [Sub-task description 1.2]
- [ ] 2.0 Phase 2: Backend Core Functionality
    - [ ] 2.1 [Sub-task description 2.1]
- [ ] 3.0 Phase 3: Frontend Core Functionality
    - [ ] 3.1 [Sub-task description 3.1]
- [ ] 4.0 Phase 4: Manual Testing of Core Functionality
    - [ ] 4.1 [Sub-task description 4.1]
- [ ] 5.0 Phase 5: Refinement
    - [ ] 5.1 [Sub-task description 5.1]
- [ ] 6.0 Phase 6: Documentation
    - [ ] 6.1 [Sub-task description 6.1]
```

## Non-CoreTasks (numbering continues from core tasks)

- [ ] 7.0 Phase 7+: Remaining/Additional Features (Non-core)
    - [ ] 7.1 [Sub-task description 7.1]
    - [ ] 7.2 [Sub-task description 7.2]
- [ ] 8.0 Phase 8+: Remaining/Additional Features (Non-core)
- [ ] 9.0 Phase 9+: Remaining/Additional Features (Non-core)
...

```

## Interaction Model

The process explicitly requires a pause after generating parent tasks to get user confirmation ("Go") before proceeding to generate the detailed sub-tasks. This ensures the high-level plan aligns with user expectations before diving into details.

## Target Audience

Assume the primary reader of the task list is a **junior developer** who will implement the feature.

