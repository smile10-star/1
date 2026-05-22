==================== 文件：src/api/routes.py ====================
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Any
from src.core.crew import CodeArchitectCrew

app = FastAPI(title="CodeArchitect API")
architect = CodeArchitectCrew()

class RequirementRequest(BaseModel):
requirement: str
max_rounds: int = 5

class DesignResponse(BaseModel):
requirement_tree: str
architecture_design: str
risk_report: str
final_prd: str
debate_logs: list

@app.get("/health")
async def health():
return {"status": "ok"}

@app.post("/design", response_model=DesignResponse)
async def design(req: RequirementRequest):
try:
if req.max_rounds:
architect.max_debate_rounds = req.max_rounds
result = architect.run(req.requirement)
return DesignResponse(**result)
except Exception as e:
raise HTTPException(status_code=500, detail=str(e))
