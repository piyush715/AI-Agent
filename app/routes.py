from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from app.models import ChatRequest
from app.stream import stream_response

router = APIRouter()


@router.get("/health")
def health_check():
    return {
        "status": "healthy",
        "message": "API is working"
    }


@router.post("/chat")
def chat(request: ChatRequest):

    return StreamingResponse(
        stream_response(request.message),
        media_type="text/plain"
    )