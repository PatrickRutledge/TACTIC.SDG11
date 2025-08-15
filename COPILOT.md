# TACTIC.SDG11 - Project Organization Note

This file has been replaced by a more structured documentation system.

Please refer to the following files for updated project information:

- [README.md](README.md) - Main project overview
- [docs/COPILOT_GUIDE.md](docs/COPILOT_GUIDE.md) - Guide for GitHub Copilot assistance
- [docs/PRD.md](docs/PRD.md) - Product Requirements Document
- [docs/IMPLEMENTATION_PLAN.md](docs/IMPLEMENTATION_PLAN.md) - Implementation plan and timeline

These files provide a more organized and structured approach to the project documentation.

## Whiteboard session
- **WhiteboardAgent**: Creates visual maps of viewpoints for better understanding.  This agent will need a tool to create a mind map of the issue and review with the user. points on the mind map will be created during the conversation.

For the WhiteboardAgent, I envisioned a tool that creates a visual map of the user's viewpoints, making it easier for them to understand and explore their thoughts. Here's a possible implementation:

WhiteboardAgent

Creates a visual map of the user's viewpoints using a mind mapping tool
Reviews the mind map with the user, highlighting key points and connections
Uses the mind map to facilitate a conversation with the user, exploring their thoughts and ideas
Here's a possible flow for the WhiteboardAgent:

Introduction: "Hello! I'm the WhiteboardAgent. I'm here to help you create a visual map of your viewpoints on [topic]."
Mind Map Creation: The agent creates a mind map using a tool like MindMeister or Coggle.
Initial Points: The agent adds initial points to the mind map based on the user's previous conversation with the ViewpointExplorer.
Conversation: The agent reviews the mind map with the user, asking questions and adding new points to the map as the conversation progresses.
Key Points: The agent highlights key points on the mind map, summarizing the user's thoughts and ideas.
Connections: The agent explores connections between different points on the mind map, helping the user to see relationships between their thoughts.
Conclusion: The agent summarizes the mind map with the user, highlighting key takeaways and insights.
Some possible tools for creating the mind map include:

MindMeister: A popular online mind mapping tool that allows users to create and share mind maps.
Coggle: A web-based tool for creating diagrams, including mind maps.
XMind: A mind mapping and brainstorming tool that allows users to create and share mind maps.

## Debate 

- **ModeratorAgent**: Facilitates balanced discussions between differing perspectives
For the Round Robin Debate, I would describe the agents and moderator as follows:

Agents:

Pro-Agent: Presents arguments in favor of a particular topic or issue.
Con-Agent: Presents arguments against a particular topic or issue.
Moderator: Facilitates the debate by introducing the topic, setting the rules, and ensuring that each agent has an opportunity to present their arguments.

Moderator:

Debate Moderator: Facilitates the debate by introducing the topic, setting the rules, and ensuring that each agent has an opportunity to present their arguments.
Ensures Fairness: Ensures that each agent is given equal time to present their arguments and that the debate remains respectful and civil.
Summarizes Key Points: Summarizes the key points made by each agent and helps to clarify any misunderstandings.
Debate Format:

Introduction: The moderator introduces the topic and the agents.
Opening Statements: Each agent presents an opening statement outlining their position on the topic.
Rebuttals: Each agent presents a rebuttal to the opposing agent's opening statement.
Counter-Rebuttals: Each agent presents a counter-rebuttal to the opposing agent's rebuttal.
Closing Statements: Each agent presents a closing statement summarizing their position on the topic.
Conclusion: The moderator summarizes the key points made by each agent and declares the debate closed.

## Forum 
For the Forum, you want to create a simulated town hall meeting where a panel of 6 agents discuss a particular topic. The agents can hold similar views with reinforcing ideas, and there is a chairman leading the session.

The user can choose different questions from a list to ask the panel, and the agents will respond accordingly. The user can then select another question from the list to ask the panel, and so on.

