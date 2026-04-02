import pandas as pd
import os
import json
from tqdm import tqdm

from src.llm_client import LLMClient
from src.parsing import parsing
from src.load_data import load_data
from src.system_prompts import CLASSIFIER_SYSTEM
from src.rewrite_input import rewrite_input


def run_pipeline(): 
    results_short = []
    missing_rows = []

    client = LLMClient()
    batch_size = 25
    data = load_data()
    loop_data = data.loc[:50, 'post_text']

    # classify and return data
    for n in tqdm(range(0, len(loop_data), batch_size)):
        batch = loop_data[n:n+batch_size]
        expected_rows_ids = list(batch.index)
        rewrtn_string = rewrite_input(batch)
        answ = client.chat(rewrtn_string, sys_prompt=CLASSIFIER_SYSTEM)
        json_answ, missing_ids = parsing(answ, expected_rows_ids)
        results_short.extend(json_answ)
        missing_rows.extend(missing_ids)

    # join the initial data frame with the llm classification
    marked_posts_short = loop_data.to_frame().reset_index().merge(
                            pd.DataFrame(results_short), 
                            how='left', 
                            left_on='index', 
                            right_on='row_id'
                            )

    print("Missing_rows:", missing_rows)
    print()
    return marked_posts_short