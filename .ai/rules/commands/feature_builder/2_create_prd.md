# Rule: Generate Plan and Documentation

## Goal

To guide an AI assistant in creating a detailed Product Requirements Document (PRD) in Markdown format, based on our previous discussion. The PRD should be clear, actionable, and suitable for a junior developer to understand and implement the feature.

We are at the point where we have a plan, and now you will be writing the PRD-style explanation of this entire feature.

The PRD you write, will be used by a LLM that is already familiar with the existing project we are integrating this into. You are not writing the PRD for a human, but for a LLM.

Make sure to include all the details of the feature, how it's itegrated into the existing project, and how it will work.

## Process

1. **Generate Feature Name:** Generate a feature name based on the discussion. This will be used to name related files.
1. **Use Discussion:** Use the discussion to create a PRD, ui moockup.
3. **Generate PRD:** Based on our previous discussion, generate a PRD using the structure outlined below.
4. **Save PRD:** Save the generated document as `[feature-name]-prd.md` inside the `.ai/tasks` directory.

## PRD Structure

The generated PRD should include the following sections:

1. **Introduction/Overview:** Briefly describe the feature and the problem it solves. State the goal.
2. **Goals:** List the specific, measurable objectives for this feature.
3. **User Stories:** Detail the user narratives describing feature usage and benefits.
4. **Functional Requirements:** List the specific functionalities the feature must have. Use clear, concise language (e.g., "The system must allow users to upload a profile picture."). Number these requirements.
5. **Core Functionality:** List the core functionality of the feature. This will actually be the first thing that is implemented. What are the bare minimum "core" that is needed before we can implement the rest of the features?
6. **Non-Goals (Out of Scope):** Clearly state what this feature will *not* include to manage scope.
7. **Design Considerations (Optional):** Link to mockups, describe UI/UX requirements, or mention relevant components/styles if applicable.
8. **Technical Considerations (Optional):** Mention any known technical constraints, dependencies, or suggestions (e.g., "Should integrate with the existing Auth module").
9. **Success Metrics:** How will the success of this feature be measured? (e.g., "Increase user engagement by 10%", "Reduce support tickets related to X").
10. **Open Questions:** List any remaining questions or areas needing further clarification.

## PRD Rules & Guidelines

- Make sure to list our all the requirements, and make sure to list them in a way that is easy for a junior developer to understand and implement.
- The feature list is important, make sure to list out all the features that are required.
- This PRD should be written for a LLM that is already familiar with the existing project we are integrating this into.
- This PRD should be written for a LLM, not a human.
- You are writing this for a LLM (Cursor) to use. Write it for a LLM, not a human.
- Include all the details of the feature, how it's itegrated into the existing project, and how it will work.
- Include diagrams, mermaid, etc.
- Include code examples, if applicable.
- Use the existing project structure (app/framework), (api, crud, models, logic, tasks, utils, data, services, etc.)
- Include a section on the "Core" functionality of the feature. This will actually be the first thing that is implemented. What are the bare minimum "core" that is needed before we can implement the rest of the features?

## Target Audience

Assume the primary reader of the PRD is a **junior developer**. Therefore, requirements should be explicit, unambiguous, and avoid jargon where possible. Provide enough detail for them to understand the feature's purpose and core logic.

## Output

- **Format:** Markdown (`.md`)
- **Location:** `.ai/tasks/`
- **Filename:** `[feature-name]-prd.md`

## Final instructions

1. Use the discussion to create a PRD.

## Additional Context

@docs/risa_overview.md
