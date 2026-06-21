import os
from openai import OpenAI
from .config import NVIDIA_API_KEY, NVIDIA_BASE_URL, MODEL_NAME, SKILLS_DIR, load_agents_config

_CLASS_TO_KEY = {
    "PlannerAgent": "planner",
    "ResearchAgent": "researcher",
    "CoderAgent": "coder",
    "ReviewerAgent": "reviewer",
}

_ALT_SKILLS_DIR = os.path.expanduser("~/.config/opencode/skills")


class BaseAgent:
    def __init__(self):
        self.client = OpenAI(api_key=NVIDIA_API_KEY, base_url=NVIDIA_BASE_URL)
        self.system = self._load_skill_prompt()

    def _load_skill_prompt(self) -> str:
        config = load_agents_config()
        key = _CLASS_TO_KEY.get(self.__class__.__name__)
        if not key:
            raise RuntimeError(
                "Unknown agent class: " + self.__class__.__name__
            )
        agent_config = config.get("agents", {}).get(key)
        if not agent_config:
            raise RuntimeError("No config for agent: " + key)
        skill_name = agent_config["skill"]
        skill_file = os.path.join(SKILLS_DIR, skill_name, "SKILL.md")
        if not os.path.isfile(skill_file):
            alt_file = os.path.join(_ALT_SKILLS_DIR, skill_name, "SKILL.md")
            if os.path.isfile(alt_file):
                skill_file = alt_file
            else:
                raise RuntimeError(
                    "Skill file not found: " + skill_file
                    + " (also tried: " + alt_file + ")"
                )
        with open(skill_file) as f:
            content = f.read()
        return self._strip_frontmatter(content)

    @staticmethod
    def _strip_frontmatter(content: str) -> str:
        lines = content.split("\n")
        if lines and lines[0].strip() == "---":
            end = 1
            while end < len(lines) and lines[end].strip() != "---":
                end += 1
            if end < len(lines):
                return "\n".join(lines[end + 1 :]).strip()
        return content.strip()

    def call(self, prompt: str, system: str | None = None) -> str:
        try:
            response = self.client.chat.completions.create(
                model=MODEL_NAME,
                temperature=0.3,
                messages=[
                    {"role": "system", "content": system or self.system},
                    {"role": "user", "content": prompt},
                ],
            )
            return response.choices[0].message.content
        except Exception as e:
            raise RuntimeError(
                "[" + self.__class__.__name__ + "] API Error: " + str(e)
            )
