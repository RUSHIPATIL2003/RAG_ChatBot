

from groq import Groq
from config import GROQ_API_KEY, CHAT_MODEL
from vectordb import retrieve_context

 
client = Groq(api_key=GROQ_API_KEY)

def ask_rag(question):
    """Retrieve relevant chunks and ask Groq LLaMA chat model"""
    context_chunks = retrieve_context(question)
    context = "\n\n".join(context_chunks)

    prompt = f"Context:\n{context}\n\nQuestion: {question}"

    response = client.chat.completions.create(
        model=CHAT_MODEL,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
