import streamlit as st
from src.Config import Config




class OpenAISettingsPage:
	def __init__(self):
		# 初始化类时，确保会话状态已设置
		if "OPENAI_API_KEY" not in st.session_state:
			st.session_state["OPENAI_API_KEY"] = "123" # 设置输入框的展示值

	def render(): # 无需创建类的实例即可调用
		# 设置页面标题
		st.subheader("OpenAI 设置") # 页面大标题1

		# API 变量, 值从会话状态 session_state 中获取
		OPENAI_API_KEY = st.text_input("请输入 API Key", value=st.session_state["OPENAI_API_KEY"], max_chars=None, key=None, type='password')
		OPENAI_URL = st.text_input("请输入 OpenAI URL", value="", max_chars=None, key=None, type='default')
		OPENAI_MODEL_NAME = st.text_input("请输入 OpenAI Model Name", value="", max_chars=None, key=None, type='default')

		# 保存按钮
		saved = st.button("Save", key="save_button_tab1")

		# 保存在会话状态中 (会话关闭后就没了)
		if saved:
			st.session_state["OPENAI_API_KEY"] = OPENAI_API_KEY
			st.session_state["OPENAI_URL"] = OPENAI_URL
			st.session_state["OPENAI_MODEL_NAME"] = OPENAI_MODEL_NAME
			st.success("✅ API Key 已保存")
			# 创建配置对象并保存到 .env 文件中
			config = Config(openai_api_key=OPENAI_API_KEY)
			config.save_to_env()
   
   
# st.set_page_config(page_title="OpenAI 设置", layout="wide") # 🔥 set_page_config 必须是第一个命令!