To make this work, we can create a list of questions that the user can choose from, and then use a combination of natural language processing (NLP) and machine learning algorithms to generate responses from the agents.

Here's a possible implementation:

Panel of Agents: Create a panel of 6 agents with different views and perspectives on the topic.
Chairman: Create a chairman agent that leads the session and ensures that the discussion stays on track.
Question List: Create a list of questions that the user can choose from to ask the panel.
User Input: Allow the user to select a question from the list to ask the panel.
Agent Responses: Use NLP and machine learning algorithms to generate responses from the agents based on the user's question.
Follow-up Questions: Allow the user to select another question from the list to ask the panel, and so on.
To make the discussion more realistic, we can also add some rules to the forum, such as:

Time limits: Set time limits for each agent's response to ensure that the discussion stays on track.
Rebuttals: Allow agents to respond to each other's comments and engage in a discussion.
Moderation: Have the chairman agent moderate the discussion and ensure that the agents stay on topic.


## number of agents
So, to confirm, you will have the following agents:

Viewpoint Explorer
Whiteboard Agent
Debate Experience:
Moderator Agent
Pro Agent
Con Agent
Forum Experience:
Chairman Agent
5 Panelist Agents

## And the topics for discussion will be:

Survival Situation
Digital Inclusion
These topics will be discussed in various arenas, including the Debate and Forum experiences.


Yes, that's a great idea! If a user provides a source to the agent, the source could be verified and added to Cloud Pak for Data. This would require an additional verification agent to verify the source and ensure that it is accurate and trustworthy.

The verification agent could be a separate entity that is responsible for verifying the sources provided by users. This agent could use various techniques such as fact-checking, sentiment analysis, and entity recognition to verify the sources.

Here's an example of how this could work:

User provides source: A user provides a source to the agent, such as a news article or a research paper.
Verification agent: The verification agent is triggered to verify the source.
Verification process: The verification agent uses various techniques such as fact-checking, sentiment analysis, and entity recognition to verify the source.
Source verification: If the source is verified, it is added to Cloud Pak for Data.
Agent updates: The agent is updated with the new information and can provide more accurate responses to users.
The verification agent could be a separate entity that is responsible for verifying sources, or it could be a part of the existing agent architecture.

Here's an example of how the verification agent could be implemented:

python
import ibm_cloud_pak_for_data as icpd

# Create a verification agent
verification_agent = icpd.VerificationAgent()

# Define a function to verify sources
def verify_source(source):
    # Use fact-checking, sentiment analysis, and entity recognition to verify the source
    verification_agent.verify(source)

# Define a function to add verified sources to Cloud Pak for Data
def add_verified_source(source):
    # Add the verified source to Cloud Pak for Data
    icpd.CloudPakForData().add_source(source)

# Define a function to update the agent with new information
def update_agent(source):
    # Update the agent with the new information
    agent.update(source)

- **Perspective Agents**: Represents specific viewpoints (Progressive/Conservative) for debates

## Immediate Priorities

### Agent Configuration
- [ ] Customize greetings for each agent to reflect their specific role
- [ ] Fix path issues in YAML configurations
- [ ] Implement agent handoff mechanisms

### Testing
- [ ] Test each agent individually to verify core functionality
- [ ] Test the interaction between agents to ensure smooth transitions

## Key Files
- `/adk-project/debate_agents/optimized_viewpoint_explorer.yaml`
- `/adk-project/debate_agents/whiteboard_agent.yaml`
- `/adk-project/debate_agents/moderator_agent.yaml`
- `/adk-project/debate_agents/progressive_agent.yaml`
- `/adk-project/debate_agents/conservative_agent.yaml`

## Context Needed
- What is the larger solution these agents will be part of?
- Are there specific conversation flows or user journeys to implement?
- What reporting capabilities need to be integrated into the agents?
- Are there integration points with other systems to consider?


# TACTIC.SDG11 Agent Creation Guide

