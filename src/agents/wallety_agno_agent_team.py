from textwrap import dedent
from typing import Optional

from agents.wallety_team.constants import WalletyAgentConstants
from agents.wallety_team.wallety_helpdesk_agent import WalletyHelpdeskAgentService

from agno.agent import Agent
from agno.models.ollama import Ollama

class WalletyAgentTeam(WalletyAgentConstants):
    def __init__(self):
        super().__init__()

    def get_wallety_agno_agent_team(
        self,
        user_id: Optional[str] = None,
        session_id: Optional[str] = None
    ) -> Agent:
       return Agent(
            team=[WalletyHelpdeskAgentService().get_wallety_helpdesk_agent(user_id, session_id)],
            model=Ollama(id=self.TOOL_MODEL),
            description=dedent("""\
                A comprehensive description of what the customer is requesting with clear information and service insights.
            """),
            instructions=dedent("""\
                You are the lead customer support of a prestigious financial services platform! 📰

                Your role:
                1. Coordinate between the helpdesk agent and transation assistant
                2. Combine their findings into a compelling narrative
                3. Ensure all information is properly sourced and verified
                4. Present a correct view of information needed by the customer
                5. Highlight key risks and opportunities

            """),
            add_datetime_to_instructions=True,
            show_tool_calls=True,
            markdown=True
        )