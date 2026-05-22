==================== 文件：src/core/crew.py ====================
import os
from typing import Dict, Any
from dotenv import load_dotenv
from src.utils.llm_client import LLMClient

load_dotenv()

class CodeArchitectCrew:
def init(self):
self.llm = LLMClient()
self.max_debate_rounds = int(os.getenv("MAX_DEBATE_ROUNDS", "5"))

def _call_agent(self, agent_role: str, task_desc: str) -> str:
system_prompt = f"你是{agent_role}。请完成任务。"
return self.llm.call(task_desc, system_prompt=system_prompt)["content"]

def run(self, requirement: str) -> Dict[str, Any]:

Phase 1: 需求解析
req_tree = self._call_agent("需求分析专家", f"将以下需求转为结构化JSON树：\n{requirement}")

Phase 2: 架构生成
arch = self._call_agent("系统架构师", f"基于需求树设计架构：\n{req_tree}")

Phase 3: 风险评估
risk = self._call_agent("风控校验官", f"评估以下架构的风险：\n{arch}")

Phase 4: 多轮辩论融合
final_arch = arch
for i in range(self.max_debate_rounds):
decision = self._call_agent("设计评审主席", f"架构：{final_arch}\n风险：{risk}\n判断是否通过（仅回复'通过'或'不通过'）：")
if "通过" in decision:
break
final_arch = self._call_agent("系统架构师", f"根据以下风险优化架构：\n{risk}\n原架构：{final_arch}")

Phase 5: PRD生成
prd = self._call_agent("技术文档撰写师", f"基于最终架构生成PRD：\n{final_arch}")
return {
"requirement_tree": req_tree,
"architecture_design": arch,
"risk_report": risk,
"final_prd": prd,
"debate_logs": [{"final_architecture": final_arch}]
}
