import requests
import os
from dotenv import load_dotenv

load_dotenv()

backend = os.getenv("backend_url")

def hit_backend(news_text):
    response = requests.post(f"{backend}/predict", json={"text" : news_text})
    return response.json()


print(hit_backend("Hello"))