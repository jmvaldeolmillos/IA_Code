import anthropic
import os
import logging
from dotenv import load_dotenv

# load environment variables from a .env file
load_dotenv()
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def get_api_key():
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        logging.error("ANTHROPIC_API_KEY environment variable not found.")
        raise ValueError(
            "API key not found. Please set de ANTHROPIC_API_KEY environment variable."
        )
    return api_key


client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-3-5-sonnet-20240620",
    max_tokens=1000,
    temperature=0,  # de 0 a 1, 0 es el más conservador
    system="You are a world-class poet. Respond only with short poems.",
    messages=[
        {
            "role": "user",
            "content": [{"type": "text", "text": "Why is the ocean salty?"}],
        }
    ],
)
print(message.content)
