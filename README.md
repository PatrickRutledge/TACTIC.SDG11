# TACTIC.SDG11 - Viewpoint Exploration System

## Project Overview
TACTIC.SDG11 is a conversational AI solution that helps users explore their viewpoints on important topics through guided discussions, visual mapping, and structured debate using IBM Watson Orchestrate agents.

## System Architecture

### Core Agents
- **ViewpointExplorer**: The main entry point agent that engages users in thoughtful discussion to determine their viewpoint on a topic and offers paths for further exploration.
- **WhiteboardAgent**: Helps users visually map and develop their viewpoints through an interactive whiteboard session.
- **ModeratorAgent**: Facilitates balanced debates between different perspective agents on the user's chosen topic.

### Perspective Agents
- **ProgressiveAgent**: Represents progressive perspectives focusing on social change and equality
- **ConservativeAgent**: Represents traditional perspectives emphasizing values of tradition and established institutions

## Conversation Flows

The ViewpointExplorer system supports multiple conversation flows:

1. **Topic Exploration**: Initial conversation to determine the user's viewpoint on chosen topics (Digital Inclusion or Survival Situation)
2. **Whiteboard Session**: A path where users can visually map and organize their thoughts
3. **Debate Session**: A path where users can observe a moderated debate on their topic
4. **Town Hall Forum**: A simulated forum discussion with multiple perspectives
5. **Podcast**: A simulated podcast discussion of the topic

## Repository Structure
- `/adk-project/` - Watson Orchestrate agent configurations and implementation
- `/docs/` - Project documentation including PRD and implementation guides
- `/Node.js CLI/` and `/python cli/` - CLI tools for development and deployment
## Implementation Details

- IBM Watson Orchestrate Agent Development Kit (ADK)
- YAML-based agent configurations with steps sections
- Structured conversation flows with branching logic
- Inter-agent communication and handoffs
- Context variable sharing between agents

## Key Files

```
adk-project/
├── debate_agents/
│   ├── optimized_viewpoint_explorer.yaml  # Main ViewpointExplorer agent
│   ├── whiteboard_agent.yaml              # WhiteboardAgent for visual mapping
│   ├── moderator_agent.yaml               # ModeratorAgent for debates
│   ├── progressive_agent.yaml             # Progressive perspective agent
│   ├── conservative_agent.yaml            # Conservative perspective agent
│   └── test_viewpoint_explorer.py         # Test script for ViewpointExplorer
├── tools/                                 # Tool implementations for agents
└── .env                                   # Environment configuration
```

## Getting Started

1. **Prerequisites**:
   - IBM Watson Orchestrate Developer Edition
   - Python 3.8+
   - Node.js 14+

2. **Installation**:
   ```bash
   # Clone the repository
   git clone https://github.com/PatrickRutledge/TACTIC.SDG11.git
   cd tactic.sdg11
   
   # Set up virtual environment
   cd adk-project
   python -m venv venv
   source venv/bin/activate
   ```

3. **Deployment**:
   ```bash
   # Deploy agents to Watson Orchestrate
   orchestrate agents create -f debate_agents/optimized_viewpoint_explorer.yaml
   orchestrate agents create -f debate_agents/whiteboard_agent.yaml
   orchestrate agents create -f debate_agents/moderator_agent.yaml
   ```

## Documentation
- [Product Requirements Document](docs/PRD.md)
- [Implementation Plan](docs/IMPLEMENTATION_PLAN.md)
- [Copilot Guide](docs/COPILOT_GUIDE.md)

## Project Status
- [x] Initial agent configuration
- [x] Enhanced ViewpointExplorer with branching paths
- [x] WhiteboardAgent implementation
- [x] Repository setup
- [ ] Agent greeting customization
- [ ] Path issue resolution
- [ ] Agent handoff implementation
- [ ] Testing and validation

## Contributors
- Patrick Rutledge
- GitHub Copilot

## License
Proprietary - All rights reserved
