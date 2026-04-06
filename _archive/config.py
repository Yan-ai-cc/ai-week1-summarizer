from dotenv import load_dotenv
import os

# 加载 .env
load_dotenv()

API_KEY = os.getenv("API_KEY")
API_URL = os.getenv("API_URL")
MODEL_NAME = os.getenv("MODEL_NAME")

if not API_KEY:
    raise ValueError("API_KEY 未设置，请检查 .env 文件")
