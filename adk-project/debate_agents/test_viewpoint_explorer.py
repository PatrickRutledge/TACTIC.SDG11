#!/usr/bin/env python3
"""
ViewpointExplorer Test Script
This script tests the ViewpointExplorer agent with sample questions.
"""

import os
import json
import argparse
import requests
import time
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Base URL for the chat API
BASE_URL = "http://localhost:3000/api"  # Adjust if your API is at a different location

def get_auth_headers():
    """Get authentication headers for API requests"""
    # This is a simplified version - you may need to adjust based on your actual auth mechanism
    return {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.getenv('WO_API_KEY')}"
    }

def start_conversation(agent_name):
    """Start a new conversation with the specified agent"""
    url = f"{BASE_URL}/conversations"
    payload = {
        "agent": agent_name
    }
    
    response = requests.post(url, headers=get_auth_headers(), json=payload)
    if response.status_code == 200:
        return response.json().get("conversationId")
    else:
        print(f"Error starting conversation: {response.status_code}")
        print(response.text)
        return None

def send_message(conversation_id, message):
    """Send a message to the agent and get the response"""
    url = f"{BASE_URL}/conversations/{conversation_id}/messages"
    payload = {
        "text": message
    }
    
    response = requests.post(url, headers=get_auth_headers(), json=payload)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error sending message: {response.status_code}")
        print(response.text)
        return None

def test_basic_conversation():
    """Test a basic conversation flow with the ViewpointExplorer agent"""
    conversation_id = start_conversation("ViewpointExplorer")
    if not conversation_id:
        print("Failed to start conversation")
        return
    
    print("\n--- Testing Basic Conversation Flow ---\n")
    
    # Test questions for a basic conversation flow
    test_messages = [
        "Hello, I'd like to explore my views on climate change.",
        "I think we need to take immediate action to reduce carbon emissions.",
        "Scientific reports show rising global temperatures and extreme weather events.",
        "Those who oppose climate action often cite economic concerns, but I believe the long-term costs of inaction are greater."
    ]
    
    # Send messages and print responses
    for message in test_messages:
        print(f"\nUser: {message}")
        response = send_message(conversation_id, message)
        if response:
            agent_response = response.get("text", "No response")
            print(f"ViewpointExplorer: {agent_response}")
            # Short pause to simulate conversation flow
            time.sleep(1)
        else:
            print("Failed to get response")
    
    print("\n--- Basic Conversation Test Completed ---\n")

def test_deeper_questions_path():
    """Test the deeper questions path"""
    conversation_id = start_conversation("ViewpointExplorer")
    if not conversation_id:
        print("Failed to start conversation")
        return
    
    print("\n--- Testing Deeper Questions Path ---\n")
    
    # Initial conversation to get to the choice point
    initial_messages = [
        "I want to discuss education reform.",
        "I believe we need to focus more on critical thinking skills and less on standardized testing.",
        "My evidence is that students in countries with less testing often show better problem-solving abilities.",
        "Those who oppose this view often worry about accountability and measuring progress."
    ]
    
    for message in initial_messages:
        print(f"\nUser: {message}")
        response = send_message(conversation_id, message)
        if response:
            agent_response = response.get("text", "No response")
            print(f"ViewpointExplorer: {agent_response}")
            time.sleep(1)
        else:
            print("Failed to get response")
    
    # Choose the deeper questions path
    print("\nUser: I'd like to develop my perspective further with more detailed questions.")
    response = send_message(conversation_id, "I'd like to develop my perspective further with more detailed questions.")
    if response:
        agent_response = response.get("text", "No response")
        print(f"ViewpointExplorer: {agent_response}")
        time.sleep(1)
    else:
        print("Failed to get response")
    
    # Answer deeper questions
    deeper_responses = [
        "I value creativity, critical thinking, and individual development over standardization.",
        "As we learn more about different learning styles and personalized education, I think my view will evolve toward even more customized approaches.",
        "I would reduce the frequency of standardized tests and give teachers more autonomy."
    ]
    
    for message in deeper_responses:
        print(f"\nUser: {message}")
        response = send_message(conversation_id, message)
        if response:
            agent_response = response.get("text", "No response")
            print(f"ViewpointExplorer: {agent_response}")
            time.sleep(1)
        else:
            print("Failed to get response")
    
    print("\n--- Deeper Questions Path Test Completed ---\n")

