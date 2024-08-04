from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain_community.llms import Ollama

MODEL = "gemma2"

llm = Ollama(
    model=MODEL,
    callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]),
    temperature=0.1,
)
from langchain.prompts import PromptTemplate

prompt = PromptTemplate(
    input_variables=["topic"],
    template="Talk me about the most {topic} countries",
)

chain = llm | prompt
response = chain.invoke("poorest")
print(response["text"])
