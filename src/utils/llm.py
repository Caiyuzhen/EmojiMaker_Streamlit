import streamlit as st
from src.Config import Config
import requests
# from openai import OpenAI
from langchain.llms import
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
# from llamaapi import LlamaAPI


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
	chat = ChatOpenAI(
		base_url="http://127.0.0.1:1234/v1", 
		api_key="EMPTY",
		temperature=0.7,
	)
	# res = chat.invoke("你好, 请告诉我如何做一个完美的荷包蛋")
	# print(res)
 


	# 生成提示词	
	# prompt = ChatPromptTemplate.from_template(template=template)
	chat_template_prompt = ChatPromptTemplate.from_messages(
		[
			("system", "你是一个厨师, 你的任务是回答用户的问题, 请用中文回答。"),
			("human", "Hello, how are you doing?"),
			("ai", "I'm doing well, thanks!"),
			("human", "{user_input}"), # 👈 构建动态的用户输入内容
		]
	)
 
	# 输出解析器和【链】
	output_parser = StrOutputParser()
 
	# 构建 LCEL 链
	chain = (
		chat_template_prompt |
		chat |
		output_parser
	)

	# 动态地定义用户的问题
	user_input = "你好, 请教我怎么做炒鸡蛋这道菜, 用中文回答我"



	# 调用链并传递 user_input (🌟 一般输出) ———————————————————————————————————————————-——————————————————————
	# response = chain.invoke({"user_input": user_input})
	# print(response)
 
 
    # 使用流式调用 (🌟 流式输出) ———————————————————————————————————————————-——————————————————————
	for chunk in chain.stream({"user_input": user_input}):
		print(chunk, end="")
  
  
  
  
	# 👇 OpenAI Python SDK 的调用方式
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