from .base_agent import BaseAgent
class ReviewerAgent(BaseAgent):
    def review(self, code: str) -> str: return self.call(prompt=code, system="You are a reviewer. Find bugs.")