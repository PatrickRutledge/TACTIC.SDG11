"""
Viewpoint Discovery Agent Python Implementation

This module provides the Python implementation of the viewpoint discovery agent,
which engages users in discussions to determine their viewpoints on various topics.
The agent integrates with the IBM Watson Orchestrate system to provide a conversational
experience that helps users articulate and explore their perspectives.
"""

import json
import logging
import os
import traceback
from datetime import datetime
from logging.handlers import RotatingFileHandler
from typing import Dict, List, Optional, Any, Union

from orchestrate.annotations import agent, handler, parameter
from orchestrate.types import Message

# Configure enhanced logging system
def setup_logging(agent_name: str, log_dir: str = "logs") -> logging.Logger:
    """
    Set up advanced structured logging for the agent.
    
    Args:
        agent_name: Name of the agent for logging identification
        log_dir: Directory to store log files
        
    Returns:
        Logger instance configured with file and console handlers
    """
    # Create log directory if it doesn't exist
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    log_file = os.path.join(log_dir, f"{agent_name}.log")
    
    # Create a custom JSON formatter for structured logging
    class JsonFormatter(logging.Formatter):
        def format(self, record):
            log_data = {
                "timestamp": datetime.utcnow().isoformat(),
                "level": record.levelname,
                "agent": agent_name,
                "message": record.getMessage(),
                "module": record.module,
                "function": record.funcName,
                "line": record.lineno
            }
            
            # Include exception info if present
            if record.exc_info:
                log_data["exception"] = self.formatException(record.exc_info)
                
            # Include custom fields if present
            if hasattr(record, "context") and record.context:
                log_data["context"] = record.context
                
            return json.dumps(log_data)
    
    # Set up file handler with rotation (10MB max size, keep 5 backups)
    file_handler = RotatingFileHandler(
        log_file, 
        maxBytes=10*1024*1024,  
        backupCount=5
    )
    file_handler.setFormatter(JsonFormatter())
    
    # Set up console handler with simpler format for human readability
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    ))
    
    # Get logger for this agent
    logger = logging.getLogger(agent_name)
    logger.setLevel(logging.INFO)
    
    # Remove any existing handlers to avoid duplicates
    if logger.handlers:
        for handler in logger.handlers:
            logger.removeHandler(handler)
    
    # Add our handlers
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger

# Initialize enhanced logger
logger = setup_logging("viewpoint_discovery_agent")

class AgentError(Exception):
    """Base class for Viewpoint Discovery Agent exceptions."""
    pass

class ContextError(AgentError):
    """Exception raised when there's an issue with the context variables."""
    pass

class HandoffError(AgentError):
    """Exception raised when there's an issue with handoffs to other agents."""
    pass

class TopicError(AgentError):
    """Exception raised when there's an issue with the topic."""
    pass

class InputError(AgentError):
    """Exception raised when there's an issue with user input."""
    pass

