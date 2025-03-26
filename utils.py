import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
from keybert import KeyBERT
from googletrans import Translator
import json

def fetch_news(company, max_articles=10):
    """Fetches news articles from Bing News for a given company."""
    url = f'https://www.bing.com/news/search?q={company}'
    headers = {
       'User-Agent': 'Mozilla/5.0',
       'Accept-Language': 'en-US, en; q=0.9'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = [item.get_text() for item in soup.select('a.title')[:max_articles]]
    return articles

def analyze_sentiment(text):
    """Performs sentiment analysis on a given text."""
    return TextBlob(text).sentiment.polarity

def extract_keywords(text):
    """Extracts keywords from the given text."""
    kw_model = KeyBERT()
    return kw_model.extract_keywords(text)

def translate_text(text, target_lang='en'):
    """Translates text to the target language."""
    translator = Translator()
    return translator.translate(text, dest=target_lang).text

def save_results(data, filename="results.json"):
    """Saves analysis results to a JSON file."""
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
