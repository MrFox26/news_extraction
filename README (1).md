# News Analysis Tool

This repository contains a Jupyter notebook that analyzes news articles about a specific company. It fetches news from Bing News, performs sentiment analysis, classifies topics, extracts keywords, and generates an audio output of the final sentiment in Hindi.

## Features

- Fetches latest news articles for a given company.
- Analyzes sentiment of each article using TextBlob.
- Classifies topics using a zero-shot classification model from Hugging Face.
- Computes sentiment distribution across articles.
- Extracts key phrases using KeyBERT.
- Compares coverage between consecutive articles.
- Determines overall sentiment and translates it to Hindi.
- Converts the translated sentiment to audio using gTTS.

## Usage

1. Open the JupyterLab interface of this Space.
2. Open the notebook `final (1).ipynb`.
3. Run the cells in order.
4. When prompted, enter the company name to analyze.
5. The output will be displayed in the notebook, including a JSON summary and an audio file.

## Requirements

The necessary packages are listed in `requirements.txt` and will be installed automatically when the Space is built.

## Notes

- This tool uses web scraping and may be subject to changes in the Bing News website structure.
- The sentiment analysis and topic classification are based on pre-trained models and may not be 100% accurate.
- The audio output is in Hindi; ensure that the system supports audio playback.