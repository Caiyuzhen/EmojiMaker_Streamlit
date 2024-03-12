# 安装依赖
`pip3 install streamlit`
`pip3 install -q -U langchain openai tiktoken pinecone-client langchain-openai`
`pip3 install Pillow`

# 维护依赖
`pip3 freeze > requirements.txt`

# 启动项目
`streamlit run main.py`
 
# 部署
`share.streamlit.io`

# 使用 Poetry 管理依赖
## 初始化
`pip3 install poetry`
- 未有项目
  - 新建: `poetry new my-project`
- 已有项目
  - c初始化: `poetry init`
- 添加依赖: `poetry add`
  -比如: poetry add langchain-openai
## 进入虚拟环境
`poetry shell`
## 启动项目
`streamlit run main.py`