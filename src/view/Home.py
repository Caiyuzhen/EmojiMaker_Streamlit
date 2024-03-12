
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



class Homepage:
    # __init__
	def __init__(self):
		# 实例化时初始化环境, 实例属性
		self.config = Config.load_env()
  
	def update_config(self, new_config):
		self.config = new_config
 
	def render(self):
		hasKEY = False # 如果所有必需的密钥都存在,则设置 hasKEY 为 True
		if (
			st.session_state["OPENAI_API_KEY"]
			and st.session_state["AI_SERVER_URL"]
			and st.session_state["AI_MODEL_NAME"]
		):
			hasKEY = True
			# print("🔑🔑🔑 KEY 都齐全了: ", hasKEY)
		else:
			st.warning("🔑 请设置 OpenAI 的 API Key、OpenAI URL 和模型名称")
			# chat = None  # 确保 chat 变量定义，但不实例化 ChatOpenAI


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
		if hasKEY: # 如果 chat 存在 (前提是输入了 KEY), 就显示输入框
			with st.container():
				st.subheader("一个聊天窗口")
				prompt = st.text_area("请输入你的问题 (prompt)", value="", height=300, max_chars=None, key=None) # 输入框
				haveAsked = st.button("📮 发送问题",)
				if prompt:
					print("👉拿到了 URL: ", st.session_state["AI_SERVER_URL"])
					if haveAsked: # 如果有点击发送问题的按钮, 就调用 llm, 显示回答
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
		if not hasKEY: # 如果 chat 不存在(没有设置 KEY, 就显示提示 banner）
			st.markdown('<style>div.block-container{margin-top: 20px;}</style>', unsafe_allow_html=True) # 🔥 使用 html 添加自定义间距




		# 😄 实例化展示 Emoji 图片的窗口 ————————————————————————————————————————————————————————————————
		with st.container():
			st.subheader("Change Object Name to Emoji")
			object_name = st.text_input("请输入物体名称(例如: 猫)", value="", max_chars=None, key="object_input", type='default')
			find_emoji = st.button("Generate Emoji")

			if object_name and find_emoji: # 如果有输入物体名称 且 点了按钮
				# 调用函数, 传入物体名称, 返回 emoji
				emoji_path = get_emoji_from_name(object_name) # 传入名词, 返回 emoji 图片路径
				if emoji_path:
					picture = create_emoji_with_bg(emoji_path, 16) # 传入 emoji 图片路径、padding, 返回带有随机背景色的图片
					st.image(picture, width=100)
					# st.image(emoji_path, width=100) # 显示 emoji 图片
				else:
					st.warning("🤷‍♂️ 没有找到对应的 emoji 图片")
		
				# 调用函数, 返回随机背景色
				background_colors = get_random_color()
  