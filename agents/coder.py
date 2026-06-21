from .base_agent import BaseAgent


class CoderAgent(BaseAgent):
    def implement(self, plan: str, context: str) -> str:
        return self.call(prompt="P: " + plan + "\nC: " + context)
