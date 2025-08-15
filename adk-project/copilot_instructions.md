```markdown
# GitHub Copilot Instructions

## Purpose
This file contains instructions for GitHub Copilot to follow when assisting with this project.

## Project Context
This project involves IBM Watson Orchestrate agents, specifically focusing on debate and viewpoint exploration capabilities.

## Collaboration Reminder
GitHub Copilot is not alone in this project - when facing complex challenges or needing specialized knowledge about Watson Orchestrate, it's encouraged to ask for help and collaborate with Watson for specific implementation details.

## Naming Conventions and Standards
- Use snake_case consistently for all agent names and file names
- Use "viewpoint_discovery_agent" as the standard name, not "explorer" or any variations
- DO NOT GET CONFUSED WITH "DISCOVERY" - If you encounter "DISCOVERY" it is related to "WATSON DISCOVERY" which is a completely different agent on a different module
- Be cautious when accessing the archive folder - it contains historical experiments with inconsistent naming

## Agent Roles and Interactions
- Define the roles of each agent, including the viewpoint_discovery_agent, whiteboard_agent, debate_agent, and forum_agent
- Determine the interactions between agents, including handoff mechanisms and context variables
- Ensure that each agent's role and interactions are clearly defined and aligned with the overall project goals

## YAML Configuration Files
- Use YAML configuration files to define the agent's behavior, conversation flows, and handoff mechanisms
- Ensure that each YAML file is well-organized, readable, and follows a consistent structure
- Use comments and annotations to explain the purpose and functionality of each section

## Python Files
- Use Python files to implement the agent's logic and interactions
- Ensure that each Python file is well-organized, readable, and follows a consistent structure
- Use comments and annotations to explain the purpose and functionality of each section

## Handoffs and Context Variables
- Define the handoff mechanisms between agents, including the context variables that are passed between agents
- Ensure that each handoff is clearly defined and aligned with the overall project goals
- Use context variables to store user responses, viewpoints, and other relevant information

## Best Practices
- Use a consistent structure for YAML configuration files and Python files
- Ensure that each file is well-organized and easy to read
- Use comments and annotations to explain the purpose and functionality of each section
- Test and validate each agent's role and interactions
- Ensure that each agent is functioning as expected and aligned with the overall project goals

## Guidelines for Agent YAML Configuration Files
- Agent name and description
- Conversation flows and handoff mechanisms
- Context variables and data storage
- Ensure that each section is clearly defined and aligned with the overall project goals

## Guidelines for Python Files
- Agent logic and interactions
- Handoff mechanisms and context variables
- Data storage and retrieval
- Ensure that each section is clearly defined and aligned with the overall project goals

## Guidelines for Handoffs and Context Variables
- Handoff mechanisms and context variables
- Data storage and retrieval
- Agent interactions and logic
- Ensure that each section is clearly defined and aligned with the overall project goals

## Folder Structure Convention
- Each agent should have its own folder with a consistent structure:
  ```
  /agent_name/
  ├── agent_name.py           # Python implementation
  ├── agent_name.yaml         # YAML configuration
  ├── agent_name_summary.md   # Main summary document (optional)
  └── agent_name_docs/        # Documentation folder
      ├── implementation_notes.md
      ├── watson_feedback.md
      └── other_documentation.md
  ```
- Keep one main summary document at the same level as the code files
- Place all detailed documentation, implementation notes, Watson feedback, and other documentation in the agent_name_docs subfolder
- This structure provides clear separation between code and documentation while keeping the main summary accessible

```
