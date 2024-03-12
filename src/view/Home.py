
from src.utils.llm import request_llm_custom_msg
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.schema import (
	AIMessage,
	HumanMessage,
	SystemMessage
)

from src.utils.getRandomColors import create_emoji_with_bg, get_emoji_from_name, get_random_color


class Homepage:
	@staticmethod # 无需创建类的实例即可调用
	def render():
		st.write("Welcome to the Homepage!")
  
	@staticmethod # 无需创建类的实例即可调用
	def render():
		# 初始化 OpenAI
		hasKEY = False


		# 设置会话存储的兜底值
		if "OPENAI_API_KEY" not in st.session_state:
			st.session_state["OPENAI_API_KEY"] = "123" # 兜底
			# chat = ChatOpenAI(openai_api_key=openAI_api_key) # 有 OpenAI KEY 的话就使用 KEY 来初始化 chat 实例
		if "AI_SERVER_URL" not in st.session_state:
			st.session_state["AI_SERVER_URL"] = "123" # 兜底
		if "OPENAI_MODEL_NAME" not in st.session_state:
			st.session_state["OPENAI_MODEL_NAME"] = "123" # 兜底

		# 如果所有必需的密钥都存在,则设置 hasKEY 为 True
		if (
			st.session_state["OPENAI_API_KEY"]
			and st.session_state["AI_SERVER_URL"]
			and st.session_state["OPENAI_MODEL_NAME"]
		):
			hasKEY = True
		else:
			st.warning("🔑 请设置 OpenAI 的 API Key、OpenAI URL 和模型名称")
			# chat = None  # 确保 chat 变量定义，但不实例化 ChatOpenAI
        
        
		if "PINECONE_API_KEY" not in st.session_state:
			st.session_state["PINECONE_API_KEY"] = "123" # 兜底
		if "PINECONE_API_ENDPOINT" not in st.session_state:
			st.session_state["PINECONE_API_ENDPOINT"] = "123" # 兜底




		# 用 container 分别【显示】设置后的两个 KEY, 👇 st.markdown 可以使用 md 来设置显示的格式
		with st.container():
			st.subheader("🔑 OpenAI KEY")
			st.markdown(f"""
				| OPEN_AI_KEY  |
				| ------------ |
				| {st.session_state["OPENAI_API_KEY"]} |
			""")
			st.markdown('<style>div.block-container{margin-top: 20px;}</style>', unsafe_allow_html=True) # 🔥 使用 html 添加自定义间距
			
		with st.container():
			st.subheader("🔑 Pinecone KEY")
			st.markdown(f"""
				| PINECONE_API_KEY | PINECONE_API_ENDPOINT |
				| -----------------|-----------------------|
				| {st.session_state["PINECONE_API_KEY"]} | {st.session_state["PINECONE_API_ENDPOINT"]} |
			""")



		# 💬 实例化聊天窗口 ————————————————————————————————————————————————————————————————
		if hasKEY: # 如果 chat 存在 (前提是输入了 KEY), 就显示输入框
			with st.container():
				st.subheader("一个聊天窗口")
				prompt = st.text_area("请输入你的问题 (prompt)", value="", height=300, max_chars=None, key=None) # 输入框
				haveAsked = st.button("Ask")
				if haveAsked: # 如果有输入问题, 就显示回答
					# 使用 llm 内的方法, 获取 AI 的输入
					response, emoji = request_llm_custom_msg(
						msg=prompt,
						temperature=0.7,  # 根据需要调整温度
						max_tokens=2048,  # 根据需要调整最大令牌数
						emoji="👌",  # 可选的 emoji
      					base_url=st.session_state["AI_SERVER_URL"],
						api_key=st.session_state["OPENAI_API_KEY"],
					)
					# ai_message = chat([HumanMessage(content=prompt)])
					st.write(ai_message.content) # 显示回答
				st.markdown('<style>div.block-container{margin-bottom: 20px;}</style>', unsafe_allow_html=True) # 🔥 使用 html 添加自定义间距
		if not chat: # 如果 chat 不存在(没有设置 KEY, 就显示提示 banner）
			st.markdown('<style>div.block-container{margin-top: 20px;}</style>', unsafe_allow_html=True) # 🔥 使用 html 添加自定义间距




		# 😄 展示 Emoji 图片 ————————————————————————————————————————————————————————————————
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
  