import streamlit as st
from src.Config import Config
from openai import OpenAI

INFO = "ℹ️ Open AI key 有问题，请检查"


def request_llm_custom_msg(
    msg,
    temperature,
    max_tokens,
    emoji,
    api_key=st.session_state.open_ai_api_key,
    base_url=st.session_state.open_ai_base_url,
    model=st.session_state.open_ai_modelname,
):
    try:
        llm = OpenAI(
            api_key=api_key,
            base_url=base_url,
			model=model,
            max_tokens=max_tokens, # token 数
            temperature=temperature, # 模型输出的创意程度 (随机性)
            messages=[{"role": "system", "content": msg}],
        )
    except Exception as e:
        return INFO, "⛔"

    return completion.choices[0].message.content, emoji