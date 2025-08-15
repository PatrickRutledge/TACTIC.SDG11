# Questions for Watson on viewpoint_discovery_agent Optimization

Thank you for your review and suggestions for our viewpoint_discovery_agent. We have several questions and areas where we'd appreciate your further guidance:

## Context Variables

1. What best practices do you recommend for making context variables more robust and less fragile?
2. Could you provide examples of validation or default value handling for context variables?
3. For complex user responses that might not fit neatly into string variables, what approaches do you recommend?
4. Are there specific context variables beyond those already defined that you think would be particularly valuable?

## Edge Case Handling

1. Could you provide an example of how to structure a dedicated section for edge case handling in the YAML file?
2. What are the most common edge cases we should prepare for with this type of conversational agent?
3. How should we handle scenarios where the user provides information not known to the agent?
4. What's the best approach for handling a user who frequently changes topics or goes off-topic?

## Handoff Mechanisms

1. Could you provide a complete example of a robust handoff implementation including error handling?
2. What specific parameters should be included in all handoffs for consistency?
3. How do we implement return paths from handoff destinations back to the viewpoint_discovery_agent?
4. How should we handle timeouts or connection issues during handoffs?
5. What's the recommended approach for preparing users for handoffs to maintain a smooth experience?

## Error Handling

1. What specific error handling patterns work best in Watson Orchestrate YAML files?
2. Could you provide examples of graceful recovery from common error scenarios?
3. How detailed should error messages be for end users vs. logging for administrators?

## System Prompt Optimization

1. What additional guidance should we include in the system prompt to better handle edge cases?
2. How can we enhance the system prompt to maintain consistent agent personality across all scenarios?

## Additional Features

1. Could you elaborate on the verification_agent concept for fact-checking?
2. What are some examples of advanced features we might consider adding in future iterations?

We appreciate any code examples, templates, or patterns you can share that demonstrate best practices for these areas.


### Watsons Response to Github Copilot
I'm glad to hear that my previous suggestions were helpful. I'll do my best to provide detailed answers to your developer's questions.

Context Variables

Best practices for making context variables more robust and less fragile:
Use clear and descriptive names for context variables.
Define context variables at the top level of the YAML file to make them easily accessible.
Use default values for context variables to handle cases where the user doesn't provide a value.
Validate user input for context variables to ensure they are in the expected format.
Examples of validation or default value handling for context variables:
Use the default keyword to set a default value for a context variable.
Use the validate keyword to validate user input for a context variable.
Use conditional statements to handle cases where the user doesn't provide a value for a context variable.
Approaches for handling complex user responses that might not fit neatly into string variables:
Use arrays or objects to store complex user responses.
Use the parse keyword to parse user input into a specific format.
Use conditional statements to handle cases where the user provides a complex response.
Additional context variables that might be valuable:
user_id: a unique identifier for the user.
conversation_id: a unique identifier for the conversation.
topic: the current topic of conversation.
viewpoint: the user's viewpoint on the topic.
Edge Case Handling

Example of how to structure a dedicated section for edge case handling in the YAML file:
Create a separate section in the YAML file for edge case handling.
Use conditional statements to handle specific edge cases.
Use error handling patterns to handle unexpected errors.
Most common edge cases to prepare for:
User provides invalid input.
User changes topic or goes off-topic.
User provides information not known to the agent.
User experiences a technical issue.
Handling scenarios where the user provides information not known to the agent:
Use the unknown keyword to handle cases where the user provides unknown information.
Use conditional statements to handle cases where the user provides unexpected information.
Handling a user who frequently changes topics or goes off-topic:
Use the topic context variable to track the current topic of conversation.
Use conditional statements to handle cases where the user changes topic or goes off-topic.
Handoff Mechanisms

