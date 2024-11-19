from langchain_community.llms import FakeListLLM, HuggingFaceHub
from langchain_openai.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from transformers import pipeline
import torch
import os

class LLMService:
    def __init__(self):
        pass        

    @staticmethod
    def fake_message(message: str) -> str:
        fake_llm = FakeListLLM(responses=["Hi, how are you?", "Good morning!"])
        return fake_llm.invoke(message)

    @staticmethod
    def chat_gpt_translate(message: str) -> str:
        
        template = ChatPromptTemplate([
            ("system", "You are an English to Portuguese (Brazil) translator. Reject any other language."),
            ("user", "Translate this: {message}")
        ])
        llm = ChatOpenAI(model="gpt-4o", api_key=os.getenv("OPENAI_API_KEY"))
        response = llm.invoke(template.format_messages(message=message))
        return response.content
        
    @staticmethod
    def helsinki_nlp_translate(message: str) -> str:
        llm = HuggingFaceHub(
            repo_id='Helsinki-NLP/opus-mt-en-de',
            huggingfacehub_api_token = os.getenv("HUGGINGFACEHUB_API_TOKEN"),
            model_kwargs={}
        )
        output = llm.invoke(message)
        return output
