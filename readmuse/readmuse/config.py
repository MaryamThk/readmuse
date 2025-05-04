import os
from dotenv import load_dotenv

load_dotenv()

def get_config():
    return {
        "API_URL": os.getenv("API_URL", "https://openrouter.ai/api/v1/chat/completions"),
        "API_KEY": os.getenv("API_KEY") or raise_key_error(),
    }

def raise_key_error():
    raise EnvironmentError("Missing API_KEY. Set it in a .env file or environment variable.")