Complete example of a robust handoff implementation including error handling:
Use the handoff keyword to implement a handoff.
Use error handling patterns to handle unexpected errors during the handoff.
Use conditional statements to handle cases where the handoff fails.
Specific parameters to include in all handoffs for consistency:
agent: the agent to hand off to.
topic: the current topic of conversation.
viewpoint: the user's viewpoint on the topic.
evidence: any evidence or examples provided by the user.
Implementing return paths from handoff destinations back to the viewpoint_discovery_agent:
Use the return keyword to implement a return path.
Use conditional statements to handle cases where the user returns from a handoff.
Handling timeouts or connection issues during handoffs:
Use error handling patterns to handle unexpected errors during the handoff.
Use conditional statements to handle cases where the handoff times out or experiences a connection issue.
Error Handling

Specific error handling patterns that work best in Watson Orchestrate YAML files:
Use the try-catch pattern to handle unexpected errors.
Use the error keyword to handle specific error scenarios.
Examples of graceful recovery from common error scenarios:
Use the recover keyword to recover from an error.
Use conditional statements to handle cases where an error occurs.
Detail level of error messages for end users vs. logging for administrators:
Use the error keyword to log error messages for administrators.
Use the message keyword to display error messages to end users.
System Prompt Optimization

Additional guidance to include in the system prompt to better handle edge cases:
Use the system keyword to define a system prompt.
Use conditional statements to handle cases where the user provides unexpected input.
Enhancing the system prompt to maintain consistent agent personality across all scenarios:
Use the personality keyword to define the agent's personality.
Use conditional statements to handle cases where the user interacts with the agent in different ways.
Additional Features

Elaboration on the verification_agent concept for fact-checking:
Use the verification_agent keyword to implement a verification agent.
Use conditional statements to handle cases where the user provides information that needs to be verified.
Examples of advanced features to consider adding in future iterations:
Use the advanced keyword to define advanced features.
Use conditional statements to handle cases where the user interacts with the agent in different ways.
I hope this helps! Let me know if you have any further questions or need additional assistance.


# Follow-up Questions for Watson

Thank you for your comprehensive answers. To help us implement these recommendations effectively, we'd appreciate some specific code examples in Watson Orchestrate YAML format:

## Context Variables - Implementation Examples

Could you provide a concrete example of context variable validation and default handling in Watson Orchestrate YAML? For instance:

```yaml
# Example of robust context variable handling with validation and defaults
context_variables:
  - name: topic
    description: "The topic that the user wants to discuss"
    type: string
    default: "sustainability"  # Is this syntax correct for defaults?
    validation: ???  # What's the correct syntax for validation?
```

## Edge Case Handling - YAML Structure

Could you provide a complete YAML example showing the recommended structure for edge case handling? Particularly:

```yaml
# Example of edge case handling section
steps:
  # ... regular conversation flow ...
  
  # How should edge case handling be structured?
  - name: handle_topic_change
    type: ???
    condition: ???
    # What's the correct syntax for detecting and handling a topic change?
```

## Handoff Implementation

Could you provide a complete handoff example with error handling that shows:
1. The syntax for preparing a handoff
2. The actual handoff with all parameters
3. Error handling if handoff fails
4. Return path implementation

```yaml
# Example of complete handoff with error handling
steps:
  - name: prepare_handoff
    type: ???
    # What's the syntax for preparing a handoff?
  
  - name: execute_handoff
    type: ???
    # What's the complete handoff syntax with error handling?
  
  - name: handle_failed_handoff
    type: ???
    # How do we detect and handle a failed handoff?
  
  - name: handle_return_from_handoff
    type: ???
    # How do we implement a return path from a handoff?
```

## Error Handling - Try/Catch Example

Could you provide a complete try/catch example in Watson Orchestrate YAML?

```yaml
# Example of try/catch pattern
steps:
  - name: try_operation
    type: ???
    # What's the syntax for a try block?
  
  - name: catch_error
    type: ???
    # What's the syntax for a catch block?
  
  - name: recover_from_error
    type: ???
    # What's the syntax for recovering from an error?
```

These specific code examples would greatly help us implement your recommendations correctly.


## Watsons response to Github Copilot

watsonx
12:34 PM
I'd be happy to provide specific code examples in Watson Orchestrate YAML format to help you implement the recommendations effectively.

Context Variables - Implementation Examples

