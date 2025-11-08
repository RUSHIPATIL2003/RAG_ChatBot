# embedding.py

from sentence_transformers import SentenceTransformer
import numpy as np
from config import EMBED_MODEL

embed_model = SentenceTransformer(EMBED_MODEL)


def _to_py_str(x):
    """Convert input to a plain Python str, handling numpy scalar types."""
    try:
        
        if hasattr(x, "item") and not isinstance(x, str):
            return str(x.item())
    except Exception:
        pass
    return str(x)


def get_embedding(text):
    """Generate embedding vector for given text.

    Always pass a list of Python strings to the SentenceTransformer.encode
    to avoid tokenizer type errors from numpy types or bytes.
    """
    
    if isinstance(text, (list, tuple)):
        texts = [_to_py_str(t) for t in text]
        if len(texts) == 0:
            texts = [" "]
    else:
        texts = [_to_py_str(text) if text is not None else " "]

    
    cleaned = []
    for t in texts:
        try:
            s = t.encode("utf-8", errors="ignore").decode("utf-8").strip()
            cleaned.append(s if s else " ")
        except Exception:
            cleaned.append(" ")

    try:
        
        embeddings = embed_model.encode(cleaned, convert_to_numpy=True)
        
        if embeddings.ndim == 2:
            vec = embeddings[0]
        else:
            vec = embeddings
        return vec.tolist()
    except Exception as e:
        print(f"Error encoding text: {str(e)}")
        
        try:
            dim = embed_model.get_sentence_embedding_dimension()
        except Exception:
            dim = 384
        return np.zeros(dim).tolist()
