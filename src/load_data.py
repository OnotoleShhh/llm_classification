import os
import pandas as pd

def load_data(file_name = 'Social_Media_Sentiment_Analysis_AI_Trends_2026.csv', usecols=['post_text']) -> pd.DataFrame:
    FILE_PATH = os.path.abspath(__file__)
    SRC_FOLDER = os.path.dirname(FILE_PATH)
    PROJECT_FOLDER = os.path.dirname(SRC_FOLDER)
    DATA_FOLDER = os.path.join(PROJECT_FOLDER, 'data')
    data_path = os.path.join(DATA_FOLDER, file_name)
    data = pd.read_csv(data_path, usecols=usecols)
    return data