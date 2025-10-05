from agents.researcher_agent import create_researcher_crew

def run_researcher_flow(query: str):
    crew = create_researcher_crew()
    result = crew.run(query)
    print(result)
    