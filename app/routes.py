from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from app.models import ChatRequest
from app.stream import stream_response
from app.stream import stream_rag_response

from app.rag import (
    load_pdf,
    split_documents,
    create_embeddings,
    create_vector_store,
    retrieve_documents,
    build_context
)

router = APIRouter()


@router.get("/health")
def health_check():
    return {
        "status": "healthy",
        "message": "API is working"
    }


@router.post("/chat")
def chat(request: ChatRequest):

    # Step 1: Load the PDF
    docs = load_pdf()

    # Step 2: Split into chunks
    chunks = split_documents(docs)

    # Step 3: Load embedding model
    embedding = create_embeddings()

    # Step 4: Create vector database
    vector_store = create_vector_store(chunks, embedding)

    # Step 5: Retrieve relevant chunks
    results = retrieve_documents(
        vector_store,
        request.message
    )

    # Step 6: Build context
    context = build_context(results)

    # Step 7: Send context + question to Groq
    return StreamingResponse(
        stream_rag_response(
            context,
            request.message
        ),
        media_type="text/plain"
    )