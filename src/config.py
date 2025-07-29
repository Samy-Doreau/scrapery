from pathlib import Path
import os

from dotenv import load_dotenv

# Load .env file at project root if it exists
ENV_PATH = Path(__file__).resolve().parent.parent / ".env"
if ENV_PATH.exists():
    load_dotenv(ENV_PATH)
else:
    # .env may not exist in initial setup; user can copy from .env.example
    load_dotenv()

# Generic placeholders; update in your own .env
TARGET_URL: str = os.getenv("TARGET_URL", "https://example.com")  # TODO: Replace with real URL
CSS_SELECTOR: str = os.getenv("CSS_SELECTOR", ".item")  # TODO: Replace with real CSS selector 