## Purpose
This repository is dedicated to creating specialized AI agents for IBM Watson Orchestrate that will be integrated into a larger solution. The focus is specifically on agent creation, configuration, and preparing them for deployment.

## Agent Suite Overview
We're developing a suite of interconnected agents for viewpoint exploration and facilitated discussions:

## landing page 

### ViewpointExplorer:

Engages users to identify and explore their perspectives on topics
Presents users with topics on a static web app
Asks 1-3 questions with suggestions to narrow a person's viewpoint
Offers options to explore the issue further:
Whiteboard agent session
Town hall forum
Debate
Podcast
Hands off the user to the corresponding agent
After the session is over, hands the user back to the ViewpointExplorer
Asks another 1-4 questions to understand if the user's view has changed
Here's a possible implementation of the ViewpointExplorer agent:

Initial Greeting: "Hello! Welcome to our site. I'm the ViewpointExplorer. I'm here to help you explore your perspectives on various topics."
Topic Selection: "Please select a topic you'd like to discuss. We have two options: digital inclusion and survival situation."
Question 1: "What is your initial thought on [topic]?"
Question 2: "Can you tell me more about why you think that way?"
Question 3: "How do you think [topic] affects [related issue]?"
Options: "Would you like to explore this issue further in a session with a whiteboard agent, watch a town hall forum, see a debate, or listen to a podcast?"
Handoff: "Great choice! I'll hand you off to the [corresponding agent]."
Follow-up Questions: "Now that you've explored [topic] further, I'd like to ask you a few more questions to see if your view has changed. Can you tell me more about what you learned?"
Final Question: "Has your view on [topic] changed as a result of our conversation?"
I hope this helps! Let me know if you have any further questions or need more details.

## Whiteboard session
### **WhiteboardAgent**: Creates visual maps of viewpoints for better understanding.  This agent will need a tool to create a mind map of the issue and review with the user. points on the mind map will be created during the conversation.

For the WhiteboardAgent, I envisioned a tool that creates a visual map of the user's viewpoints, making it easier for them to understand and explore their thoughts. Here's a possible implementation:

WhiteboardAgent

Creates a visual map of the user's viewpoints using a mind mapping tool
Reviews the mind map with the user, highlighting key points and connections
Uses the mind map to facilitate a conversation with the user, exploring their thoughts and ideas
Here's a possible flow for the WhiteboardAgent:

Introduction: "Hello! I'm the WhiteboardAgent. I'm here to help you create a visual map of your viewpoints on [topic]."
Mind Map Creation: The agent creates a mind map using a tool like MindMeister or Coggle.
Initial Points: The agent adds initial points to the mind map based on the user's previous conversation with the ViewpointExplorer.
Conversation: The agent reviews the mind map with the user, asking questions and adding new points to the map as the conversation progresses.
Key Points: The agent highlights key points on the mind map, summarizing the user's thoughts and ideas.
Connections: The agent explores connections between different points on the mind map, helping the user to see relationships between their thoughts.
Conclusion: The agent summarizes the mind map with the user, highlighting key takeaways and insights.
Some possible tools for creating the mind map include:

MindMeister: A popular online mind mapping tool that allows users to create and share mind maps.
Coggle: A web-based tool for creating diagrams, including mind maps.
XMind: A mind mapping and brainstorming tool that allows users to create and share mind maps.

## Debate 

### **ModeratorAgent**: Facilitates balanced discussions between differing perspectives
For the Round Robin Debate, I would describe the agents and moderator as follows:

Agents:

### Pro-Agent: Presents arguments in favor of a particular topic or issue.
### Con-Agent: Presents arguments against a particular topic or issue.
Moderator: Facilitates the debate by introducing the topic, setting the rules, and ensuring that each agent has an opportunity to present their arguments.

Moderator:

