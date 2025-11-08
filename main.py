# main.py

from pdf_load import extract_text, chunk_text
from vectordb import add_chunks
from rag_pipeline import ask_rag
import time



PDF_PATH = r"E:\Projech\bajaj_finserv_factsheet_Oct.pdf"


print(" Extracting text from PDF...")
pdf_text = extract_text(PDF_PATH)
chunks = chunk_text(pdf_text)


print(" Creating embeddings and storing chunks...")
add_chunks(chunks)


print(" PDF loaded! You can now ask questions.")
while True:
    q = input("\nAsk a question (or type 'exit'): ")
    if q.lower() == "exit":
        print(" Exiting chatbot...")
        break


    start = time.time()
    print("Answer:", ask_rag(q))
    end = time.time()
    print(f"(Response time: {end - start:.2f} seconds)")