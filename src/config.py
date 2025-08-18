import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