Here's a concrete example of context variable validation and default handling in Watson Orchestrate YAML:

yaml
context_variables:
  - name: topic
    description: "The topic that the user wants to discuss"
    type: string
    default: "sustainability"
    validation:
      - type: string
      - required: true
      - pattern: "^[a-zA-Z0-9_]+$"
In this example, the topic context variable has a default value of "sustainability", and it's validated to ensure that it's a string that matches the pattern ^[a-zA-Z0-9_]+$.

Edge Case Handling - YAML Structure

Here's a complete YAML example showing the recommended structure for edge case handling:

yaml
steps:
  # ... regular conversation flow ...
  - name: handle_topic_change
    type: condition
    condition:
      - type: topic_change
      - topic: "{{ context.topic }}"
    then:
      - name: ask_topic_change_question
        type: question
        question: "You've changed the topic. Would you like to discuss {{ context.topic }}?"
In this example, the handle_topic_change step is a condition that checks if the topic has changed, and if so, it asks a question to confirm the topic change.

Handoff Implementation

Here's a complete handoff example with error handling that shows:

The syntax for preparing a handoff
The actual handoff with all parameters
Error handling if handoff fails
Return path implementation
yaml
steps:
  - name: prepare_handoff
    type: message
    message: "I'm going to hand you off to another agent. Please wait."
  - name: execute_handoff
    type: handoff
    agent: "another_agent"
    topic: "{{ context.topic }}"
    viewpoint: "{{ context.viewpoint }}"
    evidence: "{{ context.evidence }}"
    maxTimeoutMinutes: 30
    error:
      - name: handle_failed_handoff
        type: message
        message: "Sorry, the handoff failed. Please try again."
  - name: handle_return_from_handoff
    type: return
    agent: "another_agent"
    topic: "{{ context.topic }}"
    viewpoint: "{{ context.viewpoint }}"
    evidence: "{{ context.evidence }}"
In this example, the prepare_handoff step prepares the user for the handoff, the execute_handoff step performs the actual handoff with error handling, and the handle_return_from_handoff step implements the return path from the handoff.

Error Handling - Try/Catch Example

Here's a complete try/catch example in Watson Orchestrate YAML:

yaml
steps:
  - name: try_operation
    type: try
    steps:
      - name: perform_operation
        type: message
        message: "I'm going to perform an operation."
      - name: handle_success
        type: message
        message: "The operation was successful."
    catch:
      - name: catch_error
        type: catch
        error:
          - name: handle_error
            type: message
            message: "An error occurred. Please try again."
      - name: recover_from_error
        type: recover
        steps:
          - name: ask_recovery_question
            type: question
            question: "Would you like to try again?"
In this example, the try_operation step tries to perform an operation, and if it fails, it catches the error and handles it with a message. The recover_from_error step recovers from the error by asking a question to the user.


Your updated YAML file looks great! You've added a lot of functionality to the viewpoint_discovery_agent, including the ability to explore different perspectives and hand off to other agents.

Here are a few suggestions for further improvement:

Consider adding more context variables to store the user's responses and preferences. This will help you to personalize the conversation and provide more relevant information to the user.
You may want to add more steps to the conversation flow to handle different scenarios and edge cases. For example, you could add a step to handle the case where the user provides a new fact that is not available to the discovery agent.
Consider adding more handoff mechanisms to allow the user to switch between different agents and conversation flows. This will provide more flexibility and allow the user to explore different topics and perspectives.
You may want to add more error handling to handle cases where the user provides invalid or unexpected input. This will help to prevent the conversation from breaking and provide a better user experience.
Overall, your YAML file is well-structured and easy to follow. You've done a great job of defining the conversation flow and the different steps and handoffs. With a few more tweaks and additions, you'll have a robust and effective viewpoint_discovery_agent that can provide valuable insights and information to users.

Here is an updated version of your YAML file with some additional suggestions and improvements:

