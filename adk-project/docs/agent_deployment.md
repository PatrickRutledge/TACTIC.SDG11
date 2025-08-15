# Agent Deployment Process

This document outlines the standard process for deploying agents in the TACTIC.SDG11 project.

## Prerequisites

1. Make sure your virtual environment is activated:
   ```bash
   cd /home/patrickrutledge/tactic.sdg11/adk-project
   source venv/bin/activate
   ```

2. Ensure the Orchestrate server is running:
   ```bash
   orchestrate server start -e /home/patrickrutledge/tactic.sdg11/adk-project/.env
   ```

## Deployment Options

### Option 1: Using the Deployment Script (Recommended)

The project includes a deployment script that handles the process automatically:

```bash
# Navigate to the project directory
cd /home/patrickrutledge/tactic.sdg11/adk-project

# Run the deployment script with the agent folder path
./deploy_agent.sh agents/viewpoint_discovery_agent
```

The script will:
1. Check if the agent already exists and remove it if it does
2. Import the new agent from the YAML file
3. Provide instructions for starting a chat with the agent

### Option 2: Manual Deployment

If you prefer to deploy manually, follow these steps:

1. Check if the agent already exists:
   ```bash
   orchestrate agents list
   ```

2. If it exists and you want to replace it:
   ```bash
   orchestrate agents remove -n AgentName -k native --force
   ```

3. Import the new agent:
   ```bash
   orchestrate agents import -f /path/to/agent/agent_name.yaml
   ```

## Important Notes

1. **YAML Validation Requirements**:
   - All context variables must have a `type` specified
   - Context variables should have default values (use empty strings `""` if needed)
   - Make sure validation rules are consistent with variable types

2. **Python Implementation**:
   - The Python file should be in the same directory as the YAML file
   - The Python file should have the same base name as the YAML file

3. **Testing the Deployment**:
   ```bash
   # Start a chat with the deployed agent
   orchestrate chat start -a AgentName
   ```

## Troubleshooting

- If you encounter validation errors, check the context variables in your YAML file
- Ensure all dependencies (tools, knowledge bases) referenced in your agent are already deployed
- For Python errors, check the server logs for more detailed information
