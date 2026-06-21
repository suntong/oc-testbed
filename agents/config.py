import os
import yaml
from dotenv import load_dotenv
load_dotenv()

NVIDIA_API_KEY = os.getenv("NVIDIA_API_KEY", "")
NVIDIA_BASE_URL = os.getenv("NVIDIA_BASE_URL", "https://integrate.api.nvidia.com/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "meta/llama-3.1-8b-instruct")

SKILLS_DIR = os.path.expanduser(
    os.getenv("SKILLS_DIR", "~/.superpowers/skills")
)
AGENTS_CONFIG = os.path.join(os.path.dirname(__file__), "agents.yaml")

def load_agents_config():
    with open(AGENTS_CONFIG) as f:
        return yaml.safe_load(f)
