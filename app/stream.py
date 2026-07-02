from groq import Groq

from app.config import GROQ_API_KEY
from app.prompts import SYSTEM_PROMPT

client = Groq(api_key=GROQ_API_KEY)

def stream_response(message: str):

    stream = client.chat.completions.create(
        model="llama-3.3-70b-versatile",

        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": message
            }
        ],

        stream=True
    )

    for chunk in stream:

        if chunk.choices[0].delta.content:

            yield chunk.choices[0].delta.content

def stream_rag_response(context: str, question: str):

    stream = client.chat.completions.create(
        model="llama-3.3-70b-versatile",

        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "system",
                "content": f"""
Answer ONLY from the provided context.

If the answer is not present in the context,
reply with:
"I couldn't find that information in the uploaded document."

Context:

{context}
"""
            },
            {
                "role": "user",
                "content": question
            }
        ],

        stream=True
    )

    for chunk in stream:

        if chunk.choices[0].delta.content:

            yield chunk.choices[0].delta.content