@agent("viewpoint_discovery_agent")
class ViewpointDiscoveryAgent:
    """
    An agent designed to engage users in discussion to determine their viewpoint on topics.
    
    This agent helps users articulate and explore their perspectives through thoughtful
    questioning and analysis. It can identify the user's core viewpoints, supporting evidence,
    and underlying values while maintaining a neutral, empathetic stance.
    
    The agent implements robust error handling to ensure a smooth conversation flow
    even when unexpected conditions occur. It also maintains conversation metrics
    to track important events like topic changes or handoff attempts.
    """
    
    def __init__(self):
        """Initialize the Viewpoint Discovery Agent with default values and metrics tracking."""
        # Available perspectives for exploration
        self.perspectives = [
            "Economic Perspective",
            "Social Perspective",
            "Ethical Perspective",
            "Legal Perspective",
            "Environmental Perspective"
        ]
        
        # Initialize conversation metrics
        self._topic_changes = 0
        self._handoff_attempts = 0
        self._handoff_successes = 0
        self._conversation_start_time = datetime.utcnow()
        
        logger.info("Viewpoint Discovery Agent initialized")
        
    @handler("introduction")
    def introduction(self) -> Dict[str, Any]:
        """
        Handle the initial introduction step.
        
        Returns:
            Dict[str, Any]: Response with greeting message
        """
        return {
            "response": "Hello! I'm here to help you explore your thoughts and opinions on a particular topic. What topic would you like to discuss today?"
        }
    
    @handler("capture_topic")
    def capture_topic(self, message: Message) -> Dict[str, Any]:
        """
        Capture the topic the user wants to discuss.
        
        This handler processes the user's initial topic selection and performs validation
        to ensure it's a viable discussion topic. It handles various edge cases such as
        empty responses, extremely short topics, and potentially sensitive content.
        
        Args:
            message: User's message containing the topic
            
        Returns:
            Dict[str, Any]: Response with the captured topic
        """
        try:
            # Validate message object
            if message is None:
                raise InputError("Message object is None")
                
            # Get content with safe fallback
            topic = message.content.strip() if hasattr(message, 'content') else ""
            
            # Comprehensive validation
            if not topic:
                logger.warning("Empty topic provided")
                return {
                    "response": "I didn't quite catch that. Could you please share what topic you'd like to explore?"
                }
                
            if len(topic) < 2:
                logger.warning(f"Topic too short: '{topic}'")
                return {
                    "response": "That topic seems a bit short. Could you please provide a more specific topic you'd like to discuss?"
                }
                
            # Check if topic is overly lengthy (might indicate misunderstanding)
            if len(topic) > 100:
                logger.warning(f"Unusually long topic provided: {len(topic)} chars")
                return {
                    "response": "That's quite detailed! Could you provide a shorter, more focused topic for our discussion?"
                }
                
            # Log the selected topic
            logger.info(f"User selected topic: {topic}")
            
            # Store metrics
            self._record_conversation_event("topic_selected", {"topic": topic})
            
            # Return with context variables
            return {
                "context_variables": {
                    "topic": topic,
                    "previous_topic": topic
                },
                "response": f"That's an interesting topic. What are your initial thoughts or viewpoints on {topic}?"
            }
            
        except InputError as e:
            # Handle specific input errors
            logger.error(f"Input error in capture_topic: {str(e)}")
            return {
                "response": "I'm having trouble understanding your input. Could you please share what topic you'd like to explore?"
            }
        except Exception as e:
            # Handle unexpected errors
            logger.error(f"Unexpected error in capture_topic: {str(e)}", exc_info=True)
            return {
                "response": "I apologize, but I'm having trouble processing your request. Could you please share what topic you'd like to discuss today?"
            }
            
    def _record_conversation_event(self, event_type: str, data: Dict[str, Any] = None) -> None:
        """
        Record a conversation event for metrics and analysis.
        
        Args:
            event_type: The type of event (e.g., topic_change, handoff_attempt)
            data: Additional data about the event
        """
        if data is None:
            data = {}
            
        # Add timestamp
        data["timestamp"] = datetime.utcnow().isoformat()
        
        # Log with context
        logger_extras = {"context": data}
        logger.info(f"Conversation event: {event_type}", extra=logger_extras)
    
    @handler("initial_viewpoint")
    def initial_viewpoint(self, message: Message, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Capture the user's initial viewpoint on the topic.
        
        This handler processes the user's first expression of their perspective on the 
        conversation topic. It stores this viewpoint in the context variables and formulates 
        a follow-up question to explore the reasoning behind their viewpoint.
        
        The handler is a critical point in the conversation flow as it transitions from
        topic selection to deeper exploration of the user's perspective.
        
        Args:
            message: User's message containing their initial viewpoint statement
            context: Conversation context including the selected topic
            
        Returns:
            Dict[str, Any]: Response acknowledging the viewpoint with follow-up question
        """
        try:
            # Extract the user's viewpoint from their message
            user_viewpoint = message.content
            
            # Get the current conversation topic with fallback
            conversation_topic = context.get("topic", "the topic")
            
            # Log the viewpoint capture for analysis
            logger.info(f"Initial viewpoint captured for topic '{conversation_topic}': {user_viewpoint}")
            
            # Track this significant conversation event
            self._record_conversation_event("viewpoint_captured", {
                "topic": conversation_topic,
                "viewpoint_length": len(user_viewpoint)
            })
            
            # Store the viewpoint in context variables and provide a follow-up question
            # that encourages deeper reflection on the factors that shaped their perspective
            return {
                "context_variables": {
                    "viewpoint": user_viewpoint
                },
                "response": f"Thank you for sharing your perspective. I'd like to understand more about your reasoning. What experiences, values, or information have shaped your viewpoint on {conversation_topic}?"
            }
        except Exception as e:
            # Handle unexpected errors
            logger.error(f"Error capturing initial viewpoint: {str(e)}", exc_info=True)
            return {
                "response": "Thank you for sharing that. Could you tell me more about why you hold this perspective?"
            }
        
    
    @handler("detect_topic_change")
    def detect_topic_change(self, message: Message, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Detect if the user has changed topics during the conversation.
        
        This handler compares the current topic with the previous topic to determine
        if the user has shifted the conversation. When a topic change is detected,
        it confirms with the user whether they want to pursue the new topic or return
        to the previous one. The handler handles various edge cases such as missing
        context variables and partial topic changes.
        
        Args:
            message: User's message that might indicate a topic change
            context: Conversation context containing current and previous topics
            
        Returns:
            Dict[str, Any]: Response handling any topic change with appropriate options
        """
        try:
            # Verify context is valid
            if not context:
                logger.warning("Empty context in detect_topic_change")
                return {"continue": True}
            
            # Extract topics from context with fallbacks
            current_topic = context.get("topic", "")
            previous_topic = context.get("previous_topic", "")
            
            # Log the comparison for debugging
            logger.debug(f"Topic comparison - Current: '{current_topic}', Previous: '{previous_topic}'")
            
            # Verify we have valid strings to compare
            if not current_topic or not previous_topic:
                logger.warning("Missing topic information in context")
                return {"continue": True}  # Continue the conversation flow
            
            # Check for topic change with case-insensitive comparison
            if current_topic.lower() != previous_topic.lower():
                # Track topic change in metrics
                self._topic_changes += 1
                self._record_conversation_event(
                    "topic_change", 
                    {"from": previous_topic, "to": current_topic, "change_count": self._topic_changes}
                )
                
                logger.info(f"Topic change detected ({self._topic_changes}): {previous_topic} -> {current_topic}")
                
                return {
                    "response": f"I notice you've moved to discussing {current_topic} instead of {previous_topic}. Would you like to continue with this new topic?"
                }
            
            return {"continue": True}
            
        except ContextError as e:
            # Handle context-specific errors
            logger.error(f"Context error in detect_topic_change: {str(e)}")
            return {"continue": True}  # Fail gracefully by continuing
            
        except Exception as e:
            # Handle unexpected errors
            logger.error(f"Unexpected error in detect_topic_change: {str(e)}", exc_info=True)
            return {"continue": True}  # Fail gracefully by continuing
    
    @handler("evidence_question")
    def evidence_question(self, message: Message, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Handle the user's response with evidence supporting their viewpoint.
        
        This handler processes the user's evidence or examples that support their
        viewpoint on the conversation topic. It detects when users reference new information 
        sources like studies or research and captures this information separately.
        
        The handler performs several key functions:
        1. Validates input and handles missing or empty responses
        2. Detects references to new information/research using keyword analysis
        3. Records evidence characteristics for conversation analytics
        4. Provides appropriate responses based on evidence type
        5. Stores evidence in context for later use in the conversation
        
        Args:
            message: User's message containing evidence or examples
            context: Conversation context including topic and viewpoint
            
        Returns:
            Dict[str, Any]: Response acknowledging evidence and suggesting perspective exploration
        """
        try:
            # Extract and validate user evidence
            user_evidence = self._extract_evidence_from_message(message)
            
            # Analyze the evidence characteristics
            evidence_analysis = self._analyze_evidence(user_evidence)
            
            # Record metrics about the provided evidence
            self._track_evidence_metrics(user_evidence, evidence_analysis)
            
            # Build and return the appropriate response
            return self._build_evidence_response(user_evidence, evidence_analysis)
            
        except InputError as e:
            # Handle specific input validation errors
            logger.error(f"Input error in evidence_question: {str(e)}")
            return {
                "response": "I'm having trouble processing your examples. Could you try explaining your evidence in a different way?"
            }
        except Exception as e:
            # Handle unexpected errors with graceful fallback
            logger.error(f"Unexpected error in evidence_question: {str(e)}", exc_info=True)
            return {
                "response": "I appreciate your input. Would you be interested in exploring this topic from different perspectives?"
            }
    
    def _extract_evidence_from_message(self, message: Message) -> str:
        """
        Extract and validate evidence from user message.
        
        Args:
            message: User's message object
            
        Returns:
            str: Extracted evidence text
            
        Raises:
            InputError: If message is None or content is empty
        """
        # Validate message object
        if message is None:
            raise InputError("Message object is None")
            
        # Get content with safe fallback
        evidence = message.content if hasattr(message, 'content') else ""
        
        # Check if evidence is empty
        if not evidence or evidence.strip() == "":
            logger.warning("Empty evidence provided")
            raise InputError("Empty evidence provided")
            
        return evidence
    
    def _analyze_evidence(self, evidence: str) -> Dict[str, Any]:
        """
        Analyze evidence for characteristics like new information markers.
        
        Args:
            evidence: The evidence text to analyze
            
        Returns:
            Dict[str, Any]: Analysis results including contains_new_info flag
        """
        # Check for new information markers with comprehensive detection
        info_markers = [
            "new study", "recent research", "just published", "new report",
            "latest findings", "recently discovered", "new data shows",
            "according to new", "new evidence", "recent developments"
        ]
        
        contains_new_info = any(marker in evidence.lower() for marker in info_markers)
        
        return {
            "contains_new_info": contains_new_info,
            "evidence_type": "new_information" if contains_new_info else "standard_evidence",
            "length": len(evidence)
        }
    
    def _track_evidence_metrics(self, evidence: str, analysis: Dict[str, Any]) -> None:
        """
        Record metrics about the provided evidence for analytics.
        
        Args:
            evidence: The evidence text
            analysis: Analysis results from _analyze_evidence
        """
        # Record the evidence type and characteristics in metrics
        self._record_conversation_event(
            "evidence_provided", 
            {
                "type": analysis["evidence_type"], 
                "length": analysis["length"],
                "contains_citations": "http" in evidence.lower() or "www" in evidence.lower()
            }
        )
        
        if analysis["contains_new_info"]:
            logger.info("New information detected in user evidence")
    
    def _build_evidence_response(self, evidence: str, analysis: Dict[str, Any]) -> Dict[str, Any]:
        """
        Build appropriate response based on evidence analysis.
        
        Args:
            evidence: The evidence text
            analysis: Analysis results from _analyze_evidence
            
        Returns:
            Dict[str, Any]: Response with context variables and appropriate message
        """
        # Prepare response with context variables
        response = {
            "context_variables": {
                "evidence": evidence
            }
        }
        
        # Add new fact if detected and provide appropriate response
        if analysis["contains_new_info"]:
            response["context_variables"]["new_fact"] = evidence
            response["response"] = "That's interesting information I wasn't aware of. I've noted this for our discussion. Would you be interested in exploring this topic from a specific perspective? This could help deepen your understanding."
        else:
            response["response"] = "Thank you for providing those examples. Would you be interested in exploring this topic from a specific perspective? This could help deepen your understanding."
        
        return response
    
    @handler("perspective_exploration")
    def perspective_exploration(self, message: Message, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Handle the user's choice of perspective for exploration.
        
        This handler processes the user's selection of a perspective from which to explore
        the topic further. It enables users to examine their viewpoint from alternative angles,
        which is a critical step in developing a more nuanced understanding of complex issues.
        
        The handler supports:
        1. Selecting a specific predefined perspective (e.g., Economic, Social, Ethical)
        2. Declining to explore alternative perspectives (continuing with own perspective)
        3. Handling ambiguous or invalid perspective selections with graceful fallbacks
        
        This is a key moment in the conversation where users can choose to expand beyond
        their initial viewpoint and consider how others might approach the same topic.
        
        Args:
            message: User's message containing their selected perspective
            context: Conversation context including topic, viewpoint and evidence
                
        Returns:
            Dict[str, Any]: Response with perspective-specific follow-up questions
        """
        try:
            # Process the user's perspective selection
            perspective_selection = self._process_perspective_selection(message)
            
            # Handle case where user declines to explore alternative perspectives
            if self._is_perspective_declined(perspective_selection):
                return self._handle_perspective_decline()
            
            # Normalize and validate the selected perspective
            normalized_perspective = self._normalize_perspective(perspective_selection)
            
            # Generate response for the selected perspective
            return self._generate_perspective_response(normalized_perspective)
            
        except InputError as e:
            # Handle specific input validation errors
            logger.error(f"Input error in perspective_exploration: {str(e)}")
            return {
                "response": "I'm having trouble understanding your selection. Would you like to explore this topic from an economic, social, ethical, legal, or environmental perspective? Or would you prefer to continue with your own perspective?"
            }
        except Exception as e:
            # Handle unexpected errors with graceful fallback
            logger.error(f"Unexpected error in perspective_exploration: {str(e)}", exc_info=True)
            return {
                "response": "I apologize for the confusion. Would you like to continue with your own perspective on this topic or explore it from another angle?"
            }
    
    def _process_perspective_selection(self, message: Message) -> str:
        """
        Process and validate the user's perspective selection.
        
        Args:
            message: User's message object containing perspective selection
            
        Returns:
            str: The processed perspective selection
            
        Raises:
            InputError: If message is None or content is empty
        """
        # Validate message object
        if message is None:
            raise InputError("Message object is None")
            
        # Extract perspective selection with safe fallback
        selection = message.content if hasattr(message, 'content') else ""
        
        # Handle empty selection
        if not selection or selection.strip() == "":
            logger.warning("Empty perspective selection")
            perspective_list = ", ".join(self.perspectives)
            raise InputError(f"Empty perspective selection. Options: {perspective_list}")
        
        # Log the selected perspective
        logger.info(f"User selected perspective: {selection}")
        self._record_conversation_event("perspective_selected", {"perspective": selection})
        
        return selection
    
    def _is_perspective_declined(self, selection: str) -> bool:
        """
        Check if the user has declined to explore alternative perspectives.
        
        Args:
            selection: The user's perspective selection text
            
        Returns:
            bool: True if user declined to explore perspectives
        """
        # Comprehensive list of decline phrases
        decline_phrases = [
            "no thanks", "continue with my own", "own perspective", 
            "no", "skip", "my perspective", "pass", "don't want to",
            "not interested", "stay with mine"
        ]
        
        return any(phrase in selection.lower() for phrase in decline_phrases)
    
    def _handle_perspective_decline(self) -> Dict[str, Any]:
        """
        Handle when user declines to explore alternative perspectives.
        
        Returns:
            Dict[str, Any]: Response prompting for counterarguments
        """
        # When user declines perspectives, redirect to counterarguments
        logger.info("User declined to explore alternative perspectives")
        return {
            "response": "I appreciate you sharing those points. Have you considered any counterarguments or alternative perspectives on this topic? What might someone with a different viewpoint say?"
        }
    
    def _normalize_perspective(self, selection: str) -> str:
        """
        Normalize and validate the selected perspective against known options.
        
        Handles typos and partial matches by finding the closest known perspective.
        
        Args:
            selection: The user's perspective selection
            
        Returns:
            str: The normalized perspective name
        """
        # Check if it's already an exact match
        if selection in self.perspectives:
            return selection
        
        # Try case-insensitive match
        for perspective in self.perspectives:
            if perspective.lower() == selection.lower():
                return perspective
        
        # Try partial match
        logger.warning(f"Unknown perspective selected: {selection}")
        for perspective in self.perspectives:
            if perspective.lower() in selection.lower():
                logger.info(f"Matched to known perspective: {perspective}")
                return perspective
        
        # If no match found, return as is (will be handled as custom perspective)
        return selection
    
    def _generate_perspective_response(self, perspective: str) -> Dict[str, Any]:
        """
        Generate an appropriate response for the selected perspective.
        
        Args:
            perspective: The normalized perspective name
            
        Returns:
            Dict[str, Any]: Response with context variables and follow-up question
        """
        # Store the selected perspective and provide appropriate response
        return {
            "context_variables": {
                "selected_perspective": perspective
            },
            "response": f"Let's analyze the issue from the {perspective} perspective. How might someone thinking primarily from a {perspective} angle view this issue differently than you do?"
        }
    
    @handler("summary")
    def summary(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate a summary of the user's viewpoint based on the conversation.
        
        This handler creates a cohesive summary of the user's viewpoint by analyzing
        the conversation context. It integrates the conversation topic, user viewpoint, 
        and supporting evidence into a concise summary and asks the user to confirm its accuracy.
        The handler handles various edge cases such as missing context variables and
        incomplete information.
        
        Args:
            context: Conversation context containing topic, viewpoint, and evidence
            
        Returns:
            Dict[str, Any]: Response with a comprehensive summary for user confirmation
        """
        try:
            # Delegate to helper methods for better organization and readability
            if not self._validate_summary_context(context):
                return self._handle_missing_summary_context()
            
            # Extract and validate key conversation elements
            conversation_elements = self._extract_summary_elements(context)
            
            # Check if we have enough meaningful information to create a summary
            if not self._has_sufficient_viewpoint_info(conversation_elements):
                return self._handle_insufficient_viewpoint_info()
            
            # Generate the actual summary text
            summary_text = self._generate_viewpoint_summary(conversation_elements)
            
            # Track metrics for summary generation
            self._record_conversation_event("summary_generated", {
                "topic": conversation_elements["conversation_topic"],
                "has_perspective": conversation_elements["selected_perspective"] is not None,
                "has_new_fact": conversation_elements["new_fact"] is not None
            })
            
            logger.info("Generated viewpoint summary")
            
            return {
                "response": summary_text
            }
            
        except ContextError as e:
            # Handle context-specific errors
            logger.error(f"Context error in summary: {str(e)}")
            return {
                "response": "I'm having trouble creating a summary of your viewpoint. Could you briefly restate your main position on this topic?"
            }
        except Exception as e:
            # Handle unexpected errors
            logger.error(f"Unexpected error in summary: {str(e)}", exc_info=True)
            return {
                "response": "Let me try to summarize what I understand so far. You've shared some interesting thoughts on this topic. Have I understood your position correctly?"
            }
    
    def _validate_summary_context(self, context: Dict[str, Any]) -> bool:
        """
        Validate that the context has the necessary elements for summary generation.
        
        Args:
            context: Conversation context to validate
            
        Returns:
            bool: True if context is valid, False otherwise
        """
        # Check if context exists
        if not context:
            logger.warning("Missing context in summary handler")
            return False
        return True
    
    def _handle_missing_summary_context(self) -> Dict[str, Any]:
        """
        Handle the case where the context is missing for summary generation.
        
        Returns:
            Dict[str, Any]: Response requesting context information
        """
        return {
            "response": "I'd like to summarize your viewpoint, but I seem to be missing some context. Could you remind me what topic we're discussing and your main perspective on it?"
        }
        
    def _extract_summary_elements(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Extract and validate all necessary elements for summary generation from context.
        
        Args:
            context: Conversation context containing viewpoint information
            
        Returns:
            Dict[str, Any]: Dictionary with all validated elements for summary
        """
        # Extract key variables with fallbacks and validation
        conversation_topic = self._get_validated_context_var(context, "topic", "the topic")
        user_viewpoint = self._get_validated_context_var(context, "viewpoint", "your thoughts")
        supporting_evidence = self._get_validated_context_var(context, "evidence", "the points you've made")
        
        # Get optional perspective if it exists
        selected_perspective = context.get("selected_perspective", None)
        
        # Get optional new facts if they exist
        new_fact = context.get("new_fact", None)
        
        return {
            "conversation_topic": conversation_topic,
            "user_viewpoint": user_viewpoint,
            "supporting_evidence": supporting_evidence,
            "selected_perspective": selected_perspective,
            "new_fact": new_fact
        }
    
    def _has_sufficient_viewpoint_info(self, elements: Dict[str, Any]) -> bool:
        """
        Check if we have enough meaningful information to create a summary.
        
        Args:
            elements: Dictionary with extracted conversation elements
            
        Returns:
            bool: True if we have sufficient information, False otherwise
        """
        if (elements["conversation_topic"] == "the topic" or 
            elements["user_viewpoint"] == "your thoughts"):
            logger.warning("Insufficient information for summary")
            return False
        return True
        
    def _handle_insufficient_viewpoint_info(self) -> Dict[str, Any]:
        """
        Handle the case where we don't have enough information for a summary.
        
        Returns:
            Dict[str, Any]: Response requesting more information
        """
        return {
            "response": "I'd like to summarize your viewpoint, but I don't have enough information yet. Could you tell me more about your perspective on this topic?"
        }
    
    def _generate_viewpoint_summary(self, elements: Dict[str, Any]) -> str:
        """
        Generate a comprehensive summary text from conversation elements.
        
        Args:
            elements: Dictionary with extracted conversation elements
            
        Returns:
            str: Formatted summary text
        """
        # Format perspective text if available
        perspective_text = ""
        if elements["selected_perspective"]:
            perspective_text = f" When looking at this from a {elements['selected_perspective']}, "
        
        # Format new fact text if available
        fact_text = ""
        if elements["new_fact"] and len(elements["new_fact"]) > 10:
            fact_text = f" You've also shared new information: {elements['new_fact'][:100]}..."
        
        # Create a comprehensive summary
        return (f"Let me summarize what I understand about your viewpoint so far: You believe that "
                f"{elements['conversation_topic']} is important, and your perspective includes "
                f"{elements['user_viewpoint']}.{perspective_text} You've supported this with "
                f"{elements['supporting_evidence']}.{fact_text} Is this an accurate summary of your position?")
    
    def _get_validated_context_var(self, context: Dict[str, Any], var_name: str, default_value: str) -> str:
        """
        Get and validate a context variable with proper error handling.
        
        Args:
            context: Conversation context
            var_name: Name of the variable to retrieve
            default_value: Default value if variable doesn't exist
            
        Returns:
            Validated string value of the context variable
        """
        try:
            value = context.get(var_name, default_value)
            
            # Simple validation
            if not value or not isinstance(value, str):
                return default_value
                
            # Trim very long values to a reasonable length
            if len(value) > 500:
                return value[:497] + "..."
                
            return value
            
        except Exception as e:
            logger.warning(f"Error validating context variable {var_name}: {str(e)}")
            return default_value
    
    @handler("next_steps")
    def next_steps(self, message: Message, context: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Handle user's choice for next steps in the conversation.
        
        This handler processes the user's selection for how to proceed with the conversation.
        Options include deeper exploration of their viewpoint, handoff to a debate system,
        or handoff to a whiteboard system. The handler handles various edge cases such as
        ambiguous selections, empty responses, failed handoffs, and invalid message objects.
        
        Args:
            message: User's message with choice
            context: Optional conversation context
            
        Returns:
            Dict[str, Any]: Response based on user's choice with appropriate next steps
        """
        try:
            # Validate message object
            if message is None:
                raise InputError("Message object is None")
                
            # Extract choice with safe fallback
            choice_text = message.content.strip() if hasattr(message, 'content') else ""
            
            # If empty choice, provide guidance
            if not choice_text:
                logger.warning("Empty choice in next_steps")
                return {
                    "response": "I didn't catch your preference. Would you like to: 1) Develop your perspective further, 2) See a debate on this topic, or 3) Use a whiteboard to map your viewpoint?"
                }
            
            # Process choice with enhanced detection and more robust parsing
            choice_text_lower = choice_text.lower()
            
            # Option 1: Develop perspective further
            if (choice_text == "1" or 
                any(word in choice_text_lower for word in ["develop", "further", "more", "questions", "continue", "depth"])):
                
                logger.info("User chose to develop perspective further")
                self._record_conversation_event("next_step_selected", {"choice": "develop_further"})
                
                return {
                    "response": "Great! Let's explore your perspective in more depth. What specific aspects of this topic would you like to explore further?"
                }
                
            # Option 2: Handoff to debate system
            elif (choice_text == "2" or 
                  any(word in choice_text_lower for word in ["debate", "agent", "different", "perspectives", "discuss"])):
                
                logger.info("User chose handoff to debate system")
                self._handoff_attempts += 1
                self._record_conversation_event("handoff_attempt", {
                    "type": "debate",
                    "attempt_number": self._handoff_attempts
                })
                
                try:
                    # Prepare for handoff with safeguards
                    return {
                        "context_variables": {
                            "handoff_status": "initiating_debate"
                        },
                        "response": "I'll hand you off to our debate system, where you can see different agents discuss this topic from various perspectives. This should give you a more rounded view of the issue.",
                        "handoff": {
                            "agent": "debate_agent",
                            "timeout": 60  # Add timeout in seconds
                        }
                    }
                except Exception as handoff_error:
                    # Handle handoff preparation errors
                    logger.error(f"Failed to prepare debate handoff: {str(handoff_error)}")
                    return {
                        "response": "I'm having trouble connecting to the debate system right now. Would you like to continue exploring your perspective with me instead?"
                    }
                    
            # Option 3: Handoff to whiteboard system
            elif (choice_text == "3" or 
                  any(word in choice_text_lower for word in ["whiteboard", "visual", "map", "draw"])):
                
                logger.info("User chose handoff to whiteboard system")
                self._handoff_attempts += 1
                self._record_conversation_event("handoff_attempt", {
                    "type": "whiteboard",
                    "attempt_number": self._handoff_attempts
                })
                
                try:
                    # Prepare for handoff with safeguards
                    return {
                        "context_variables": {
                            "handoff_status": "initiating_whiteboard"
                        },
                        "response": "I'll hand you off to our whiteboard system, where you can visually map out and develop your viewpoint.",
                        "handoff": {
                            "agent": "whiteboard_agent",
                            "timeout": 60  # Add timeout in seconds
                        }
                    }
                except Exception as handoff_error:
                    # Handle handoff preparation errors
                    logger.error(f"Failed to prepare whiteboard handoff: {str(handoff_error)}")
                    return {
                        "response": "I'm having trouble connecting to the whiteboard system right now. Would you like to continue exploring your perspective with me instead?"
                    }
            
            # Handle ambiguous or unrecognized choices
            else:
                logger.warning(f"Ambiguous next step choice: '{choice_text}'")
                return {
                    "response": "I didn't quite understand your choice. Would you like to: 1) Develop your perspective further with more detailed questions, 2) See how different agents might debate this topic from various perspectives, or 3) Engage in a whiteboard session where we can visually map out and develop your viewpoint?"
                }
                
        except InputError as e:
            # Handle specific input errors
            logger.error(f"Input error in next_steps: {str(e)}")
            return {
                "response": "I'm having trouble understanding your choice. Could you select option 1, 2, or 3?"
            }
        except Exception as e:
            # Handle unexpected errors
            logger.error(f"Unexpected error in next_steps: {str(e)}", exc_info=True)
            return {
                "response": "I apologize, but I'm having trouble processing your choice. Would you like to continue exploring your perspective with me for now?"
            }
    
    @handler("deeper_questions")
    def deeper_questions(self, message: Message, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Handle deeper exploration of the user's viewpoint.
        
        Args:
            message: User's message
            context: Conversation context
            
        Returns:
            Dict[str, Any]: Response with deeper questions
        """
        topic = context.get("topic", "this topic")
        
        return {
            "response": f"What are the core values or principles that underlie your viewpoint on {topic}? How do you think your perspective might evolve or change in the future, given new information or experiences?"
        }
    
    @handler("closing")
    def closing(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Handle the closing of the conversation.
        
        Args:
            context: Conversation context
            
        Returns:
            Dict[str, Any]: Closing response
        """
        topic = context.get("topic", "our topic")
        
        return {
            "response": f"I appreciate you taking the time to explore your viewpoint on {topic}. Your thoughtful responses have helped create a clearer picture of your perspective. Feel free to return anytime you'd like to explore your thoughts on another topic."
        }
    
    @handler("handle_return_from_handoff")
    def handle_return_from_handoff(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Handle the user's return from a handoff to another agent.
        
        This handler manages the transition back from another agent (debate or whiteboard)
        to this agent. It acknowledges the return, resets the handoff status, and offers
        options for continuing the conversation. The handler handles various edge cases
        such as missing context, unknown handoff status, and unexpected returns.
        
        Args:
            context: Conversation context including handoff status
            
        Returns:
            Dict[str, Any]: Welcome back response with appropriate next steps
        """
        try:
            # Check if context exists
            if not context:
                logger.warning("Missing context in handle_return_from_handoff")
                return {
                    "context_variables": {
                        "handoff_status": "none"
                    },
                    "response": "Welcome back! Would you like to continue our discussion?"
                }
            
            # Get topic with fallback
            topic = context.get("topic", "our topic")
            
            # Get previous handoff status
            handoff_status = context.get("handoff_status", "unknown")
            
            # Track metrics for handoff returns
            self._handoff_successes += 1
            self._record_conversation_event("handoff_return", {
                "from_status": handoff_status,
                "success_count": self._handoff_successes,
                "topic": topic
            })
            
            # Log the handoff return
            logger.info(f"User returned from handoff with status: {handoff_status}")
            
            # Customize response based on what they're returning from
            if handoff_status == "returning_from_debate":
                return {
                    "context_variables": {
                        "handoff_status": "none"
                    },
                    "response": f"Welcome back from the debate! Did seeing different perspectives on {topic} help clarify your own viewpoint? Would you like to continue exploring your thoughts on this topic or discuss something else?"
                }
            elif handoff_status == "returning_from_whiteboard":
                return {
                    "context_variables": {
                        "handoff_status": "none"
                    },
                    "response": f"Welcome back from the whiteboard session! Did visualizing your thoughts on {topic} help organize your ideas? Would you like to continue exploring this topic or discuss something new?"
                }
            else:
                # Generic response for unknown handoff status
                return {
                    "context_variables": {
                        "handoff_status": "none"
                    },
                    "response": f"Welcome back! I hope your experience was helpful. Would you like to continue exploring your viewpoint on {topic} or discuss something else?"
                }
                
        except ContextError as e:
            # Handle context-specific errors
            logger.error(f"Context error in handle_return_from_handoff: {str(e)}")
            return {
                "context_variables": {
                    "handoff_status": "none"
                },
                "response": "Welcome back! Would you like to continue our previous discussion or start a new one?"
            }
        except Exception as e:
            # Handle unexpected errors
            logger.error(f"Unexpected error in handle_return_from_handoff: {str(e)}", exc_info=True)
            return {
                "context_variables": {
                    "handoff_status": "none"
                },
                "response": "Welcome back! I apologize for any confusion. Would you like to continue our discussion?"
            }

# If this file is run directly, print a message
if __name__ == "__main__":
    print("Viewpoint Discovery Agent module loaded.")
    print("This module is designed to be imported and used within the IBM Watson Orchestrate system.")
