```markdown
# Debate System README

## Overview
The Public Discourse Multi-Agent Debate System is a collection of specialized AI agents designed to facilitate meaningful debates on complex topics. Each agent represents a different perspective or plays a specific role in the debate process.

## Agents
The system includes the following agents:

### Main Agents
- **DebateAgent**: General debate facilitator that presents multiple perspectives with evidence-based reasoning
- **ModeratorAgent**: Facilitates structured debates, manages speaking turns, and ensures fair representation of all perspectives
- **ViewpointExplorer**: Engages users to determine and explore their viewpoint on a chosen topic, with pathways to deeper exploration, debates, or visual mapping
- **WhiteboardAgent**: Helps users visually map and develop their viewpoints through an interactive whiteboard session

### Perspective Agents
- **ProgressivePerspectiveAgent**: Represents progressive perspectives focusing on social change and equality
- **ConservativePerspectiveAgent**: Represents traditional perspectives emphasizing values of tradition and established institutions
- **ScientificPerspectiveAgent**: Represents scientific perspectives focusing on evidence-based reasoning and data analysis
- **EconomicPerspectiveAgent**: Represents economic perspectives analyzing issues through economic principles and market dynamics

## Debate Formats
The system supports various debate formats:

- **Structured Debate**: A formal debate with clear rules, timed responses, and organized structure
- **Roundtable**: An open discussion format where agents freely contribute perspectives
- **Point-Counterpoint**: A back-and-forth format focusing on specific arguments and counter-arguments
- **ViewpointExploration**: A guided exploration of the user's own viewpoint with options for development

## Usage
To interact with the debate system:

1. Access the chat interface at http://localhost:3002/chat-lite
2. Select any of the agents from the dropdown menu
3. Start a conversation with your chosen agent

### Using the ModeratorAgent
The ModeratorAgent can facilitate full debates. Example prompts:

- "Set up a structured debate on climate change with ScientificPerspectiveAgent, EconomicPerspectiveAgent, and ProgressivePerspectiveAgent"
- "I'd like to hear different perspectives on education reform"
- "Moderate a point-counterpoint debate on technology regulation"

### Using Perspective Agents Directly
You can also engage with individual perspective agents:

- "What's the progressive perspective on universal basic income?"
- "How would a conservative approach immigration policy?"
- "What does the scientific evidence say about renewable energy?"
- "From an economic standpoint, what are the impacts of raising minimum wage?"

### Using the ViewpointExplorer
The ViewpointExplorer helps users explore their own perspectives:

- "I want to develop my viewpoint on climate change"
- "Help me articulate my thoughts on education reform"
- "I'd like to analyze my stance on technology regulation"

## ViewpointExplorer System

The ViewpointExplorer system is a specialized component that helps users:
1. Articulate and explore their viewpoints on any topic
2. Develop their perspectives through structured questioning
3. Visualize their thoughts through an interactive whiteboard session
4. Observe a debate between different perspective agents
5. Refine their thinking through guided exploration

### ViewpointExplorer Conversation Flow

1. The ViewpointExplorer initiates the conversation by asking the user about a topic of interest
2. Through a series of questions, the agent helps the user articulate their viewpoint
3. The agent summarizes the user's perspective and offers three paths:
   - Deeper exploration through more detailed questions
   - A debate session with multiple perspective agents (via ModeratorAgent)
   - A visual mapping session (via WhiteboardAgent)
4. Based on the user's choice, the conversation continues with the appropriate agent
5. Each path provides different ways for users to develop and refine their thinking

### WhiteboardAgent Capabilities

The WhiteboardAgent provides:
- Visual representation of the user's viewpoint
- Interactive refinement of viewpoint components
- Identification of connections between elements
- Gap analysis and development suggestions
- Exportable text summary of the viewpoint map

## System Components
The system includes several key components:

- **debate_system_config.json**: Main configuration for the debate system
- **debate_system_manager.py**: Script to manage and coordinate debates
- **debate_agent_core.py**: Core functionality for debate agents
- **debate_flow_patterns.py**: Defines different debate flow structures
- **chat_service_manager.py**: Manages the chat service
- **optimized_viewpoint_explorer.yaml**: Configuration for the ViewpointExplorer agent
- **whiteboard_agent.yaml**: Configuration for the WhiteboardAgent

## Implementation Details

The system is built using the Watson Orchestrate Agent Development Kit (ADK) with:
- YAML configuration files for each agent
- Context variable sharing between agents
- Conditional branching based on user responses
- Asynchronous processing for improved performance
- Timeout parameters to prevent endless loops
- Error handling for unexpected user responses

## Development
To further develop the system, you can:

1. Add new perspective agents (ethical, historical, international, etc.)
2. Enhance agent knowledge bases
3. Create new debate formats
4. Implement more sophisticated turn-taking mechanisms
5. Add support for evidence citation and fact-checking
6. Expand the WhiteboardAgent's visualization capabilities
7. Add new pathways for viewpoint exploration and development

```
