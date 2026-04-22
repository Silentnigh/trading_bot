import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="C:/Users/Banti/Desktop/trading-bot/.env")
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

BASE_URL = "https://testnet.binancefuture.com"

print("API:", API_KEY)
print("SECRET:", API_SECRET)