def test_debate_handoff():
    """Test the handoff to the ModeratorAgent for a debate"""
    conversation_id = start_conversation("ViewpointExplorer")
    if not conversation_id:
        print("Failed to start conversation")
        return
    
    print("\n--- Testing Debate Handoff ---\n")
    
    # Initial conversation to get to the choice point
    initial_messages = [
        "I want to discuss universal basic income.",
        "I think it could help reduce poverty and provide economic security.",
        "Pilot programs have shown positive outcomes in terms of health and education.",
        "Critics worry about funding and potential reduction in work incentives."
    ]
    
    for message in initial_messages:
        print(f"\nUser: {message}")
        response = send_message(conversation_id, message)
        if response:
            agent_response = response.get("text", "No response")
            print(f"ViewpointExplorer: {agent_response}")
            time.sleep(1)
        else:
            print("Failed to get response")
    
    # Choose the debate path
    print("\nUser: I'd like to see different perspectives debate this topic.")
    response = send_message(conversation_id, "I'd like to see different perspectives debate this topic.")
    if response:
        agent_response = response.get("text", "No response")
        print(f"ViewpointExplorer: {agent_response}")
        
        # Check if we've been handed off to the ModeratorAgent
        if "ModeratorAgent" in agent_response or "debate" in agent_response.lower():
            print("\n--- Successfully handed off to ModeratorAgent ---")
        else:
            print("\n--- Handoff to ModeratorAgent may have failed ---")
    else:
        print("Failed to get response")
    
    print("\n--- Debate Handoff Test Completed ---\n")

def test_whiteboard_handoff():
    """Test the handoff to the WhiteboardAgent"""
    conversation_id = start_conversation("ViewpointExplorer")
    if not conversation_id:
        print("Failed to start conversation")
        return
    
    print("\n--- Testing Whiteboard Handoff ---\n")
    
    # Initial conversation to get to the choice point
    initial_messages = [
        "I want to discuss artificial intelligence ethics.",
        "I believe we need strong regulations to ensure AI is developed responsibly.",
        "We've already seen issues with bias in algorithms and privacy concerns.",
        "Some argue that too much regulation could stifle innovation."
    ]
    
    for message in initial_messages:
        print(f"\nUser: {message}")
        response = send_message(conversation_id, message)
        if response:
            agent_response = response.get("text", "No response")
            print(f"ViewpointExplorer: {agent_response}")
            time.sleep(1)
        else:
            print("Failed to get response")
    
    # Choose the whiteboard path
    print("\nUser: I'd like to engage in a whiteboard session to map out my viewpoint.")
    response = send_message(conversation_id, "I'd like to engage in a whiteboard session to map out my viewpoint.")
    if response:
        agent_response = response.get("text", "No response")
        print(f"ViewpointExplorer: {agent_response}")
        
        # Check if we've been handed off to the WhiteboardAgent
        if "WhiteboardAgent" in agent_response or "whiteboard" in agent_response.lower():
            print("\n--- Successfully handed off to WhiteboardAgent ---")
        else:
            print("\n--- Handoff to WhiteboardAgent may have failed ---")
    else:
        print("Failed to get response")
    
    print("\n--- Whiteboard Handoff Test Completed ---\n")

def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(description="Test the ViewpointExplorer agent")
    parser.add_argument('--test', choices=['basic', 'deeper', 'debate', 'whiteboard', 'all'], 
                        default='all', help='Which test to run')
    args = parser.parse_args()
    
    if args.test == 'basic' or args.test == 'all':
        test_basic_conversation()
    
    if args.test == 'deeper' or args.test == 'all':
        test_deeper_questions_path()
    
    if args.test == 'debate' or args.test == 'all':
        test_debate_handoff()
    
    if args.test == 'whiteboard' or args.test == 'all':
        test_whiteboard_handoff()

if __name__ == "__main__":
    main()
