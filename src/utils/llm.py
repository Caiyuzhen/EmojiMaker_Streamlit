import streamlit as st
from src.Config import Config
import requests
from openai import OpenAI


INFO = "ℹ️ Open AI key 有问题，请检查"


def request_llm_custom_msg(
	api_key,
	inputMsg,
	temperature,
	server_url,
	model,
	max_tokens,
):
	# 使用 OpenAI 客户端加载模型
	client = OpenAI(base_url=server_url, api_key=api_key)
	try:
		completion = client.chat.completions.create(
			api_key=api_key,
			temperature=temperature, # 模型输出的创意程度 (随机性)
			server_url=server_url,
			model=model,
			messages=[
				{"role": "system", "content": "Please answer the user's question."},
				{"role": "user", "content": inputMsg},
			],
			max_tokens=max_tokens,
		)
		# 返回模型的回答
		return completion.choices[0].message['content'], "OK 👍"
	except Exception as e:
			return f"Error: {str(e)}", "⛔"