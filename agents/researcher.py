from .base_agent import BaseAgent


class ResearchAgent(BaseAgent):
    def lookup(self, topic: str) -> str:
        return self.call(prompt=topic)
