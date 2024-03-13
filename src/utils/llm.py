import streamlit as st
from src.Config import Config
import requests
# from openai import OpenAI
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


INFO = "ℹ️ Open AI key 有问题，请检查"


def request_llm_custom_msg(
	api_key,
	inputMsg, # 用户输入的问题
	temperature,
	server_url, # 服务 URL
	model,
	max_tokens,
):
	# 使用 OpenAI 客户端加载模型
	llm = ChatOpenAI(
		base_url=server_url, 
		api_key=api_key,
		temperature=temperature,
	)

	# 构造提示词模板
	template = """
		你是一个聊天机器人，你的任务是回答用户的问题。

		用户的问题是：
		“{{question}}”。
			
		请回答用户的问题, 并在每次回答后都说 “啦啦啦我回答完啦！”
	"""

	# 生成提示词	
	prompt = PromptTemplate(template)
 
	# 构造输出解析器和【链】
	output_parser = StrOutputParser()
 
	# 调用链, 获取回答
	chain = prompt | llm | output_parser


	response = chain.invoke({"question": inputMsg})
	st.info(response)
 
	# 返回模型的回答
	return response, "OK 👍"

	# try:
	# 	completion = llm.chat.completions.create(
	# 		api_key=api_key,
	# 		temperature=temperature, # 模型输出的创意程度 (随机性)
	# 		server_url=server_url,
	# 		model=model,
	# 		messages=[
	# 			{"role": "system", "content": "Please answer the user's question."},
	# 			{"role": "user", "content": inputMsg},
	# 		],
	# 		max_tokens=max_tokens,
	# 	)
	# 	# 返回模型的回答
	# 	return completion.choices[0].message['content'], "OK 👍"
	# except Exception as e:
	# 		return f"Error: {str(e)}", "⛔"