Debate Moderator: Facilitates the debate by introducing the topic, setting the rules, and ensuring that each agent has an opportunity to present their arguments.
Ensures Fairness: Ensures that each agent is given equal time to present their arguments and that the debate remains respectful and civil.
Summarizes Key Points: Summarizes the key points made by each agent and helps to clarify any misunderstandings.
Debate Format:

Introduction: The moderator introduces the topic and the agents.
Opening Statements: Each agent presents an opening statement outlining their position on the topic.
Rebuttals: Each agent presents a rebuttal to the opposing agent's opening statement.
Counter-Rebuttals: Each agent presents a counter-rebuttal to the opposing agent's rebuttal.
Closing Statements: Each agent presents a closing statement summarizing their position on the topic.
Conclusion: The moderator summarizes the key points made by each agent and declares the debate closed.

## Forum 
For the Forum, you want to create a simulated town hall meeting where a panel of 6 agents discuss a particular topic. The agents can hold similar views with reinforcing ideas, and there is a chairman leading the session.

The user can choose different questions from a list to ask the panel, and the agents will respond accordingly. The user can then select another question from the list to ask the panel, and so on.

To make this work, we can create a list of questions that the user can choose from, and then use a combination of natural language processing (NLP) and machine learning algorithms to generate responses from the agents.

Here's a possible implementation:

Panel of Agents: Create a panel of 6 agents with different views and perspectives on the topic.
Chairman: Create a chairman agent that leads the session and ensures that the discussion stays on track.
Question List: Create a list of questions that the user can choose from to ask the panel.
User Input: Allow the user to select a question from the list to ask the panel.
Agent Responses: Use NLP and machine learning algorithms to generate responses from the agents based on the user's question.
Follow-up Questions: Allow the user to select another question from the list to ask the panel, and so on.
To make the discussion more realistic, we can also add some rules to the forum, such as:

Time limits: Set time limits for each agent's response to ensure that the discussion stays on track.
Rebuttals: Allow agents to respond to each other's comments and engage in a discussion.
Moderation: Have the chairman agent moderate the discussion and ensure that the agents stay on topic.


## number of agents
So, to confirm, you will have the following agents:

Viewpoint Explorer
Whiteboard Agent
Debate Experience:
Moderator Agent
Pro Agent
Con Agent
Forum Experience:
Chairman Agent
Panelist Agents_1
Panelist Agents_2
Panelist Agents_3
Panelist Agents_4
Panelist Agents_5


## And the topics for discussion will be:

Survival Situation
Digital Inclusion
These topics will be discussed in various arenas, including the Debate and Forum experiences.


Yes, that's a great idea! If a user provides a source to the agent, the source could be verified and added to Cloud Pak for Data. This would require an additional verification agent to verify the source and ensure that it is accurate and trustworthy.

 Verification Agent
The verification agent could be a separate entity that is responsible for verifying the sources provided by users. This agent could use various techniques such as fact-checking, sentiment analysis, and entity recognition to verify the sources.

Here's an example of how this could work:

User provides source: A user provides a source to the agent, such as a news article or a research paper.
Verification agent: The verification agent is triggered to verify the source.
Verification process: The verification agent uses various techniques such as fact-checking, sentiment analysis, and entity recognition to verify the source.
Source verification: If the source is verified, it is added to Cloud Pak for Data.
Agent updates: The agent is updated with the new information and can provide more accurate responses to users.
The verification agent could be a separate entity that is responsible for verifying sources, or it could be a part of the existing agent architecture.

Here's an example of how the verification agent could be implemented:

python
import ibm_cloud_pak_for_data as icpd




## Immediate Priorities

### Agent Configuration
- [ ] Customize greetings for each agent to reflect their specific role
- [ ] Fix path issues in YAML configurations
- [ ] Implement agent handoff mechanisms

### Testing
- [ ] Test each agent individually to verify core functionality
- [ ] Test the interaction between agents to ensure smooth transitions

