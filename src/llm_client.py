import os
import json
from openai import OpenAI

from src.system_prompts import CLASSIFIER_SYSTEM


class LLMClient():
    """
    Creates connection to DeepSeek.
    """

    def __init__(self):
        self.client = OpenAI(
        api_key=os.environ.get('DEEPSEEK_API_KEY'),
        base_url="https://api.deepseek.com"
        )

        self.model = 'deepseek-chat'

    def chat(self, text: str, temperature: int = 0.3, sys_prompt = CLASSIFIER_SYSTEM):
        """
        text: text to classify
        temperature: how creative a model should be. 0 - precise, 1 - creative
        """
        response = self.client.chat.completions.create(
            model = self.model,
            messages=[
                {
                    "role": "system", 
                    "content": sys_prompt
                },
                {
                    "role": "user", 
                    "content": text
                },
            ],
            stream=False,
            temperature=temperature
        )

        return response.choices[0].message.content

