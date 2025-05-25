from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
    GEMINI_KEY = os.getenv('GEMINI_KEY')


settings = Settings()
