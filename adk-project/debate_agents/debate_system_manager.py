#!/usr/bin/env python
"""
Debate System Manager

This script helps manage and coordinate interactions between multiple debate agents.
"""

import os
import json
import sys
from pathlib import Path
import subprocess
import argparse

# Define the base path
BASE_PATH = Path(os.path.dirname(os.path.abspath(__file__)))
PROJECT_PATH = BASE_PATH.parent

class DebateSystemManager:
    """Manager for the multi-agent debate system."""
    
    def __init__(self):
        self.config_path = BASE_PATH / "debate_system_config.json"
        self.load_config()
        
    def load_config(self):
        """Load the debate system configuration."""
        try:
            with open(self.config_path, 'r') as f:
                self.config = json.load(f)
            print(f"Loaded configuration for {self.config['system_name']}")
        except Exception as e:
            print(f"Error loading configuration: {e}")
            sys.exit(1)
    
    def list_agents(self):
        """List all available debate agents."""
        print("\nAvailable Agents:")
        print(f"Moderator: {self.config['agents']['moderator']['name']}")
        print("\nPerspective Agents:")
        for agent in self.config['agents']['perspectives']:
            print(f"- {agent['name']}: {agent['description']}")
    
    def list_debate_formats(self):
        """List all available debate formats."""
        print("\nAvailable Debate Formats:")
        for name, format_info in self.config['debate_formats'].items():
            print(f"- {name}: {format_info['description']}")
    
    def list_topic_categories(self):
        """List all available topic categories."""
        print("\nAvailable Topic Categories:")
        for category in self.config['topics']['categories']:
            print(f"- {category}")
    
    def start_chat_with_agent(self, agent_name):
        """Start a chat with a specific agent."""
        # This would integrate with the Watson Orchestrate chat interface
        print(f"\nStarting chat with {agent_name}...")
        # Placeholder for the actual implementation
        print(f"Chat with {agent_name} can be accessed at http://localhost:3002/chat-lite")
        print(f"Select '{agent_name}' from the agent dropdown.")
    
    def setup_debate(self, topic, format_name, perspectives):
        """Set up a debate on a specific topic with selected perspectives."""
        if format_name not in self.config['debate_formats']:
            print(f"Error: Format '{format_name}' not found.")
            return
        
        # Validate perspectives
        valid_perspectives = [p['name'] for p in self.config['agents']['perspectives']]
        for p in perspectives:
            if p not in valid_perspectives:
                print(f"Warning: Perspective '{p}' not found in configuration.")
        
        print(f"\nSetting up {format_name} debate on topic: {topic}")
        print(f"Using moderator: {self.config['agents']['moderator']['name']}")
        print(f"With perspectives: {', '.join(perspectives)}")
        
        # Placeholder for actual debate setup logic
        print("\nDebate setup complete. Access at http://localhost:3002/chat-lite")
        print(f"Select '{self.config['agents']['moderator']['name']}' from the agent dropdown.")
        print("Send the following message to start:")
        print(f"'Set up a {format_name} debate on {topic} with {', '.join(perspectives)}'")

def main():
    """Main function to run the debate system manager."""
    parser = argparse.ArgumentParser(description="Manage the multi-agent debate system.")
    subparsers = parser.add_subparsers(dest="command", help="Command to execute")
    
    # List agents command
    subparsers.add_parser("list-agents", help="List all available debate agents")
    
    # List formats command
    subparsers.add_parser("list-formats", help="List all available debate formats")
    
    # List topics command
    subparsers.add_parser("list-topics", help="List all available topic categories")
    
    # Chat with agent command
    chat_parser = subparsers.add_parser("chat", help="Start a chat with a specific agent")
    chat_parser.add_argument("agent_name", help="Name of the agent to chat with")
    
    # Setup debate command
    debate_parser = subparsers.add_parser("setup-debate", help="Set up a debate")
    debate_parser.add_argument("topic", help="The debate topic")
    debate_parser.add_argument("format", help="The debate format")
    debate_parser.add_argument("perspectives", nargs="+", help="Perspectives to include")
    
    args = parser.parse_args()
    manager = DebateSystemManager()
    
    if args.command == "list-agents":
        manager.list_agents()
    elif args.command == "list-formats":
        manager.list_debate_formats()
    elif args.command == "list-topics":
        manager.list_topic_categories()
    elif args.command == "chat":
        manager.start_chat_with_agent(args.agent_name)
    elif args.command == "setup-debate":
        manager.setup_debate(args.topic, args.format, args.perspectives)
    else:
        # If no command is provided, show system info and available commands
        print(f"\n{manager.config['system_name']} v{manager.config['version']}")
        print(f"{manager.config['description']}")
        print("\nAvailable commands:")
        print("  list-agents     List all available debate agents")
        print("  list-formats    List all available debate formats")
        print("  list-topics     List all available topic categories")
        print("  chat            Start a chat with a specific agent")
        print("  setup-debate    Set up a debate")
        print("\nUse --help for more information on each command.")

if __name__ == "__main__":
    main()
