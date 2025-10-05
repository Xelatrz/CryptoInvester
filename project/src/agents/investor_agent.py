from crewai import Agent, Crew
from tools.wallet import buy, sell, get_balance, get_portfolio_value, list_holdings

def create_investor_crew():
    investor = Agent(
        role="Crypto Investor",
        goal="Execute trades based on user instructions",
        backstory="You manage digital asset portfolios.",
        tools=[buy, sell, get_balance, get_portfolio_value, list_holdings]
    )
    return Crew(agents=[investor])
