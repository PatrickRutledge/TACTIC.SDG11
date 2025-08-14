"""
Debate Agents Package

This package contains components for building and deploying debate agents
in the IBM Watson Orchestrate environment.
"""

from .debate_agent import DebateAgent
from .debate_flow import DebateFlow
from .debate_knowledge import DebateKnowledgeBase

__all__ = ['DebateAgent', 'DebateFlow', 'DebateKnowledgeBase']
