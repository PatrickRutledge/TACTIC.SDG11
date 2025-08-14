"""
Debate Knowledge Base Configuration

This file defines the knowledge base structure for the debate agent,
including how to access and utilize debate-relevant information.
"""

from ibm_watsonx_orchestrate.agent_builder import KnowledgeBase
import json
import os

# Sample debate topics and reference information
SAMPLE_TOPICS = [
    {
        "topic": "Climate Change Mitigation",
        "description": "Debate on the most effective approaches to mitigate climate change",
        "perspectives": [
            {
                "position": "Regulatory Approach",
                "key_points": [
                    "Government regulations are necessary to enforce emissions standards",
                    "Carbon pricing mechanisms can create economic incentives",
                    "International agreements establish global commitments"
                ]
            },
            {
                "position": "Market-Based Solutions",
                "key_points": [
                    "Innovation and technology development should drive changes",
                    "Private sector initiatives can be more efficient than regulation",
                    "Consumer choice and market demand can shift production patterns"
                ]
            }
        ]
    },
    {
        "topic": "Artificial Intelligence Regulation",
        "description": "Debate on how to approach AI regulation and governance",
        "perspectives": [
            {
                "position": "Proactive Regulation",
                "key_points": [
                    "Early regulatory frameworks can prevent harmful applications",
                    "Ethical guidelines should be established before widespread adoption",
                    "Precautionary principle suggests caution with emerging technologies"
                ]
            },
            {
                "position": "Innovation-First Approach",
                "key_points": [
                    "Regulation may stifle innovation and beneficial development",
                    "Technology often evolves faster than regulatory frameworks can adapt",
                    "Self-regulation by industry can be more responsive to rapid changes"
                ]
            }
        ]
    }
]

class DebateKnowledgeBase:
    """Knowledge base for debate-relevant information."""
    
    def __init__(self):
        self.topics = SAMPLE_TOPICS
        # In a real implementation, this would connect to a proper knowledge base
        
    def get_topic_information(self, topic_name):
        """Retrieve information about a specific debate topic."""
        for topic in self.topics:
            if topic["topic"].lower() == topic_name.lower():
                return topic
        return None
    
    def get_available_topics(self):
        """Get a list of available debate topics."""
        return [topic["topic"] for topic in self.topics]
    
    def get_perspective(self, topic_name, position):
        """Get information about a specific perspective on a topic."""
        topic = self.get_topic_information(topic_name)
        if topic:
            for perspective in topic["perspectives"]:
                if perspective["position"].lower() == position.lower():
                    return perspective
        return None