yaml
spec_version: v1
kind: native
name: viewpoint_discovery_agent
description: A conversational agent designed to engage users in a discussion to determine their viewpoint on a particular topic.
context_access_enabled: true
context_variables:
  - name: topic
    description: The topic that the user wants to discuss
    type: string
  - name: viewpoint
    description: The user's viewpoint on the topic
    type: string
  - name: evidence
    description: Evidence or examples that support the user's viewpoint
    type: string
  - name: clarification
    description: Clarification of the user's viewpoint
    type: string
  - name: selected_perspective
    description: The perspective the user wants to explore the topic from
    type: string
  - name: new_fact
    description: A new fact provided by the user that is not available to the discovery agent
    type: string

llm: watsonx/meta-llama/llama-3-2-90b-vision-instruct
style: default
collaborators: []
tools: []
knowledge_base: []

system: "You are the viewpoint_discovery_agent, a conversational agent designed to engage users in thoughtful discussion to determine their viewpoint on various topics. Your approach is friendly, neutral, and non-judgmental. You use a curious and inquiring tone, with simple and clear language that avoids technical jargon. Your questioning style is open-ended and probing, encouraging users to share their thoughts and opinions. Your responses are brief and concise, summarizing the user's viewpoint and asking follow-up questions."

steps:
  - name: introduction
    type: message
    message: "Hello! I'm here to help you explore your thoughts and opinions on a particular topic. What topic would you like to discuss today?"
    async: true

  - name: capture_topic
    type: question
    question: "Could you please share what topic you'd like to explore?"
    async: true

  - name: initial_viewpoint
    type: question
    question: "That's an interesting topic. What are your initial thoughts or viewpoints on {{ context.topic }}?"
    async: true

  - name: viewpoint_prompt
    type: prompt
    prompt: "Please share your perspective on this topic."
    default: "I'd love to hear more about your perspective on this topic. Could you share a bit more detail?"

  - name: explore_reasoning
    type: message
    message: "Thank you for sharing your perspective. I'd like to understand more about your reasoning. What experiences, values, or information have shaped your viewpoint on this topic?"

  - name: evidence_question
    type: question
    question: "What evidence or examples would you point to that support your viewpoint?"

  - name: evidence_prompt
    type: prompt
    prompt: "Please share any evidence, examples, or reasoning that supports your viewpoint."
    default: "Even a simple example or personal experience that shaped your view would be helpful."

  - name: perspective_exploration
    type: question
    question: "Would you be interested in exploring this topic from a specific perspective? This could help deepen your understanding."
    options:
      - Economic Perspective
      - Social Perspective
      - Ethical Perspective
      - Legal Perspective
      - Environmental Perspective
      - No thanks, continue with my own perspective

  - name: analyze_perspective
    type: message
    message: "Let's analyze the issue from the {{ context.selected_perspective }} perspective."

  - name: perspective_analysis
    type: question
    question: "How might someone thinking primarily from a {{ context.selected_perspective }} perspective view this issue differently than you do?"

  - name: counterarguments
    type: message
    message: "I appreciate you sharing those points. Have you considered any counterarguments or alternative perspectives on this topic? What might someone with a different viewpoint say?"

  - name: summary
    type: message
    message: "Let me summarize what I understand about your viewpoint so far: You believe that {{ context.topic }} is important, and your perspective includes {{ context.viewpoint }}. You've supported this with {{ context.evidence }}. Is this an accurate summary of your position?"

  - name: summary_confirmation
    type: question
    question: "Is this summary accurate? If not, what would you like to clarify or add?"

  - name: next_steps_introduction
    type: message
    message: "Now that we have a good understanding of your viewpoint on {{ context.topic }}, I'd like to offer some options for how we can proceed."

  - name: next_steps
    type: question
    question: "Would you like to: 1) Develop your perspective further with more detailed questions, 2) See how different agents might debate this topic from various perspectives, or 3) Engage in a whiteboard session where we can visually map out and develop your viewpoint?"

  - name: next_steps_prompt
    type: prompt
    prompt: "Please choose option 1, 2, or 3, or let me know if you'd prefer something else."
    default: "I didn't quite understand your response. Could you please choose one of the options or provide more information?"

  - name: new_fact
    type: question
    question: "You've provided a new fact that is not available to me. Would you like me to verify this information using a verification agent?"

  - name: verification_agent
    type: handoff
    agent: verification_agent
    topic: "{{ context.topic }}"
    viewpoint: "{{ context.viewpoint }}"
    evidence: "{{ context.evidence }}"
    maxTimeoutMinutes: 30

  - name: handoff_to_debate
    type: handoff
    agent: debate_agent
    topic: "{{ context.topic }}"
    viewpoint: "{{ context.viewpoint }}"
    evidence: "{{ context.evidence }}"
    maxTimeoutMinutes: 30

  - name: handoff_to_whiteboard
    type: handoff
    agent: whiteboard_agent
    topic: "{{ context.topic }}"
    viewpoint: "{{ context.viewpoint }}"
    evidence: "{{ context.evidence }}"
    maxTimeoutMinutes: 30
    # Follow-up Questions for Watson

