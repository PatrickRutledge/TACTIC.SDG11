"""
Debate Flow Module

Defines flow patterns for different types of debates in the multi-agent debate system.
"""

class DebateFlow:
    """Base class for all debate flows."""
    
    def __init__(self, name, description):
        """Initialize a debate flow.
        
        Args:
            name (str): The name of the flow.
            description (str): The description of the flow.
        """
        self.name = name
        self.description = description
        self.phases = []
        self.current_phase = None
        self.participants = []
        self.moderator = None
        self.topic = None
        
    def setup(self, topic, moderator, participants):
        """Set up the debate flow.
        
        Args:
            topic (str): The topic of the debate.
            moderator (str): The moderator of the debate.
            participants (list): The participants in the debate.
            
        Returns:
            dict: Information about the flow setup.
        """
        self.topic = topic
        self.moderator = moderator
        self.participants = participants
        self.current_phase = 0 if self.phases else None
        
        return {
            "flow": self.name,
            "topic": topic,
            "moderator": moderator,
            "participants": participants,
            "phases": [p["name"] for p in self.phases],
            "status": "ready"
        }
    
    def next_phase(self):
        """Move to the next phase of the debate.
        
        Returns:
            dict: Information about the next phase.
        """
        if self.current_phase is None:
            return {"status": "error", "message": "No phases defined"}
        
        if self.current_phase >= len(self.phases) - 1:
            return {"status": "complete", "message": "Debate is complete"}
        
        self.current_phase += 1
        return {
            "status": "success",
            "phase": self.phases[self.current_phase]["name"],
            "instructions": self.phases[self.current_phase]["instructions"]
        }
    
    def current_phase_info(self):
        """Get information about the current phase.
        
        Returns:
            dict: Information about the current phase.
        """
        if self.current_phase is None:
            return {"status": "error", "message": "No phases defined"}
        
        return {
            "phase": self.phases[self.current_phase]["name"],
            "instructions": self.phases[self.current_phase]["instructions"],
            "progress": f"{self.current_phase + 1}/{len(self.phases)}"
        }


class StructuredDebateFlow(DebateFlow):
    """A structured debate flow with formal phases."""
    
    def __init__(self):
        """Initialize a structured debate flow."""
        super().__init__(
            "structured",
            "A formal debate with clear rules, timed responses, and organized structure."
        )
        
        self.phases = [
            {
                "name": "opening_statements",
                "instructions": "Each participant presents their initial position on the topic."
            },
            {
                "name": "cross_examination",
                "instructions": "Participants question each other's positions and arguments."
            },
            {
                "name": "rebuttal",
                "instructions": "Participants respond to criticisms and strengthen their arguments."
            },
            {
                "name": "closing_statements",
                "instructions": "Each participant summarizes their position and key arguments."
            }
        ]


class RoundtableDebateFlow(DebateFlow):
    """A roundtable discussion flow with less formal structure."""
    
    def __init__(self):
        """Initialize a roundtable debate flow."""
        super().__init__(
            "roundtable",
            "An open discussion format where agents freely contribute perspectives on the topic."
        )
        
        self.phases = [
            {
                "name": "introduction",
                "instructions": "Moderator introduces the topic and participants."
            },
            {
                "name": "initial_perspectives",
                "instructions": "Each participant briefly shares their initial perspective."
            },
            {
                "name": "open_discussion",
                "instructions": "Free-flowing discussion moderated to ensure all perspectives are heard."
            },
            {
                "name": "synthesis",
                "instructions": "Moderator guides the group toward identifying common ground and key differences."
            },
            {
                "name": "closing_thoughts",
                "instructions": "Each participant shares final thoughts on the topic."
            }
        ]


class PointCounterpointDebateFlow(DebateFlow):
    """A point-counterpoint debate flow focusing on specific arguments."""
    
    def __init__(self):
        """Initialize a point-counterpoint debate flow."""
        super().__init__(
            "point_counterpoint",
            "A back-and-forth format focusing on specific arguments and counter-arguments."
        )
        
        self.phases = [
            {
                "name": "topic_framing",
                "instructions": "Moderator frames the topic and explains the format."
            },
            {
                "name": "position_statements",
                "instructions": "Each side presents their initial position in brief statements."
            },
            {
                "name": "point_phase",
                "instructions": "First side presents a key point or argument."
            },
            {
                "name": "counterpoint_phase",
                "instructions": "Second side responds directly to the point with a counterpoint."
            },
            {
                "name": "clarification",
                "instructions": "Brief exchange to clarify positions and address misunderstandings."
            },
            {
                "name": "role_swap",
                "instructions": "Sides swap roles, with the second side now presenting a point."
            },
            {
                "name": "summary",
                "instructions": "Moderator summarizes the key points and counterpoints discussed."
            }
        ]


def get_debate_flow(flow_name):
    """Get a debate flow by name.
    
    Args:
        flow_name (str): The name of the flow.
        
    Returns:
        DebateFlow: The requested debate flow.
    """
    flows = {
        "structured": StructuredDebateFlow(),
        "roundtable": RoundtableDebateFlow(),
        "point_counterpoint": PointCounterpointDebateFlow()
    }
    
    return flows.get(flow_name.lower())
