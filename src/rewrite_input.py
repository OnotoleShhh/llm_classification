import pandas as pd

def rewrite_input(data: pd.Series):
    """
    Transforms pandas series data into a string formatted for LLM processing
    
    Example input: 
        0 I don’t agree with this at all.
    
    Example output: 
        [ROW ID: 0]
        Text: I don’t agree with this at all.
    """
    blocks = []
    for idx, text in data.items():
        block = f"[ROW ID: {idx}]\nText: {text}"
        blocks.append(block)
    
    return '\n\n'.join(blocks)