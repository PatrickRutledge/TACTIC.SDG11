# TACTIC.SDG11 - Product Requirements Document

## 1. Product Overview

TACTIC.SDG11 is a conversational AI solution that helps users explore their viewpoints on important topics through guided discussions, visual mapping, and structured debate. The system uses specialized IBM Watson Orchestrate agents to facilitate different interaction modalities.

## 2. User Experience Flow

### 2.1 Entry Point
Users start on a static web app where they are greeted by the ViewpointExplorer agent.

### 2.2 Topic Selection
Two topics are available for exploration:
- Digital Inclusion
- Survival Situation

### 2.3 Initial Exploration
The ViewpointExplorer guides users through 1-3 questions to understand their initial viewpoint.

### 2.4 Exploration Options
Users can choose to:
- Work with the WhiteboardAgent for visual mapping
- Watch a town hall forum discussion
- Observe a moderated debate between different perspectives
- Listen to a podcast on the topic

### 2.5 Follow-up Assessment
After experiencing their chosen exploration option, users return to the ViewpointExplorer for 1-4 follow-up questions to assess if/how their viewpoint has evolved.

## 3. Agent Specifications

### 3.1 ViewpointExplorer Agent
**Purpose**: Initial engagement and viewpoint assessment
**Capabilities**:
- Topic introduction and question facilitation
- Handoff to specialized agents based on user choice
- Follow-up assessment of viewpoint evolution
- Friendly, neutral tone with open-ended questioning

**Key Interactions**:
```
Initial Greeting: "Hello! Welcome to our site. I'm the ViewpointExplorer. I'm here to help you explore your perspectives on various topics."
Topic Selection: "Please select a topic you'd like to discuss. We have two options: digital inclusion and survival situation."
Question 1: "What is your initial thought on [topic]?"
Question 2: "Can you tell me more about why you think that way?"
Question 3: "How do you think [topic] affects [related issue]?"
Options: "Would you like to explore this issue further in a session with a whiteboard agent, watch a town hall forum, see a debate, or listen to a podcast?"
Handoff: "Great choice! I'll hand you off to the [corresponding agent]."
Follow-up Questions: "Now that you've explored [topic] further, I'd like to ask you a few more questions to see if your view has changed. Can you tell me more about what you learned?"
Final Question: "Has your view on [topic] changed as a result of our conversation?"
```

### 3.2 WhiteboardAgent
**Purpose**: Visual mapping of user viewpoints
**Capabilities**:
- Creates mind maps representing user viewpoints
- Highlights connections between ideas
- Identifies gaps or inconsistencies
- Provides structure to abstract concepts

**Key Interactions**:
```
Introduction: "Hello! I'm the WhiteboardAgent. I'm here to help you create a visual map of your viewpoints on [topic]."
Mind Map Creation: The agent creates a mind map using visualization techniques.
Initial Points: The agent adds initial points based on the user's previous conversation.
Conversation: The agent reviews the mind map with the user, asking questions and adding new points.
Key Points: The agent highlights key points, summarizing the user's thoughts.
Connections: The agent explores connections between different points.
Conclusion: The agent summarizes with key takeaways and insights.
```

### 3.3 ModeratorAgent
**Purpose**: Facilitates balanced discussions between differing perspectives
**Capabilities**:
- Introduces debate topics and participants
- Ensures fair speaking time for different perspectives
- Summarizes key arguments
- Maintains respectful discourse

**Debate Format**:
```
Introduction: The moderator introduces the topic and the debating agents.
Opening Statements: Each perspective agent presents their opening position.
Rebuttals: Each agent responds to opposing arguments.
Counter-Rebuttals: Each agent addresses the rebuttals.
Closing Statements: Final position summary from each agent.
Conclusion: The moderator summarizes key points and closes the debate.
```

### 3.4 Perspective Agents (Progressive/Conservative)
**Purpose**: Represent specific viewpoints in debates
**Capabilities**:
- Present coherent arguments from a particular perspective
- Respond to opposing arguments with counterpoints
- Maintain consistent viewpoint throughout discussion
- Use evidence and reasoning to support positions

## 4. Technical Requirements

### 4.1 Agent Implementation
- All agents implemented as IBM Watson Orchestrate YAML configurations
- Context sharing between agents for seamless handoffs
- Proper error handling and fallback mechanisms

### 4.2 Web Integration
- Static web application for user interface
- API connections to Watson Orchestrate
- Simple interface for topic selection and agent interaction

### 4.3 Content Requirements
- Pre-defined debate content for both topics
- Visual mapping templates for WhiteboardAgent
- Town hall and podcast simulations

## 5. Success Criteria
- Seamless handoffs between agents
- Coherent user journey from initial exploration to follow-up
- Demonstrated ability to help users explore different aspects of their viewpoints
- Engaging and educational experience that encourages critical thinking
