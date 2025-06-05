from agno.playground import Playground

from agents.web_agent import WalletyWebAgentService

######################################################
## Routes for the Playground Interface
######################################################

# Get Agents to serve in the playground
web_agent = WalletyWebAgentService().get_web_agent(debug_mode=True)

# Create a playground instance
playground = Playground(agents=[web_agent])

# Get the router for the playground
playground_router = playground.get_async_router()
