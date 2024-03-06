import streamlit as st



if "OPENAI_API_KEY" not in st.session_state:
    st.session_state["OPENAI_API_KEY"] = "" # 设置输入框的展示值

if "PINECONE_API_KEY" not in st.session_state:
	st.session_state["PINECONE_API_KEY"] = "" # 设置输入框的展示值

if "PINECONE_API_ENDPOINT" not in st.session_state:
	st.session_state["PINECONE_API_ENDPOINT"] = "" # 设置输入框的展示值


# 设置页面标题和布局 
st.set_page_config(page_title="对话 APP", layout="wide")
st.title("对话 APP")