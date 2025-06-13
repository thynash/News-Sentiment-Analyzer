import requests
import json
from datetime import datetime,timezone
from sentiment_analysis import get_sentiment  # make sure this file exists

NEWS_API_KEY = "your_api_key_here"
URL = f"https://newsapi.org/v2/top-headlines?country=us&apiKey=d7e63ceb813c4e82a165e7b686904df0"

def fetch_headlines():
    response = requests.get(URL)
    articles = response.json().get("articles", [])
    return [article["title"] for article in articles if article.get("title")]

