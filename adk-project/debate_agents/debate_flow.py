"""
Debate Flow Definition

This file defines the conversational flow for a structured debate,
including the different phases and transitions between them.
"""

from ibm_watsonx_orchestrate.agent_builder import Flow
from ibm_watsonx_orchestrate.agent_builder.models import State, Transition, Message

class DebateFlow(Flow):
    """Flow for structured debates."""
    
    def __init__(self, name="DebateFlow"):
        super().__init__(name=name)
        
        # Define the states of the debate
        self.add_state(State(
            name="introduction",
            description="Introduction to the debate topic and format",
            entry_message="Welcome to our debate. Let's begin by introducing our topic."
        ))
        
        self.add_state(State(
            name="opening_statements",
            description="Opening statements from each perspective",
            entry_message="Let's start with opening statements presenting the key arguments."
        ))
        
        self.add_state(State(
            name="arguments",
            description="Detailed arguments from each perspective",
            entry_message="Now, let's delve deeper into the arguments for each position."
        ))
        
        self.add_state(State(
            name="rebuttals",
            description="Rebuttals to the arguments presented",
            entry_message="Now each side will have an opportunity to respond to the arguments presented."
        ))
        
        self.add_state(State(
            name="cross_examination",
            description="Questions and answers between debaters",
            entry_message="Let's move to the cross-examination phase where questions can be posed to each side."
        ))
        
        self.add_state(State(
            name="closing_statements",
            description="Final statements summarizing positions",
            entry_message="We'll now hear closing statements from each side."
        ))
        
        self.add_state(State(
            name="conclusion",
            description="Summary of the debate and key takeaways",
            entry_message="Thank you for this debate. Let me summarize the key points and takeaways."
        ))
        
        # Define transitions between states
        self.add_transition(Transition(
            source="introduction",
            target="opening_statements",
            condition="topic_introduced"
        ))
        
        self.add_transition(Transition(
            source="opening_statements",
            target="arguments",
            condition="all_openings_presented"
        ))
        
        self.add_transition(Transition(
            source="arguments",
            target="rebuttals",
            condition="all_arguments_presented"
        ))
        
        self.add_transition(Transition(
            source="rebuttals",
            target="cross_examination",
            condition="all_rebuttals_presented"
        ))
        
        self.add_transition(Transition(
            source="cross_examination",
            target="closing_statements",
            condition="examination_complete"
        ))
        
        self.add_transition(Transition(
            source="closing_statements",
            target="conclusion",
            condition="all_closings_presented"
        ))
        
        # Set the initial state
        self.initial_state = "introduction"
