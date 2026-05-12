# 1
项目名称：CodeArchitect Lite 一个用多AI工具组合实现的轻量级智能架构辅助工具。  核心痛点 单一AI模型难以兼顾复杂系统的“全局架构”与“细节推演”，且单路推理容易因幻觉导致设计失误。  核心逻辑流（长链推理 + 多Agent协作） 需求解析（ChatGPT GPT-5）→ 将模糊需求转为结构树  双路径架构生成（Claude Opus 正向设计 + DeepSeek 对抗风控）→ 长链推理10~20步  融合择优 → 生成PRD（DeepSeek）  代码骨架生成（Cursor）  多Agent横向互验，纵向长链递推，形成闭环校验。  工具组合 ChatGPT（解析） + Claude（架构） + DeepSeek（校验/文档） + Cursor（代码实现）。  
