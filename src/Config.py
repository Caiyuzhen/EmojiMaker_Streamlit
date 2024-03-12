import os
import streamlit as st
from dotenv import load_dotenv


# 统一管理配置的参数
class Config:
	def __init__(
		self,
		OPENAI_API_KEY=None, 
		AI_SERVER_URL=None,
		AI_MODEL_NAME=None,
	) :
		self.OPENAI_API_KEY = OPENAI_API_KEY
		self.AI_SERVER_URL = AI_SERVER_URL
		self.AI_MODEL_NAME = AI_MODEL_NAME

	# 检查 KEY 是否有效, 是否在 KEY 列表中 (进一步的可以去做打印 log 的操作)
	def check_and_saveTo_config(self, attr, value):
		if not hasattr(self, attr):
			raise AttributeError(f"❌ Config 中没有此属性: {attr}")
		# 若合法, 则保存为实例属性
		setattr(self, attr, value)
		self.save_to_env(attr, value)

	# 修改环境变量的配置的具体方法
	def save_to_env(self, attr, value):
		# 首先加载现有的.env文件内容
		env_dict = {}
		try:
			with open(".env", "r") as file:
				for line in file:
					if "=" in line:
						key, val = line.strip().split("=", 1)
						env_dict[key] = val
		except FileNotFoundError:
			print("⚠️ .env 文件不存在，将创建一个新文件。")

		# 更新指定的配置项
		env_dict[attr] = value

		# 将更新后的内容写回.env文件
		with open(".env", "w") as file:
			for key, val in env_dict.items():
				file.write(f"{key}={val}\n")
		# print("👍 保存配置到 .env 文件")
   
   
   	# 读取 .env 配置文件
	@staticmethod # 无需创建类的实例即可调用
	def load_env():
		# 读取环境变量
		load_dotenv()
		OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
		AI_SERVER_URL = os.environ.get("AI_SERVER_URL")
		AI_MODEL_NAME = os.environ.get("AI_MODEL_NAME")
		# print("🔑🔑🔑🔑🔑 拿到了 KEY: ", OPENAI_API_KEY)
  
  		# 设置会话存储
		if "OPENAI_API_KEY" not in st.session_state:
			st.session_state["OPENAI_API_KEY"] = OPENAI_API_KEY # 兜底
			# chat = ChatOpenAI(openai_api_key=openAI_api_key) # 有 OpenAI KEY 的话就使用 KEY 来初始化 chat 实例
		if "AI_SERVER_URL" not in st.session_state:
			st.session_state["AI_SERVER_URL"] = AI_SERVER_URL # 兜底
		if "AI_MODEL_NAME" not in st.session_state:
			st.session_state["AI_MODEL_NAME"] = AI_MODEL_NAME # 兜底
   

