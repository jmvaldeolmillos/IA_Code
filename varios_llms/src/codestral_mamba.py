import logging
import os

import gradio as gr
from dotenv import load_dotenv
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage

# load environment variables from a .env file
load_dotenv()

logging.basicConfig(
    level=logging.INFO, format="&(asctime)s - %(levelname)s - %(message)s")


def get_api_key():
    api_key = os.getenv("MISTRAL_API_KEY")
    if not api_key:
        logging.error("MISTRAL_API_KEY environment variable not found.")
        raise ValueError(
            "API key not found. Please set de MISTRAL_API_KEY environment variable."
        )
    return api_key


def create_mistral_client(api_key):
    try:
        return MistralClient(api_key=api_key)
    except Exception as e:
        logging.error(f"Error creating MistraClient: {e}")
        raise


def get_chat_response(client, user_input, model="codestral-mamba-latest"):
    try:
        messages = [ChatMessage(role="user", content=user_input)]
        chat_response = client.chat(model=model, messages=messages)
        return chat_response.choices[0].message.content
    except Exception as e:
        logging.error(f"Error interacting with the Mistral API: {e}")
        return "An error occurred while interacting with de the Mistral AIP. Please try again later..."


def chat_with_mistral(user_input):
    try:
        api_key = get_api_key()
        client = create_mistral_client(api_key)
        return get_chat_response(client, user_input)
    except ValueError as e:
        return str(e)
    except Exception as e:
        logging.error(f"Unexpect error: {e}")
        return "An unexpect error occurred. Please try again later..."


def create_gradio_interface():
    ui = gr.Interface(
        fn=chat_with_mistral,
        inputs=gr.components.Textbox(label="Enter your message"),
        outputs=gr.components.Markdown(label="Chatbot response"),
        title="Mistral Coding Assistant",
        description="Get coding help an advice from the Mistral API. Enter your programing question or code snippets",
        examples=[
            ["How do I reverse a string in Python?"],
            ["Can you explain the difference between a list and a tuple in Python?"],
        ],
        allow_flagging="never",
    )
    ui.launch()


if __name__ == "__main__":
    create_gradio_interface()
