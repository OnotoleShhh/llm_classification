from llm_client import LLMClient
import pandas as pd
import os

class run_pipeline:
    def __init__(self):
        pass

FILE_PATH = os.path.abspath(__file__)
PROJECT_FOLDER = os.path.dirname(FILE_PATH)
DATA_FOLDER = os.path.join(PROJECT_FOLDER, 'data', 'Social_Media_Sentiment_Analysis_AI_Trends_2026.csv')

print(DATA_FOLDER)

client = LLMClient()

data = pd.read_csv(DATA_FOLDER)
print(data.head())

## stopped on making pipeline process. 
# I need to read data and then process it line by line with my LLMClient class.
# also i need to understand what is better: to process line by one or in batches.