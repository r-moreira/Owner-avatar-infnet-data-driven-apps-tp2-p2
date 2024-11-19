from fastapi import APIRouter
from ..models.chat_model import ChatInput, ChatOutput
from ..services.llm_service import LLMService

router = APIRouter()


@router.post("/fake_llm/")
def fake_llm_message(body: ChatInput) -> ChatOutput:
    response = LLMService.fake_message(body.message)
    return ChatOutput(message=response)

@router.post("/gpt4o/translate/en-pt/")
def chat_gpt_translate(body: ChatInput) -> ChatOutput:
    response = LLMService.chat_gpt_translate(body.message)
    return ChatOutput(message=response)

@router.post("/helsinki/translate/en-de/")
def helsinki_nlp_translate(body: ChatInput) -> ChatOutput:
    response = LLMService.helsinki_nlp_translate(body.message)
    return ChatOutput(message=response)