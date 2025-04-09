import streamlit as st
import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
from transformers import pipeline
from gtts import gTTS
import os
from keybert import KeyBERT
from googletrans import Translator
import tempfile

# Initialize models
kw_model = KeyBERT()
translator = Translator()
classifier = pipeline("sentiment-analysis")

def fetch_news(company, max_articles=10):
    url = f"https://www.bing.com/news/search?q={company}"
    headers = {
        'user-agent': 'Mozilla/5.0',
        'Accept-language': 'en-US',
    }

    doc = requests.get(url, headers=headers)
    soup = BeautifulSoup(doc.text, 'html.parser')
    articles = []

    for item in soup.find_all('div', class_='newsitem', limit=max_articles):
        title_tag = item.find('a', class_='title')
        summary_tag = item.find('div', class_='snippet')

        if title_tag and summary_tag:
            articles.append({
                'Title': title_tag.text.strip(),
                'Summary': summary_tag.text.strip(),
            })
    return articles

def analyze_summary(summary):
    sentiment = classifier(summary)[0]
    keywords = kw_model.extract_keywords(summary, stop_words='english', top_n=5)
    return sentiment, [kw[0] for kw in keywords]

def synthesize_audio(text, lang='en'):
    tts = gTTS(text=text, lang=lang)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
        tts.save(fp.name)
        return fp.name

# Streamlit UI
st.title("📰 News Extraction & Analysis")
company = st.text_input("Enter a company name to search for news:")

if company:
    with st.spinner("Fetching news..."):
        articles = fetch_news(company)

    if not articles:
        st.warning("No articles found.")
    else:
        for i, article in enumerate(articles):
            st.subheader(f"🗞️ {article['Title']}")
            st.write(article['Summary'])

            sentiment, keywords = analyze_summary(article['Summary'])
            st.write(f"**Sentiment**: {sentiment['label']} (score: {sentiment['score']:.2f})")
            st.write("**Keywords**:", ", ".join(keywords))

            audio_file = synthesize_audio(article['Summary'])
            st.audio(audio_file)
