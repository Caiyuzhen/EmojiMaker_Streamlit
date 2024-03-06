import streamlit as st



# 设置输入框的兜底值
if "OPENAI_API_KEY" not in st.session_state:
	st.session_state["OPENAI_API_KEY"] = "" # 设置输入框的展示值


# 设置页面标题和布局
st.set_page_config(page_title="OpenAI 设置", layout="wide") # 🔥 set_page_config 必须是第一个命令!
st.title("OpenAI 设置") # 页面大标题


# API 变量, 值从会话状态 session_state 中获取
openAI_api_key = st.text_input("请输入 API Key", value=st.session_state["OPENAI_API_KEY"], max_chars=None, key=None, type='default')


# 保存按钮
saved = st.button("Save")


# 保存在会话状态中 (会话关闭后就没了)
if saved:
    st.session_state["OPENAI_API_KEY"] = openAI_api_key