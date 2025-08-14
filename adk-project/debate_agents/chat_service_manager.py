#!/usr/bin/env python
"""
Chat Service Manager

Helper script to manage the debate system chat service.
"""

import os
import sys
import subprocess
import argparse
import time

def check_docker_running():
    """Check if Docker is running."""
    try:
        result = subprocess.run(["docker", "info"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.returncode == 0
    except Exception:
        return False

def stop_chat_service():
    """Stop any running chat service containers."""
    print("Stopping any existing chat service containers...")
    try:
        subprocess.run(["docker", "stop", "docker-ui-1"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        subprocess.run(["docker", "rm", "docker-ui-1"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Existing containers stopped and removed.")
    except Exception as e:
        print(f"Error stopping containers: {e}")

def start_chat_service(port=3002):
    """Start the chat service on the specified port.
    
    Args:
        port (int): The port to run the service on.
    """
    if not check_docker_running():
        print("Error: Docker is not running. Please start Docker and try again.")
        sys.exit(1)
    
    print(f"Starting chat service on port {port}...")
    try:
        result = subprocess.run([
            "docker", "run", "-d",
            "--name", "docker-ui-1",
            "-p", f"{port}:4000",
            "-v", f"{os.getcwd()}:/home/node/app/adk-project",
            "--env", "PORT=4000",
            "--env", "HOST=0.0.0.0",
            "quay.io/ibm/watsonx-orchestrate-ui:latest"
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        if result.returncode == 0:
            container_id = result.stdout.decode('utf-8').strip()
            print(f"Chat service started successfully. Container ID: {container_id}")
            print(f"Chat service is available at: http://localhost:{port}/chat-lite")
        else:
            print(f"Error starting chat service: {result.stderr.decode('utf-8')}")
    except Exception as e:
        print(f"Error starting chat service: {e}")

def restart_chat_service(port=3002):
    """Restart the chat service.
    
    Args:
        port (int): The port to run the service on.
    """
    stop_chat_service()
    time.sleep(2)  # Give Docker a moment to clean up
    start_chat_service(port)

def main():
    """Main function to run the chat service manager."""
    parser = argparse.ArgumentParser(description="Manage the debate system chat service.")
    
    # Command subparsers
    subparsers = parser.add_subparsers(dest="command", help="Command to execute")
    
    # Start command
    start_parser = subparsers.add_parser("start", help="Start the chat service")
    start_parser.add_argument("--port", type=int, default=3002, help="Port to run the service on (default: 3002)")
    
    # Stop command
    subparsers.add_parser("stop", help="Stop the chat service")
    
    # Restart command
    restart_parser = subparsers.add_parser("restart", help="Restart the chat service")
    restart_parser.add_argument("--port", type=int, default=3002, help="Port to run the service on (default: 3002)")
    
    args = parser.parse_args()
    
    if args.command == "start":
        start_chat_service(args.port)
    elif args.command == "stop":
        stop_chat_service()
    elif args.command == "restart":
        restart_chat_service(args.port)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
