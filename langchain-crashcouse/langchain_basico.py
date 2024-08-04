from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain_community.llms import Ollama

MODEL = "gemma2"

llm = Ollama(
    model=MODEL, callback_manager=CallbackManager([StreamingStdOutCallbackHandler()])
)

llm.invoke("Talk me about the most populated countries")
