# pdf_load.py

import pytesseract
from pdf2image import convert_from_path
from PyPDF2 import PdfReader


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text(pdf_path):
    text = ""

    
    try:
        reader = PdfReader(pdf_path)
        for page in reader.pages:
            if page.extract_text():
                text += page.extract_text() + "\n"
    except:
        pass

 
    if not text.strip():
        print(" No digital text found. Using OCR...")
        pages = convert_from_path(pdf_path, dpi=300)
        for i, page in enumerate(pages):
            text += pytesseract.image_to_string(page)
            print(f"OCR processed page {i+1}/{len(pages)}")

    return text

def chunk_text(text, chunk_size=1000, overlap=200):
    """Split text into overlapping chunks"""
  
    try:
        text = text.encode('utf-8', errors='ignore').decode('utf-8')
    except Exception as e:
        print(f"Warning: Error cleaning text: {str(e)}")
        return []

    chunks = []
    start = 0
    text_len = len(text)
    
    while start < text_len:
        end = start + chunk_size
       
        chunk = text[start:end]
        
        chunk = chunk.strip()
        if chunk: 
            chunks.append(chunk)
        start = end - overlap
    
    return chunks
