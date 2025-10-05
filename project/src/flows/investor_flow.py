from agents.investor_agent import create_investor_crew

def run_investor_flow(command: str):
    crew = create_investor_crew()
    result = crew.run(command)
    print(result)
