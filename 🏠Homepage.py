import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.schema import (
	AIMessage,
	HumanMessage,
	SystemMessage
)


# 初始化 OpenAI
chat = None


# 设置会话存储的兜底值
if "OPENAI_API_KEY" not in st.session_state:
    st.session_state["OPENAI_API_KEY"] = "" # 设置输入框的展示值
else:
    chat = ChatOpenAI(openai_api_key=st.session_state["OPENAI_API_KEY"]) # 有 OpenAI KEY 的话就使用 KEY 来初始化 chat 实例
    

if "PINECONE_API_KEY" not in st.session_state:
	st.session_state["PINECONE_API_KEY"] = "" # 设置输入框的展示值

if "PINECONE_API_ENDPOINT" not in st.session_state:
	st.session_state["PINECONE_API_ENDPOINT"] = "" # 设置输入框的展示值


# 设置页面标题和布局 
st.set_page_config(page_title="对话 APP", layout="wide")
st.title("💬 Chat APP")
st.markdown('<style>div.block-container{margin-top: 20px;}</style>', unsafe_allow_html=True) # 🔥 使用 html 添加自定义间距


# 用 container 分别【显示】设置后的两个 KEY
# 👇 st.markdown 可以使用 md 来设置显示的格式
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



# 💬 实例化聊天窗口
if chat: # 如果 chat 存在 (前提是输入了 KEY), 就显示输入框
	with st.container():
		st.header("一个聊天窗口")
		prompt = st.text_area("请输入你的问题 (prompt)", value="", height=300, max_chars=None, key=None) # 输入框
		haveAsked = st.button("Ask")
		if haveAsked: # 如果有输入问题, 就显示回答
			ai_message = chat([HumanMessage(content=prompt)])
			st.write(ai_message.content) # 显示回答
		st.markdown('<style>div.block-container{margin-bottom: 20px;}</style>', unsafe_allow_html=True) # 🔥 使用 html 添加自定义间距
if not chat: # 如果 chat 不存在(没有设置 KEY, 就显示提示 banner）
	st.markdown('<style>div.block-container{margin-top: 20px;}</style>', unsafe_allow_html=True) # 🔥 使用 html 添加自定义间距
	st.warning("请设置 OpenAI 的 API Key") # 显示提示信息
    

