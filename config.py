from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "17596251"))
API_HASH = getenv("API_HASH", "e58343b4c0193e293e391daf97603fcd")

BOT_TOKEN = getenv("BOT_TOKEN", "6467944590:AAGd6n4ELIPe-y8BOk9e7tB-pBhw4oh3BZA")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://hny:zara@cluster0.lfe5o.mongodb.net/?retryWrites=true&w=majority")

OWNER_ID = int(getenv("OWNER_ID", 6079943111))
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/AloneXBots")
