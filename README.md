# News Analysis App

## Overview
This Python application fetches news articles, performs sentiment analysis, extracts keywords, and translates text.

## Installation
1. Clone the repository:
   ```sh
   git clone <repository_url>
   cd <repository_folder>
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
Run the script and enter a company name to analyze related news articles:
```sh
python app.py
```

## Features
- Fetches news articles from Bing
- Analyzes sentiment using TextBlob
- Extracts keywords with KeyBERT
- Translates text using Google Translate API
- Saves results to a JSON file

## Dependencies
See `requirements.txt` for a list of required packages.
