from openai import OpenAI
from system_prompts import CLASSIFIER_SYSTEM
import os

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

    def chat(self, text, temperature):
        
        response = self.client.chat.completions.create(
            model = self.model,
            messages=[
                {
                    "role": "system", 
                    "content": CLASSIFIER_SYSTEM
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