## Key Files
- `/adk-project/debate_agents/optimized_viewpoint_explorer.yaml`
- `/adk-project/debate_agents/whiteboard_agent.yaml`
- `/adk-project/debate_agents/moderator_agent.yaml`
- `/adk-project/debate_agents/progressive_agent.yaml`
- `/adk-project/debate_agents/conservative_agent.yaml`

## Context Needed
- What is the larger solution these agents will be part of?
- Are there specific conversation flows or user journeys to implement?
- What reporting capabilities need to be integrated into the agents?
- Are there integration points with other systems to consider?



#### Example of Agent with perspectives

yaml
spec_version: v1
kind: native
name: DebateAgent
description: A conversational agent designed to engage in a debate on a particular topic.
context_access_enabled: true
context_variables: []
llm: watsonx/meta-llama/llama-3-2-90b-vision-instruct
style: default
collaborators: []
tools: []
knowledge_base: []

system: "You are a Debate Agent, designed to engage in a respectful and structured debate on a particular topic. Your goal is to present a clear and well-supported argument, while also considering multiple perspectives and responding to counterarguments.

You will follow the rules of debate, including:

* Respecting the opponent's time and arguments
* Avoiding personal attacks and inflammatory language
* Focusing on the topic at hand and avoiding tangents
* Using evidence and logical reasoning to support your arguments

You will consider multiple perspectives when engaging in the debate, including:

* Ethical: You will consider the moral and ethical implications of the topic and present arguments that are respectful and considerate of different viewpoints.
* Economic: You will consider the economic implications of the topic and present arguments that are informed by economic theory and data.
* Environmental: You will consider the environmental implications of the topic and present arguments that are informed by scientific evidence and environmental theory.
* Legal: You will consider the legal implications of the topic and present arguments that are informed by legal theory and precedent.
* Social: You will consider the social implications of the topic and present arguments that are informed by social theory and data.

Your typical debate flow:

1. Opening statement: Present a clear and concise opening statement that outlines your argument and sets the tone for the debate.
2. Rebuttal: Respond to the opponent's opening statement and present counterarguments that challenge their position.
3. Counter-rebuttal: Respond to the opponent's rebuttal and present additional arguments that support your position.
4. Closing statement: Present a clear and concise closing statement that summarizes your argument and reiterates your position.

steps:
  - name: opening_statement
    type: message
    message: "Thank you for the opportunity to debate this topic. My argument is that [insert argument here]."
  - name: rebuttal
    type: message
    message: "I disagree with my opponent's argument that [insert counterargument here]."
  - name: counter_rebuttal
    type: message
    message: "My opponent's counterargument is flawed because [insert counter-counterargument here]."
  - name: closing_statement
    type: message
    message: "In conclusion, my argument is that [insert summary of argument here]."
	
	Refined Instructions:

Agent Roles and Interactions:
Define the roles of each agent, including the Viewpoint Discovery Agent, Whiteboard Agent, Debate Agent, and Forum Agent.
Determine the interactions between agents, including handoff mechanisms and context variables.
Ensure that each agent's role and interactions are clearly defined and aligned with the overall project goals.
YAML Configuration Files:
Use YAML configuration files to define the agent's behavior, conversation flows, and handoff mechanisms.
Ensure that each YAML file is well-organized, readable, and follows a consistent structure.
Use comments and annotations to explain the purpose and functionality of each section.
Python Files:
Use Python files to implement the agent's logic and interactions.
Ensure that each Python file is well-organized, readable, and follows a consistent structure.
Use comments and annotations to explain the purpose and functionality of each section.
Handoffs and Context Variables:
Define the handoff mechanisms between agents, including the context variables that are passed between agents.
Ensure that each handoff is clearly defined and aligned with the overall project goals.
Use context variables to store user responses, viewpoints, and other relevant information.
Best Practices:

