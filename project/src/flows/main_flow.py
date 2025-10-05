from flows.researcher_flow import run_researcher_flow
from flows.investor_flow import run_investor_flow

def run_main_flow():
    user_input = input("Would you like to invest, or do you want to ask a question about a crypto related curiosity?")
    # change this so that i can ask to invest after researching, instead of relying on a prompt at the start of the conversation.

    if "invest" in user_input.lower():
        run_investor_flow(user_input)
    else:
        run_researcher_flow(user_input)
        