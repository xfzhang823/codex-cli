 # Configuration management, including dotenv for API keys

# config.py
from dotenv import load_dotenv
import os

def load_config() -> dict:
    load_dotenv()
    return {
        "OPENAI_API_KEY": os.getenv("OPENAI_API_KEY")
    }
