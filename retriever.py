import numpy as np
from sentence_transformers import SentenceTransformer
import gc   #  ADD

#  Load model ONCE
model = SentenceTransformer("models/embeddings", device="cpu")

def retrieve(query, chunks, index, top_k=3):   #  FIXED top_k

    #  Encode query
    query_embedding = model.encode(
        [query],
        batch_size=1,
        show_progress_bar=False,
        convert_to_numpy=True
    )

    #  FAISS search (NO extra np.array)
    D, I = index.search(query_embedding, top_k)

    results = []
    for i in I[0]:
        if 0 <= i < len(chunks):
            results.append(chunks[i])

    #  MEMORY CLEANUP (VERY IMPORTANT)
    del query_embedding
    gc.collect()

    return results