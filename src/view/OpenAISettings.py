import streamlit as st
from src.Config import Config
from src.view.Home import Homepage




class OpenAISettingsPage:
	def __init__(self, ):
		# 初始化类时，确保会话状态已设置
		if "OPENAI_API_KEY" not in st.session_state:
			st.session_state["OPENAI_API_KEY"] = "123" # 设置输入框的展示值

	@staticmethod # 无需创建类的实例即可调用
	def render():
		# 设置页面标题
		st.subheader("OpenAI 设置") # 页面大标题1

		# API 变量, 值从会话状态 session_state 中获取
		OPENAI_API_KEY = st.text_input("请输入 API Key", value=st.session_state.get("OPENAI_API_KEY", "XXX"), max_chars=None, key="api_key_input", type='default')
		OPENAI_URL = st.text_input("请输入 AI SERVER URL", value=st.session_state.get("AI_SERVER_URL", "XXX"), max_chars=None, key="url_input", type='default')
		AI_MODEL_NAME = st.text_input("请输入 OpenAI Model Name", value=st.session_state.get("AI_MODEL_NAME", "XXX"), max_chars=None, key="model_name_input", type='default')

		# 保存按钮
		saved = st.button("Save", key="save_button_tab1")

		# 保存在会话状态中 (会话关闭后就没了)
		if saved:
			st.session_state["OPENAI_API_KEY"] = OPENAI_API_KEY
			st.session_state["OPENAI_URL"] = OPENAI_URL
			st.session_state["AI_MODEL_NAME"] = AI_MODEL_NAME
			st.success("✅ API Key 已保存")
   
			# 【实例化】配置对象并保存到 .env 文件中
			config = Config()
			config.check_and_saveTo_config('OPENAI_API_KEY', OPENAI_API_KEY)
			config.check_and_saveTo_config('AI_SERVER_URL', OPENAI_URL)
			config.check_and_saveTo_config('AI_MODEL_NAME', AI_MODEL_NAME)
			st.success("✅ 配置已保存")
   
			# 更新配置信息
			Config.init_env()

		# 点击获取 session_state 的值 (调试用)
		if st.button("Show session_state", key="show_session_state_button"):
			st.write(st.session_state)


# st.set_page_config(page_title="OpenAI 设置", layout="wide") # 🔥 set_page_config 必须是第一个命令!