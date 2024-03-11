# 统一管理配置的参数

class Config:
	def __init__(
		self,
		openai_api_key=None, 
		pinecone_api_key=None,
		pinecone_api_endpoint=None,
		openai_url=None,
		model_name=None,
	) -> None:
		self.openai_api_key = openai_api_key
		self.pinecone_api_key = pinecone_api_key
		self.pinecone_api_endpoint = pinecone_api_endpoint
		self.openai_url = openai_url
		self.model_name = model_name
  
	def set_and_save_config(self, attr: str, value):
		if not hasattr(self, attr):
			raise AttributeError(f"Config 中没有此属性: {attr}")
			return
		setattr(self, attr, value)
		self.save_to_env()

	# 修改环境变量的配置
	def save_to_env(self, **kwargs):
		print("👍 保存配置到 .env 文件")
		# 更新需要修改的配置项
		updated_lines = []
		with open(".env", "r") as f:
			lines = f.readlines()
			for line in lines:
				key, _ = line.split("=")
				if key.strip().lower() == "openai_api_key":
					updated_lines.append(f"OPENAI_API_KEY={self.openai_api_key}\n")
				elif key.strip().lower() == "pinecone_api_key":
					updated_lines.append(f"PINECONE_API_KEY={self.pinecone_api_key}\n")
				elif key.strip().lower() == "pinecone_api_endpoint":
					updated_lines.append(f"PINECONE_API_ENDPOINT={self.pinecone_api_endpoint}\n")
				else:
					updated_lines.append(line)
		print("值:",updated_lines)
   
		# 写入更新后的内容到文件
		with open(".env", "w") as f:
			f.writelines(updated_lines)
