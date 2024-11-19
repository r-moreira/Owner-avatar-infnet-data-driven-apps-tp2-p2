from pydantic import BaseModel


class AutocompleteInput(BaseModel):
    message: str

class ChatInput(BaseModel):
    message: str
    
    
class ChatOutput(BaseModel):
    message: str
    