Thank you for your comprehensive answers. To help us implement these recommendations effectively, we'd appreciate some specific code examples in Watson Orchestrate YAML format:

## Context Variables - Implementation Examples

Could you provide a concrete example of context variable validation and default handling in Watson Orchestrate YAML? For instance:

```yaml
# Example of robust context variable handling with validation and defaults
context_variables:
  - name: topic
    description: "The topic that the user wants to discuss"
    type: string
    default: "sustainability"  # Is this syntax correct for defaults?
    validation: ???  # What's the correct syntax for validation?
```

## Edge Case Handling - YAML Structure

Could you provide a complete YAML example showing the recommended structure for edge case handling? Particularly:

```yaml
# Example of edge case handling section
steps:
  # ... regular conversation flow ...
  
  # How should edge case handling be structured?
  - name: handle_topic_change
    type: ???
    condition: ???
    # What's the correct syntax for detecting and handling a topic change?
```

## Handoff Implementation

Could you provide a complete handoff example with error handling that shows:
1. The syntax for preparing a handoff
2. The actual handoff with all parameters
3. Error handling if handoff fails
4. Return path implementation

```yaml
# Example of complete handoff with error handling
steps:
  - name: prepare_handoff
    type: ???
    # What's the syntax for preparing a handoff?
  
  - name: execute_handoff
    type: ???
    # What's the complete handoff syntax with error handling?
  
  - name: handle_failed_handoff
    type: ???
    # How do we detect and handle a failed handoff?
  
  - name: handle_return_from_handoff
    type: ???
    # How do we implement a return path from a handoff?
```

## Error Handling - Try/Catch Example

Could you provide a complete try/catch example in Watson Orchestrate YAML?

```yaml
# Example of try/catch pattern
steps:
  - name: try_operation
    type: ???
    # What's the syntax for a try block?
  
  - name: catch_error
    type: ???
    # What's the syntax for a catch block?
  
  - name: recover_from_error
    type: ???
    # What's the syntax for recovering from an error?
```

These specific code examples would greatly help us implement your recommendations correctly.


## Watsons response to Github Copilot

watsonx
12:34 PM
I'd be happy to provide specific code examples in Watson Orchestrate YAML format to help you implement the recommendations effectively.

Context Variables - Implementation Examples

Here's a concrete example of context variable validation and default handling in Watson Orchestrate YAML:

yaml
context_variables:
  - name: topic
    description: "The topic that the user wants to discuss"
    type: string
    default: "sustainability"
    validation:
      - type: string
      - required: true
      - pattern: "^[a-zA-Z0-9_]+$"
In this example, the topic context variable has a default value of "sustainability", and it's validated to ensure that it's a string that matches the pattern ^[a-zA-Z0-9_]+$.

Edge Case Handling - YAML Structure

Here's a complete YAML example showing the recommended structure for edge case handling:

yaml
steps:
  # ... regular conversation flow ...
  - name: handle_topic_change
    type: condition
    condition:
      - type: topic_change
      - topic: "{{ context.topic }}"
    then:
      - name: ask_topic_change_question
        type: question
        question: "You've changed the topic. Would you like to discuss {{ context.topic }}?"
