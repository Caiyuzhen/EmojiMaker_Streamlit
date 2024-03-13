
import streamlit as st
from src.Config import Config
from src.utils.llm import request_llm_custom_msg
from langchain_openai import ChatOpenAI
from langchain.schema import (
	AIMessage,
	HumanMessage,
	SystemMessage
)

from src.utils.getRandomColors import create_emoji_with_bg, get_emoji_from_name, get_random_color
import os
from dotenv import load_dotenv


class Homepage:
	# __init__
	def __init__(self):
		Config.init_env() # 更新 .env 的配置
 
	@staticmethod # 无需创建类的实例即可调用
	def render():
		# 👇 每次渲染页面前，先从配置文件重新加载最新配置
		Config.init_env()
		# hasKEY = False # 如果所有必需的密钥都存在,则设置 hasKEY 为 True
		# if (st.session_state.get("OPENAI_API_KEY") and st.session_state["OPENAI_API_KEY"] != "XXX" and
		# 	st.session_state.get("AI_SERVER_URL") and st.session_state["AI_SERVER_URL"] != "XXX" and
		# 	st.session_state.get("AI_MODEL_NAME") and st.session_state["AI_MODEL_NAME"] != "XXX"):
		# 	hasKEY = True
		# 	# print("🔑🔑🔑 KEY 都齐全了: ", hasKEY)
		# else:
		# 	st.warning("🔑 请设置 OpenAI 的 API Key、OpenAI URL 和模型名称")
		# 	# chat = None  # 确保 chat 变量定义，但不实例化 ChatOpenAI


		# 用 container 分别【显示】设置后的信息, st.markdown 可以使用 md 来设置显示的格式
		with st.container():
			st.subheader("OPENAI SETTINGS INFO")
			st.markdown(f"""
				| OPENAI_API_KEY | AI_MODEL_NAME |
				| -----------------|-----------------------|
				| {st.session_state["OPENAI_API_KEY"]} | {st.session_state["AI_MODEL_NAME"]} |
			""")
			st.markdown('<style>div.block-container{margin-top: 20px;}</style>', unsafe_allow_html=True) # 🔥 使用 html 添加自定义间距


		# 💬 实例化聊天窗口 ————————————————————————————————————————————————————————————————
		with st.container():
			st.subheader("一个聊天窗口")
			prompt = st.text_area("请输入你的问题 (prompt)", value="", height=300, max_chars=None, key=None) # 输入框
			if st.button("📮 发送问题"): # 如果有点击发送问题的按钮, 就调用 llm, 显示回答
				if prompt:
					print("👀 拿到了 URL: ", Config.get_env("AI_SERVER_URL"))
					response = request_llm_custom_msg( # 使用 llm 内的方法, 获取 AI 的输入
						api_key=st.session_state["OPENAI_API_KEY"],
						temperature=0.7,  # 根据需要调整温度
						server_url=st.session_state["AI_SERVER_URL"],
						model=st.session_state["AI_MODEL_NAME"],
						inputMsg=prompt,
						max_tokens=2048,  # 根据需要调整最大令牌数
					)
					# ai_message = chat([HumanMessage(content=prompt)])
					st.write(response) # 显示回答
					st.markdown('<style>div.block-container{margin-bottom: 20px;}</style>', unsafe_allow_html=True) # 🔥 使用 html 添加自定义间距
     
		# if not hasKEY: # 如果 chat 不存在(没有设置 KEY, 就显示提示 banner）
			# st.markdown('<style>div.block-container{margin-top: 20px;}</style>', unsafe_allow_html=True) # 🔥 使用 html 添加自定义间距


		# 点击获取 session_state 的值 (调试用)
		# if st.button("Show session_state"):
		# 	api_key2 = Config.get_env("OPENAI_API_KEY")
		# 	print("👀 拿到了 KEY: ", api_key2)
		# 	print("---")
  


		# 😄 实例化展示 Emoji 图片的窗口 ————————————————————————————————————————————————————————————————
		# with st.container():
		# 	st.subheader("Change Object Name to Emoji")
		# 	object_name = st.text_input("请输入物体名称(例如: 猫)", value="", max_chars=None, key="object_input", type='default')
		# 	find_emoji = st.button("Generate Emoji")

		# 	if object_name and find_emoji: # 如果有输入物体名称 且 点了按钮
		# 		# 调用函数, 传入物体名称, 返回 emoji
		# 		emoji_path = get_emoji_from_name(object_name) # 传入名词, 返回 emoji 图片路径
		# 		if emoji_path:
		# 			picture = create_emoji_with_bg(emoji_path, 16) # 传入 emoji 图片路径、padding, 返回带有随机背景色的图片
		# 			st.image(picture, width=100)
		# 			# st.image(emoji_path, width=100) # 显示 emoji 图片
		# 		else:
		# 			st.warning("🤷‍♂️ 没有找到对应的 emoji 图片")
		
		# 		# 调用函数, 返回随机背景色
		# 		background_colors = get_random_color()
  