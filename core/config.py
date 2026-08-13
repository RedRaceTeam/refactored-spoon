import os

class Settings:
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    WEBHOOK_URL = "https://refactored-spoon-c3i8.onrender.com"  # публичная ссылка
    PORT = int(os.getenv("PORT", 8000))
    ADMIN_ID = int(os.getenv("ADMIN_ID", 0))

settings = Settings()
