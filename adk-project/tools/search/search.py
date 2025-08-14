from orchestrate.annotations import tool

@tool
def search(query: str) -> dict:
    """
    A simple search tool that returns information about a given query.
    
    Args:
        query: The search query
        
    Returns:
        dict: Information related to the search query
    """
    # In a real implementation, this would connect to a search API
    # For now, we'll return some placeholder data
    return {
        "query": query,
        "results": [
            {
                "title": f"Information about {query}",
                "snippet": f"This is some information about {query} that would be useful for debates.",
                "source": "Debate Knowledge Base"
            },
            {
                "title": f"Alternative perspectives on {query}",
                "snippet": f"Different viewpoints about {query} including pros and cons.",
                "source": "Multiple Perspective Analysis"
            }
        ],
        "status": "success"
    }
