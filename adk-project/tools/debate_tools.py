from orchestrate.annotations import tool

@tool
def debate_research(topic: str) -> dict:
    """
    A simple research tool that provides information on debate topics.
    
    Args:
        topic: The topic to research
        
    Returns:
        dict: Information about the topic from multiple perspectives
    """
    # This is a placeholder implementation
    return {
        "topic": topic,
        "perspectives": {
            "scientific": f"Scientific perspective on {topic}",
            "economic": f"Economic perspective on {topic}",
            "social": f"Social perspective on {topic}",
            "political": f"Political perspective on {topic}"
        },
        "facts": [
            f"Fact 1 about {topic}",
            f"Fact 2 about {topic}",
            f"Fact 3 about {topic}"
        ]
    }
