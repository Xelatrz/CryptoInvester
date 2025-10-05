from crewai import Crew, Agent
from tools.coin import get_price, get_market_data, search_coin


def create_researcher_crew():
    researcher = Agent(
        role="Crypto Researcher",
        goal="Provide detailed analysis of cryptocurrency tokens",
        backstory="You are an expert in crypto markets.",
        tools=[get_price, get_market_data, search_coin]
    ) 

    return Crew(agents=[researcher])
