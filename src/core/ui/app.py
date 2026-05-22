==================== 文件：src/ui/app.py ====================
import streamlit as st
import requests
from datetime import datetime

st.set_page_config(page_title="CodeArchitect Lite", page_icon="🏗️", layout="wide")
st.title("🏗️ CodeArchitect Lite")
st.markdown("多智能体长链推理架构设计平台")

with st.sidebar:
api_url = st.text_input("API地址", "http://localhost:8000")
max_rounds = st.slider("最大辩论轮数", 1, 10, 5)

col_left, col_right = st.columns([1, 1])
with col_left:
requirement = st.text_area("请输入需求描述", height=300)
if st.button("开始设计"):
if not requirement:
st.error("请输入需求")
else:
with st.spinner("多智能体协作中..."):
try:
resp = requests.post(f"{api_url}/design", json={"requirement": requirement, "max_rounds": max_rounds}, timeout=180)
if resp.status_code == 200:
st.session_state.result = resp.json()
st.success("完成")
else:
st.error(f"错误 {resp.status_code}")
except Exception as e:
st.error(str(e))

with col_right:
if "result" in st.session_state:
r = st.session_state.result
tab1, tab2, tab3 = st.tabs(["PRD文档", "架构方案", "风险报告"])
with tab1:
st.markdown(r["final_prd"])
with tab2:
st.markdown(r["architecture_design"])
with tab3:
st.markdown(r["risk_report"])
else:
st.info("左侧输入需求，点击「开始设计」")

