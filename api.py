from dotenv import load_dotenv
from openai import AzureOpenAI
from PIL import Image
import os
import requests

load_dotenv()

client = AzureOpenAI(
    azure_endpoint=os.getenv("API_ENDPOINT"),
    api_key=os.getenv("API_KEY"),
    api_version="2024-08-01-preview"
)

def api_openai(message):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Eres un asistente útil y amigable."},
            {"role": "user", "content": message}
        ],
        max_tokens=200,
        temperature=0.7
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    poem = get_christmas_poem()
    print("Poema de Navidad:", poem)
