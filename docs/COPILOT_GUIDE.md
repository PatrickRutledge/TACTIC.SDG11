# TACTIC.SDG11 - Copilot Guide

## Project Context
This repository contains the development of AI agents for IBM Watson Orchestrate focusing on viewpoint exploration and debate facilitation as part of the TACTIC.SDG11 solution.

## Repository Structure
- `/adk-project/debate_agents/` - Core agent YAML files and implementation code
- `/docs/` - Project documentation including PRD and implementation guides
- `/README.md` - Main project documentation and setup instructions

## Development Workflow
1. Review and refine agent YAML configurations
2. Test agents individually in Watson Orchestrate
3. Implement and test agent handoffs
4. Document deployment process

## Current Priority Items
- [x] Create GitHub repository
- [ ] Refine agent greetings to be consistent with their roles
- [ ] Fix path issues in agent configurations
- [ ] Test agent handoffs
- [ ] Complete and validate PRD

## Agent Quick Reference

### ViewpointExplorer
- **Purpose**: Entry point for users, helps identify perspectives on topics
- **Key Files**: `optimized_viewpoint_explorer.yaml`
- **Next Steps**: Customize greeting, implement path branches

### WhiteboardAgent
- **Purpose**: Visual mapping of user viewpoints
- **Key Files**: `whiteboard_agent.yaml`
- **Next Steps**: Implement mind mapping tool integration

### ModeratorAgent
- **Purpose**: Facilitates debates between perspective agents
- **Key Files**: `moderator_agent.yaml`
- **Next Steps**: Ensure proper handoffs from ViewpointExplorer

### Perspective Agents
- **Purpose**: Represent specific viewpoints in debates
- **Key Files**: `progressive_agent.yaml`, `conservative_agent.yaml`
- **Next Steps**: Verify content and handoff mechanics

## Notes for Copilot
- Remember that the agents are part of a larger solution with a web interface
- Focus on ensuring agent configurations will work in IBM Watson Orchestrate
- Keep track of file edits in this guide for reference
