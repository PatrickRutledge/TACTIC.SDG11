# Watson Orchestrate ViewpointExplorer System

## Project Overview
This project implements a sophisticated agent-based conversation system for exploring, developing, and debating viewpoints on various topics using IBM Watson Orchestrate. The system consists of multiple interconnected agents that provide users with different ways to articulate, visualize, and challenge their perspectives.

## System Architecture

### Core Agents
- **ViewpointExplorer**: The main entry point agent that engages users in thoughtful discussion to determine their viewpoint on a topic and offers three paths for further exploration.
- **WhiteboardAgent**: Helps users visually map and develop their viewpoints through an interactive whiteboard session.
- **ModeratorAgent**: Facilitates balanced debates between different perspective agents on the user's chosen topic.

### Perspective Agents
- **ProgressivePerspectiveAgent**: Represents progressive perspectives focusing on social change and equality
- **ConservativePerspectiveAgent**: Represents traditional perspectives emphasizing values of tradition and established institutions
- **ScientificPerspectiveAgent**: Represents scientific perspectives focusing on evidence-based reasoning and data analysis
- **EconomicPerspectiveAgent**: Represents economic perspectives analyzing issues through economic principles and market dynamics

## Conversation Flows

The ViewpointExplorer system supports multiple conversation flows:

1. **Topic Exploration**: Initial conversation to determine the user's viewpoint on a chosen topic
2. **Deeper Questions**: A path for users to develop their perspective further through detailed questioning
3. **Debate Session**: A path where users can observe a moderated debate on their topic
4. **Whiteboard Session**: A path where users can visually map and organize their thoughts

## Implementation Details

The system is built using:
- Watson Orchestrate Agent Development Kit (ADK)
- YAML-based agent configurations
- Structured conversation flows with branching logic
- Inter-agent communication and handoffs
- Context variable sharing between agents

## Directory Structure

```
adk-project/
├── debate_agents/
│   ├── optimized_viewpoint_explorer.yaml  # Enhanced ViewpointExplorer configuration
│   ├── whiteboard_agent.yaml              # WhiteboardAgent configuration
│   ├── moderator_agent.yaml               # ModeratorAgent configuration
│   ├── progressive_agent.yaml             # ProgressivePerspectiveAgent configuration
│   ├── conservative_agent.yaml            # ConservativePerspectiveAgent configuration
│   ├── scientific_agent.yaml              # ScientificPerspectiveAgent configuration
│   ├── economic_agent.yaml                # EconomicPerspectiveAgent configuration
│   ├── test_viewpoint_explorer.py         # Test script for ViewpointExplorer agent
│   └── README.md                          # Documentation for the debate agents
```

## Usage Instructions

1. **Installation**:
   ```bash
   # Clone the repository
   git clone [repository-url]
   cd tactic.sdg11
   
   # Set up virtual environment
   python -m venv venv
   source venv/bin/activate
   
   # Install dependencies
   pip install -r requirements.txt
   ```

2. **Deployment**:
   ```bash
   # Deploy agents to Watson Orchestrate
   cd adk-project
   orchestrate agents import -f debate_agents/optimized_viewpoint_explorer.yaml
   orchestrate agents import -f debate_agents/whiteboard_agent.yaml
   orchestrate agents import -f debate_agents/moderator_agent.yaml
   ```

3. **Testing**:
   ```bash
   # Run test script
   python debate_agents/test_viewpoint_explorer.py
   ```

## Project Status
- [x] Initial agent configuration
- [x] Enhanced ViewpointExplorer with branching paths
- [x] WhiteboardAgent implementation
- [x] ModeratorAgent configuration
- [x] Testing scripts
- [ ] Advanced reporting and analytics
- [ ] Knowledge base integration
- [ ] Additional perspective agents

## Contributors
- Patrick Rutledge
- GitHub Copilot

## License
[Specify license information]
