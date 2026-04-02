# Comments classification

## Goal:
Compare classical ML versus LLM classification

## Project structure

### llm_client_py
creates connection to an LLM via API and return responses.

### system_prompts
contains system prompts for use in LLM

### data
contains messages from social media for classification

## Statistics
- It takes in average 1.8 seconds to make a single row request to the LLM and get the response. So it took about 27 minutes to process about 900 rows.
- it took in average 0.65 seconds to process a row with batches of 10. Threefold decrease.