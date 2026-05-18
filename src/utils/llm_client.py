==================== 文件：src/utils/llm_client.py ====================
import os
from typing import Optional, Dict, Any
from litellm import completion
from dotenv import load_dotenv

load_dotenv()

class LLMClient:
MODEL_MAP = {
"openai/gpt-4": "openai/gpt-4",
"openai/gpt-4-turbo": "openai/gpt-4-turbo",
"anthropic/claude-3-opus": "anthropic/claude-3-opus",
"deepseek/deepseek-chat": "deepseek/deepseek-chat",
}

def init(self, default_model: str = None):
self.default_model = default_model or os.getenv("MAIN_MODEL", "openai/gpt-4")
self.max_steps = int(os.getenv("MAX_REASONING_STEPS", "15"))

def call(self, prompt: str, model: Optional[str] = None, system_prompt: Optional[str] = None,
temperature: float = 0.7, max_tokens: int = 4096) -> Dict[str, Any]:
selected_model = self.MODEL_MAP.get(model, model or self.default_model)
messages = []
if system_prompt:
messages.append({"role": "system", "content": system_prompt})
messages.append({"role": "user", "content": prompt})
try:
response = completion(model=selected_model, messages=messages, temperature=temperature, max_tokens=max_tokens)
return {
"success": True,
"content": response.choices[0].message.content,
"model": selected_model,
}
except Exception as e:
return {"success": False, "error": str(e)}
