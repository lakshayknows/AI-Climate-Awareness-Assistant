# utils/config.py
from dotenv import load_dotenv
from os import getenv

load_dotenv()

OPENROUTER_API_KEY = getenv("OPENROUTER_API_KEY")
OPENROUTER_BASE_URL = getenv("OPENROUTER_BASE_URL")

if not OPENROUTER_API_KEY:
    raise ValueError("❌ OPENROUTER_API_KEY missing in .env")

MODEL_NAME = "openai/gpt-oss-120b"
