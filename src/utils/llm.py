import streamlit as st
from src.Config import Config
from openai import OpenAI

INFO = "ℹ️ Open AI key 有问题，请检查"


def request_llm_custom_msg(
    msg,
    temperature,
    emoji,
    api_key=st.session_state.open_ai_api_key,
    base_url=st.session_state.open_ai_base_url,
    model=st.session_state.open_ai_modelname,
):
    try:
        client = OpenAI(
            api_key=api_key,
            base_url=base_url,
        )
        completion = client.chat.completions.create(
            model=model,
            messages=[{"role": "system", "content": msg}],
            temperature=temperature,
        )
    except Exception as e:
        return INFO, "⛔"

    return completion.choices[0].message.content, emoji