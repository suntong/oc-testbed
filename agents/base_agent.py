from openai import OpenAI
from .config import NVIDIA_API_KEY, NVIDIA_BASE_URL, MODEL_NAME
class BaseAgent:
    def __init__(self):
        self.client = OpenAI(api_key=NVIDIA_API_KEY, base_url=NVIDIA_BASE_URL)
    def call(self, prompt: str, system: str) -> str:
        try:
            response = self.client.chat.completions.create(model=MODEL_NAME, temperature=0.3, messages=[{"role": "system", "content": system},{"role": "user", "content": prompt}])
            return response.choices[0].message.content
        except Exception as e:
            raise RuntimeError(f"[{self.__class__.__name__}] API Error: {e}")