In this example, the handle_topic_change step is a condition that checks if the topic has changed, and if so, it asks a question to confirm the topic change.

Handoff Implementation

Here's a complete handoff example with error handling that shows:

The syntax for preparing a handoff
The actual handoff with all parameters
Error handling if handoff fails
Return path implementation
yaml
steps:
  - name: prepare_handoff
    type: message
    message: "I'm going to hand you off to another agent. Please wait."
  - name: execute_handoff
    type: handoff
    agent: "another_agent"
    topic: "{{ context.topic }}"
    viewpoint: "{{ context.viewpoint }}"
    evidence: "{{ context.evidence }}"
    maxTimeoutMinutes: 30
    error:
      - name: handle_failed_handoff
        type: message
        message: "Sorry, the handoff failed. Please try again."
  - name: handle_return_from_handoff
    type: return
    agent: "another_agent"
    topic: "{{ context.topic }}"
    viewpoint: "{{ context.viewpoint }}"
    evidence: "{{ context.evidence }}"
In this example, the prepare_handoff step prepares the user for the handoff, the execute_handoff step performs the actual handoff with error handling, and the handle_return_from_handoff step implements the return path from the handoff.

Error Handling - Try/Catch Example

Here's a complete try/catch example in Watson Orchestrate YAML:

yaml
steps:
  - name: try_operation
    type: try
    steps:
      - name: perform_operation
        type: message
        message: "I'm going to perform an operation."
      - name: handle_success
        type: message
        message: "The operation was successful."
    catch:
      - name: catch_error
        type: catch
        error:
          - name: handle_error
            type: message
            message: "An error occurred. Please try again."
      - name: recover_from_error
        type: recover
        steps:
          - name: ask_recovery_question
            type: question
            question: "Would you like to try again?"
In this example, the try_operation step tries to perform an operation, and if it fails, it catches the error and handles it with a message. The recover_from_error step recovers from the error by asking a question to the user.

Your updated YAML file looks great! You've added a lot of functionality to the viewpoint_discovery_agent, including the ability to explore different perspectives and hand off to other agents.

Here are a few suggestions for further improvement:

Consider adding more context variables to store the user's responses and preferences. This will help you to personalize the conversation and provide more relevant information to the user.
You may want to add more steps to the conversation flow to handle different scenarios and edge cases. For example, you could add a step to handle the case where the user provides a new fact that is not available to the discovery agent.
Consider adding more handoff mechanisms to allow the user to switch between different agents and conversation flows. This will provide more flexibility and allow the user to explore different topics and perspectives.
You may want to add more error handling to handle cases where the user provides invalid or unexpected input. This will help to prevent the conversation from breaking and provide a better user experience.
Overall, your YAML file is well-structured and easy to follow. You've done a great job of defining the conversation flow and the different steps and handoffs. With a few more tweaks and additions, you'll have a robust and effective viewpoint_discovery_agent that can provide valuable insights and information to users.

Here is an updated version of your YAML file with some additional suggestions and improvements:

yaml
spec_version: v1
kind: native
name: viewpoint_discovery_agent
description: A conversational agent designed to engage users in a discussion to determine their viewpoint on a particular topic.
context_access_enabled: true
context_variables:
  - name: topic
    description: The topic that the user wants to discuss
    type: string
  - name: viewpoint
    description: The user's viewpoint on the topic
    type: string
  - name: evidence
    description: Evidence or examples that support the user's viewpoint
    type: string
  - name: clarification
    description: Clarification of the user's viewpoint
    type: string
  - name: selected_perspective
    description: The perspective the user wants to explore the topic from
    type: string
  - name: new_fact
    description: A new fact provided by the user that is not available to the discovery agent
    type: string

llm: watsonx/meta-llama/llama-3-2-90b-vision-instruct
style: default
collaborators: []
tools: []
knowledge_base: []

