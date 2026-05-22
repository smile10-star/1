==================== 文件：src/config/model_config.py ====================
from src.utils.llm_client import LLMClient

def get_llm_for_agent(model_name: str):
client = LLMClient()
def llm(prompt):
return client.call(prompt, model=model_name)["content"]
return llm
