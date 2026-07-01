from pydantic import BaseModel

# Request model (data coming from the user)
class ChatRequest(BaseModel):
    message: str


# Response model (data going back to the user)
class ChatResponse(BaseModel):
    response: str