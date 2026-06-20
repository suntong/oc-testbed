from .base_agent import BaseAgent
class PlannerAgent(BaseAgent):
    def plan(self, request: str) -> str: return self.call(prompt=request, system="You are a software architect. Output a numbered implementation plan.")