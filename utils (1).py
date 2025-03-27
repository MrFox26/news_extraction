# Utility functions extracted from the notebook

def fetch_news(company, max_articles=10):
    """Fetches news articles from Bing News for a given company."""
    url = f'https://www.bing.com/news/search?q={company}'
    headers = {
       'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
       'Accept-language': 'en-US, en; q=0.9',
       'connection':'keep-alive',
       'upgrade-insecure-requests': '1'
        }


def classify_topics(articles):
    """Uses zero-shot classification to assign topics to news articles."""
    candidate_labels = [
        "Technology", "Electric Vehicles", "Stock Market", "Finance", "Innovation",
        "Regulation", "Economy", "Artificial Intelligence", "Climate Change", "Energy",
        "Consulting", "Business Strategy", "Consumer Behavior", "Leadership", "Cryptocurrency",
        "Healthcare", "Cybersecurity", "Retail", "Manufacturing", "Supply Chain"
    ]


def compute_sentiment_distribution(articles):
    """Counts the number of articles in each sentiment category."""
    sentiment_counts = {"Positive": 0, "Negative": 0, "Neutral": 0}


def extract_keywords(text, top_n=3):
    """Extracts key phrases from the given text."""
    keywords = kw_model.extract_keywords(text, keyphrase_ngram_range=(1, 2), stop_words='english')
    return ', '.join([kw[0] for kw in keywords[:top_n]])


def compare_coverage(articles):
    """Generates a comparative analysis of news articles with concise comparisons."""
    comparisons = []
    topics_set = [set(article['Topics']) for article in articles]


def calculate_final_sentiment(sentiment_distribution):
    """Determines the overall sentiment based on sentiment distribution."""
    max_sentiment = max(sentiment_distribution, key=sentiment_distribution.get)


def translate_final_sentiment_to_hindi(final_sentiment_analysis):
  """Translates the final sentiment analysis to Hindi."""
  translator = Translator()
  try:
    translated_text = translator.translate(final_sentiment_analysis, dest='hi').text
    return translated_text
  except Exception as e:
    print(f"Error during translation: {e}")
    return "Translation failed."


def generate_output(company, max_articles=10):
    """Fetches news, analyzes sentiment, classifies topics, and structures the final JSON output with comparative coverage."""
    articles = fetch_news(company, max_articles)
    articles = analyze_sentiment(articles)
    articles = classify_topics(articles)
    sentiment_distribution = compute_sentiment_distribution(articles)
    coverage_differences = compare_coverage(articles)
    final_sentiment = calculate_final_sentiment(sentiment_distribution)
    translated_sentiment = translate_final_sentiment_to_hindi(final_sentiment)
