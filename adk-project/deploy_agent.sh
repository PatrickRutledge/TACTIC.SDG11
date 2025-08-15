#!/bin/bash
# Agent deployment script for IBM Watson Orchestrate
# This script deploys an agent to the local development environment
# Usage: ./deploy_agent.sh <agent_folder>
# Example: ./deploy_agent.sh agents/viewpoint_discovery_agent

# Exit on error
set -e

# Check if an agent folder is provided
if [ -z "$1" ]; then
  echo "Error: Agent folder not provided"
  echo "Usage: ./deploy_agent.sh <agent_folder>"
  echo "Example: ./deploy_agent.sh agents/viewpoint_discovery_agent"
  exit 1
fi

AGENT_FOLDER=$1
AGENT_NAME=$(basename "$AGENT_FOLDER")
YAML_FILE="${AGENT_FOLDER}/${AGENT_NAME}.yaml"
PY_FILE="${AGENT_FOLDER}/${AGENT_NAME}.py"

# Check if YAML file exists
if [ ! -f "$YAML_FILE" ]; then
  echo "Error: YAML file not found at ${YAML_FILE}"
  exit 1
fi

# Activate virtual environment
source venv/bin/activate

echo "Deploying agent from ${YAML_FILE}..."

# Check if the agent already exists
EXISTING_AGENT=$(orchestrate agents list | grep "$AGENT_NAME" || echo "")

if [ ! -z "$EXISTING_AGENT" ]; then
  echo "Agent $AGENT_NAME already exists. Removing it first..."
  orchestrate agents remove -n "$AGENT_NAME" -k native --force
fi

# Import the agent
echo "Importing agent from ${YAML_FILE}..."
orchestrate agents import -f "$YAML_FILE"

echo "Agent deployment completed successfully!"
echo "To start a chat with this agent, run:"
echo "orchestrate chat start -a $AGENT_NAME"
