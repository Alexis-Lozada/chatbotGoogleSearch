import requests
import os
from dotenv import load_dotenv

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GOOGLE_CX = os.getenv("GOOGLE_CX")

def google_search(query):
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "q": query,
        "key": GOOGLE_API_KEY,
        "cx": GOOGLE_CX
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        results = response.json().get("items", [])
        return [(r["title"], r["link"]) for r in results[:3]] if results else []
    else:
        return []
