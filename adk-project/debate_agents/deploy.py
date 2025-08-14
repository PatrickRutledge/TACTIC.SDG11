"""
Debate Agent Deployment

This script creates and deploys the Debate Agent to the IBM Watson Orchestrate environment.
"""

import os
import json
import sys
from ibm_watsonx_orchestrate.agent_builder import deploy_agent
from ibm_watsonx_orchestrate.agent_builder.models import AgentDefinition
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def deploy_debate_agent():
    """Deploy the debate agent to the Watson Orchestrate environment."""
    
    # Import our agent components
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    from debate_agent import DebateAgent
    from debate_flow import DebateFlow
    
    # Create the agent definition
    with open('debate_agent_config.json') as f:
        config = json.load(f)
    
    agent = DebateAgent(
        name=config['name'],
        description=config['description']
    )
    
    flow = DebateFlow()
    
    # Build the agent definition
    agent_definition = AgentDefinition(
        agent=agent,
        flow=flow,
        name="DebateAgent",
        description="An agent that facilitates structured debates on various topics",
    )
    
    # Deploy the agent
    deploy_result = deploy_agent(
        agent_definition=agent_definition,
        environment="local"  # or "production" for cloud deployment
    )
    
    print(f"Debate agent deployed successfully: {deploy_result}")
    return deploy_result

if __name__ == "__main__":
    deploy_debate_agent()