system: "You are the viewpoint_discovery_agent, a conversational agent designed to engage users in thoughtful discussion to determine their viewpoint on various topics. Your approach is friendly, neutral, and non-judgmental. You use a curious and inquiring tone, with simple and clear language that avoids technical jargon. Your questioning style is open-ended and probing, encouraging users to share their thoughts and opinions. Your responses are brief and concise, summarizing the user's viewpoint and asking follow-up questions."

steps:
  - name: introduction
    type: message
    message: "Hello! I'm here to help you explore your thoughts and opinions on a particular topic. What topic would you like to discuss today?"
    async: true

  - name: capture_topic
    type: question
    question: "Could you please share what topic you'd like to explore?"
    async: true

  - name: initial_viewpoint
    type: question
    question: "That's an interesting topic. What are your initial thoughts or viewpoints on {{ context.topic }}?"
    async: true

  - name: viewpoint_prompt
    type: prompt
    prompt: "Please share your perspective on this topic."
    default: "I'd love to hear more about your perspective on this topic. Could you share a bit more detail?"

  - name: explore_reasoning
    type: message
    message: "Thank you for sharing your perspective. I'd like to understand more about your reasoning. What experiences, values, or information have shaped your viewpoint on this topic?"

  - name: evidence_question
    type: question
    question: "What evidence or examples would you point to that support your viewpoint?"

  - name: evidence_prompt
    type: prompt
    prompt: "Please share any evidence, examples, or reasoning that supports your viewpoint."
    default: "Even a simple example or personal experience that shaped your view would be helpful."

  - name: perspective_exploration
    type: question
    question: "Would you be interested in exploring this topic from a specific perspective? This could help deepen your understanding."
    options:
      - Economic Perspective
      - Social Perspective
      - Ethical Perspective
      - Legal Perspective
      - Environmental Perspective
      - No thanks, continue with my own perspective

  - name: analyze_perspective
    type: message
    message: "Let's analyze the issue from the {{ context.selected_perspective }} perspective."

  - name: perspective_analysis
    type: question
    question: "How might someone thinking primarily from a {{ context.selected_perspective }} perspective view this issue differently than you do?"

  - name: counterarguments
    type: message
    message: "I appreciate you sharing those points. Have you considered any counterarguments or alternative perspectives on this topic? What might someone with a different viewpoint say?"

  - name: summary
    type: message
    message: "Let me summarize what I understand about your viewpoint so far: You believe that {{ context.topic }} is important, and your perspective includes {{ context.viewpoint }}. You've supported this with {{ context.evidence }}. Is this an accurate summary of your position?"

  - name: summary_confirmation
    type: question
    question: "Is this summary accurate? If not, what would you like to clarify or add?"

  - name: next_steps_introduction
    type: message
    message: "Now that we have a good understanding of your viewpoint on {{ context.topic }}, I'd like to offer some options for how we can proceed."

  - name: next_steps
    type: question
    question: "Would you like to: 1) Develop your perspective further with more detailed questions, 2) See how different agents might debate this topic from various perspectives, or 3) Engage in a whiteboard session where we can visually map out and develop your viewpoint?"

  - name: next_steps_prompt
    type: prompt
    prompt: "Please choose option 1, 2, or 3, or let me know if you'd prefer something else."
    default: "I didn't quite understand your response. Could you please choose one of the options or provide more information?"

  - name: new_fact
    type: question
    question: "You've provided a new fact that is not available to me. Would you like me to verify this information using a verification agent?"

  - name: verification_agent
    type: handoff
    agent: verification_agent
    topic: "{{ context.topic }}"
    viewpoint: "{{ context.viewpoint }}"
    evidence: "{{ context.evidence }}"
    maxTimeoutMinutes: 30

  - name: handoff_to_debate
    type: handoff
    agent: debate_agent
    topic: "{{ context.topic }}"
    viewpoint: "{{ context.viewpoint }}"
    evidence: "{{ context.evidence }}"
    maxTimeoutMinutes: 30

  - name: handoff_to_whiteboard
    type: handoff
    agent: whiteboard_agent
    topic: "{{ context.topic }}"
    viewpoint: "{{ context.viewpoint }}"
    evidence: "{{ context.evidence }}"
    maxTimeoutMinutes: 30

    