import streamlit as st
import streamlit.components.v1 as components
from PIL import Image, ImageDraw
from src.view.Home import Homepage
from src.view.OpenAISettings import OpenAISettingsPage



# 设置页面标题和布局 
st.set_page_config(page_title="对话 APP", layout="wide")
st.title("💬 Chat APP")
st.markdown('<style>div.block-container{margin-top: 20px;}</style>', unsafe_allow_html=True) # 🔥 使用 html 添加自定义间距



# 根据选择渲染页面
def render():
	# 页面选择器
	tab1, tab2 = st.tabs(["🏠 Homepage", "🤖 OpenAISettings"])
	custom_css = """
	<style>
		/* Tab */
		[data-baseweb="tab"] {
			color: #adb5bd !important;
			margin-right: 14px !important;
		}

		/* Tab 选中 */
		[data-baseweb="tab"][aria-selected="true"] {
			color: #023047 !important;
   			margin-right: 14px !important;
		}
	
		/* Tab 下划线 */
		[data-baseweb="tab-highlight"] {
			background-color: #023047 !important;
		}
  
		/* 文字 */
		[data-baseweb="tab"] > div > p {
			font-size: 20px !important;
			font-weight: bold !important;
		}
	</style>
	"""
	st.markdown(custom_css, unsafe_allow_html=True) # 🔥 使用 html 添加自定义样式 (CSS 注入)
	with tab1:
		Homepage.render()
	with tab2:
		OpenAISettingsPage.render() # 静态方法, 不传入 self, 直接调用
    

def main():
	render()


if __name__ == "__main__":
    main()




	
