# 返回随机背景色
import random
from PIL import Image, ImageDraw
import os



def get_random_color():
	r = lambda: random.randint(0,255) # 👈 lambda 表示匿名函数, 用于返回随机数, 可以用 r() 来调用
	return '#%02X%02X%02X' % (r(),r(),r()) # 返回随机颜色



# 返回 emoji 图片的方法
def get_emoji_from_name(searched_emoji_name):
	emoji_dir = "assets/emoji" # emoji 图片的文件夹
	for file_name in os.listdir(emoji_dir): # 遍历文件夹
		if searched_emoji_name.lower() in file_name.lower(): # 如果物体名称在文件名中, lower() 是为了忽略大小写
			return os.path.join(emoji_dir, file_name) # 返回 emoji 图片的路径
	return None # 如果没有找到, 就返回 None



# 合成带有随机背景色的 emoji
def create_emoji_with_bg(emoji_path, padding_percentage=10):
	# 加载 emoji 图片
	emoji = Image.open(emoji_path)
 
	# 生成背景图片
	background_size = (100, 100)
	background = Image.new("RGBA", background_size, get_random_color()) # 生成背景色
 

	# 保持 emoji 的纵横比，同时确保它能完整地适应背景大小
	# 计算考虑到 padding 的新尺寸
	padding = background_size[0] * padding_percentage // 100  # 根据背景尺寸和 padding 百分比计算 padding 的像素值
	new_size = (background_size[0] - padding * 2, background_size[1] - padding * 2)  # 减去两侧的 padding
	emoji.thumbnail(new_size, Image.ANTIALIAS)
	# emoji.thumbnail(background_size, Image.ANTIALIAS) # 不考虑 padding

	# 计算 emoji 的位置 (居中)
	bg_W, bg_H = background.size # 获取背景图片的宽高
	emoji_W, emoji_H = emoji.size # 获取 emoji 图片的宽高
	emoji_offset = ((bg_W - emoji_W) //2 , (bg_H - emoji_H) //2) # 减去 emoji 的宽高后, 再除以 2, 得到 emoji 的位置
 
	# 将 emoji 粘到图片上
	background.paste(emoji, emoji_offset, emoji) # 第三个参数表示 mask, 用于透明度, 这里不需要, 所以传入 emoji

	# 保存图片并返回
	picture_path = "assets/generateEmoji/emoji_with_bg.png"
	background.save(picture_path) # 保存生成后的图片到到 generateEmoji
	return picture_path



# 返回随机背景色的方法
# def get_random_color():
#     r = lambda: random.randint(0,255)
#     return '#%02X%02X%02X' % (r(),r(),r()) # 返回随机颜色



# 生成随机背景色的 HTML
# def generate_emoji_html(emoji, background_color):
#     html_str = f"""
#     <div style="font-size: 4em; background-color: {background_color}; width: 100px; height: 100px; display: flex; justify-content: center; align-items: center; border-radius: 50%;">
#         {emoji}
#     </div>
#     """
#     return html_str

# # 生成随机 html 颜色
# def get_random_color():
#     return "#"+''.join([random.choice('0123456789ABCDEF') for _ in range(6)])

# # 在Streamlit中显示带有随机背景色的emoji
# def generate_random_background_emoji(emoji):
#     background_color = get_random_color()
#     html_str = generate_emoji_html(emoji, background_color)
#     components.html(html_str, height=150)
