# 1
项目名称：CodeArchitect Lite 一个用多AI工具组合实现的轻量级智能架构辅助工具。  核心痛点 单一AI模型难以兼顾复杂系统的“全局架构”与“细节推演”，且单路推理容易因幻觉导致设计失误。  核心逻辑流（长链推理 + 多Agent协作） 需求解析（ChatGPT GPT-5）→ 将模糊需求转为结构树  双路径架构生成（Claude Opus 正向设计 + DeepSeek 对抗风控）→ 长链推理10~20步  融合择优 → 生成PRD（DeepSeek）  代码骨架生成（Cursor）  多Agent横向互验，纵向长链递推，形成闭环校验。  工具组合 ChatGPT（解析） + Claude（架构） + DeepSeek（校验/文档） + Cursor（代码实现）。  
==================== 文件：README.md ====================
# CodeArchitect Lite

基于多智能体协作与长链推理的智能架构设计平台。

## 核心特性
- 多 Agent 协作：需求解析、架构设计、风险校验、PRD 生成
- 长链推理：支持最多15步深度推理
- 模型自由切换：支持 OpenAI、Anthropic、DeepSeek

## 快速开始

1. 安装依赖
```bash
pip install -r requirements.txt

2.配置环境变量
bash
cp .env.example .env
# 编辑 .env 填入你的 API Key

3.启动后端 API
bash
uvicorn src.api.routes:app --reload --port 8000

4.启动 Web 界面（新终端）
bash
streamlit run src/ui/app.py

5.访问 http://localhost:8501
Docker 一键启动
bash
docker-compose up -d
许可证
MIT
