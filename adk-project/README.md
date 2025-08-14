# Multi-Perspective Debate System

This system provides a set of debate agents with different perspectives for facilitating rich, multi-faceted debates on complex topics.

## Agents

1. **SimpleDebateAgent** - A simplified agent that facilitates debates with multiple perspectives using the default style.
2. **PlannerDebateAgent** - A debate facilitator using the planner style with structured tools.
3. **ModeratorAgent** - A neutral moderator for facilitating debates between different perspective agents.
4. **ProgressivePerspectiveAgent** - An agent representing progressive perspectives in debates.
5. **ConservativePerspectiveAgent** - An agent representing traditional and conservative perspectives in debates.

## Agent Styles

Two styles of agents are provided:

- **Default Style**: Simpler to configure, doesn't require tools
- **Planner Style**: More structured, requires tools to be defined

## Issue Resolution

The original error "tools should be greater than 0" was resolved by:

1. Changing some agents from "planner" style to "default" style
2. For agents that use the "planner" style, adding appropriate tools

## Using the System

1. The agents can be accessed through the Watson Orchestrate chat interface at http://localhost:3000/
2. Use the ModeratorAgent to facilitate debates between the perspective agents
3. Each perspective agent will present arguments from their unique viewpoint

## Debate Formats

Multiple debate formats are supported:

- **Structured**: Formal debates with timed responses and organized rounds
- **Roundtable**: Open discussion format with moderation
- **Point-Counterpoint**: Back-and-forth format focusing on specific arguments

## Development

To modify or create new agents:

1. Edit or create YAML files in the `agents/` directory
2. Update `debate_agents/debate_system_config.json` to include new agents
3. Restart the service to load the updated agents