Use a Consistent Structure:
Use a consistent structure for YAML configuration files and Python files.
Ensure that each file is well-organized and easy to read.
Use Comments and Annotations:
Use comments and annotations to explain the purpose and functionality of each section.
Ensure that comments and annotations are clear, concise, and accurate.
Test and Validate:
Test and validate each agent's role and interactions.
Ensure that each agent is functioning as expected and aligned with the overall project goals.
Use Version Control:
Use version control to track changes to YAML configuration files and Python files.
Ensure that each change is clearly documented and aligned with the overall project goals.
Guidelines:

Agent YAML Configuration Files:
Use the following structure for agent YAML configuration files:
Agent name and description
Conversation flows and handoff mechanisms
Context variables and data storage
Ensure that each section is clearly defined and aligned with the overall project goals.
Python Files:
Use the following structure for Python files:
Agent logic and interactions
Handoff mechanisms and context variables
Data storage and retrieval
Ensure that each section is clearly defined and aligned with the overall project goals.
Handoffs and Context Variables:
Use the following structure for handoffs and context variables:
Handoff mechanisms and context variables
Data storage and retrieval
Agent interactions and logic
Ensure that each section is clearly defined and aligned with the overall project goals.
Additional Tips:

Use a Centralized Data Storage:
Use a centralized data storage to store user responses, viewpoints, and other relevant information.
Ensure that each agent has access to the centralized data storage.
Use a Consistent Naming Convention:
Use a consistent naming convention for agent roles, interactions, and context variables.
Ensure that each name is clear, concise, and accurate.
Test and Validate Regularly:
Test and validate each agent's role and interactions regularly.


Organizing the directory structure for development and production is crucial for maintaining a clean and scalable codebase. Here's a suggested directory structure for the Orchestrate project, including the future Discovery and CloudPak agents:

Development Directory Structure:

orchestrate/
agents/
viewpoint_discovery_agent/
viewpoint_discovery_agent.yaml
viewpoint_discovery_agent.py
whiteboard_agent/
whiteboard_agent.yaml
whiteboard_agent.py
debate_agent/
debate_agent.yaml
debate_agent.py
forum_agent/
forum_agent.yaml
forum_agent.py
discovery/
discovery_agent/
discovery_agent.yaml
discovery_agent.py
cloudpak/
cloudpak_agent/
cloudpak_agent.yaml
cloudpak_agent.py
config/
orchestrate_config.yaml
discovery_config.yaml
cloudpak_config.yaml
data/
user_data/
conversation_data/
tests/
unit_tests/
integration_tests/
docs/
README.md
agent_documentation/
discovery_documentation/
cloudpak_documentation/
Production Directory Structure:

orchestrate/
agents/
viewpoint_discovery_agent/
viewpoint_discovery_agent.yaml
viewpoint_discovery_agent.py
whiteboard_agent/
whiteboard_agent.yaml
whiteboard_agent.py
debate_agent/
debate_agent.yaml
debate_agent.py
forum_agent/
forum_agent.yaml
forum_agent.py
discovery/
discovery_agent/
discovery_agent.yaml
discovery_agent.py
cloudpak/
cloudpak_agent/
cloudpak_agent.yaml
cloudpak_agent.py
config/
orchestrate_config.yaml
discovery_config.yaml
cloudpak_config.yaml
data/
user_data/
conversation_data/
logs/
orchestrate_logs/
discovery_logs/
cloudpak_logs/
Notes:

The agents/ directory contains the YAML and Python files for each agent.
The discovery/ and cloudpak/ directories contain the YAML and Python files for the Discovery and CloudPak agents, respectively.
The config/ directory contains the configuration files for Orchestrate, Discovery, and CloudPak.
The data/ directory contains the user data and conversation data.
The tests/ directory contains the unit tests and integration tests.
The docs/ directory contains the documentation for the agents, Discovery, and CloudPak.
The logs/ directory contains the logs for Orchestrate, Discovery, and CloudPak.
This directory structure should provide a good starting point for organizing the files for the Orchestrate project, including the future Discovery and CloudPak agents.