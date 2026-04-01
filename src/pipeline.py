import pandas as pd
import os
import json

from src.llm_client import LLMClient

def load_data(file_name = 'Social_Media_Sentiment_Analysis_AI_Trends_2026.csv', usecols=['post_text']) -> pd.DataFrame:
    FILE_PATH = os.path.abspath(__file__)
    SRC_FOLDER = os.path.dirname(FILE_PATH)
    PROJECT_FOLDER = os.path.dirname(SRC_FOLDER)
    DATA_FOLDER = os.path.join(PROJECT_FOLDER, 'data')
    data_path = os.path.join(DATA_FOLDER, file_name)
    data = pd.read_csv(data_path, usecols=usecols)
    return data

def run_pipeline(data: pd.DataFrame): 
    client = LLMClient()
    results = []
    # classify and return data
    for text in data['post_text']:
        answ = client.chat(text)
        answ = json.loads(answ)
        results.append({
            "post_text":text,
            "sentiment":answ['sentiment']
        })

    marked_posts = pd.DataFrame(results)

    return marked_posts
