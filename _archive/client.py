import requests
from _archive.config import API_KEY, API_URL, MODEL_NAME

class AnthropicClient:
    def __init__(self):
        self.api_key = API_KEY
        self.api_url = API_URL
        self.model = MODEL_NAME

    def chat(self, messages):
        headers = {
            "x-api-key": self.api_key,
            "anthropic-version": "2023-06-01",
            "Content-Type": "application/json",
        }

        data = {
            "model": self.model,
            "messages": messages,
            "max_tokens": 1024
        }

        response = requests.post(self.api_url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()
