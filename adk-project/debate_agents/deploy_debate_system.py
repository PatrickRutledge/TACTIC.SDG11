#!/usr/bin/env python3
"""
Debate System Deployment Script
This script deploys the debate system agents using the ADK.
"""

import os
import json
import yaml
import argparse
from pathlib import Path

# Get the current directory
current_dir = Path(__file__).parent.absolute()

def load_config():
    """Load the debate system configuration"""
    config_path = current_dir / "debate_system_config.json"
    with open(config_path, 'r') as f:
        return json.load(f)

def deploy_agents():
    """Deploy all agents defined in the configuration"""
    config = load_config()
    print(f"Deploying {config['system_name']}...")
    
    # Deploy moderator agent
    moderator_config = config['agents']['moderator']
    deploy_agent(moderator_config['agent_file'])
    
    # Deploy perspective agents
    for perspective in config['agents']['perspectives']:
        deploy_agent(perspective['agent_file'])
    
    print("All agents deployed successfully!")

def deploy_agent(agent_file):
    """Deploy a single agent using the ADK CLI"""
    agent_path = current_dir / agent_file
    
    # Load agent YAML to get the name for logging
    with open(agent_path, 'r') as f:
        agent_config = yaml.safe_load(f)
    
    print(f"Deploying agent: {agent_config['name']}")
    
    # Use the ADK CLI to deploy the agent
    # Replace with actual ADK CLI command syntax
    os.system(f"wxflows agent deploy --agent-path {agent_path}")
    
    print(f"Agent {agent_config['name']} deployed successfully")

def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(description="Deploy debate system agents")
    parser.add_argument("--list", action="store_true", help="List available agents without deploying")
    args = parser.parse_args()
    
    if args.list:
        config = load_config()
        print(f"Available agents in {config['system_name']}:")
        print(f"Moderator: {config['agents']['moderator']['name']}")
        print("Perspective agents:")
        for i, perspective in enumerate(config['agents']['perspectives'], 1):
            print(f"  {i}. {perspective['name']} - {perspective['description']}")
    else:
        deploy_agents()

if __name__ == "__main__":
    main()
