from .base_agent import BaseAgent
class CoderAgent(BaseAgent):
    def implement(self, plan: str, context: str) -> str: return self.call(prompt=f"P: {plan}\nC: {context}", system="You are an engineer. Code only.")