import streamlit as st




class PineconeSettingPage:
	def __init__(self):
		# 初始化类时, 设置 session 会话存储的兜底值
		if "PINECONE_API_KEY" not in st.session_state:
			st.session_state["PINECONE_API_KEY"] = "123" # 设置输入框的展示值
		if "PINECONE_API_ENDPOINT" not in st.session_state:
			st.session_state["PINECONE_API_ENDPOINT"] = "123" # 设置输入框的展示值

	@staticmethod # 无需创建类的实例即可调用
	def render():
		# 设置页面标题和布局
		st.subheader("Pinecone 设置") # 页面大标题

		# 设置 API 变量 = 从【输入框】拿到值, 值从会话状态 session_state 中获取
		PINECONE_API_KEY = st.text_input("请输入 API_Key", value=st.session_state["PINECONE_API_KEY"], max_chars=None, key=None, type='password')
		PINECONE_API_ENDPOINT = st.text_input("请输入 API Endpoint", value=st.session_state["PINECONE_API_ENDPOINT"], max_chars=None, key=None, type='password')


		# 保存按钮
		saved = st.button("Save", key="save_button_tab2")

		# 按钮
		if saved:
			st.session_state["PINECONE_API_KEY"] = PINECONE_API_KEY
			st.session_state["PINECONE_API_ENDPOINT"] = PINECONE_API_ENDPOINT
   
# st.set_page_config(page_title="Pinecone 设置", layout="wide") # 🔥 set_page_config 必须是第一个命令!