from core.llm_engine import generate_answer
from core.retriever import retrieve
import sympy as sp
import gc   #  ADD HERE (top of file)

def solve_math(query):
    try:
        if any(char.isdigit() for char in query):
            return str(sp.sympify(query))
        return None
    except:
        return None

def tutor_response(query, chunks, index):

    #  STEP 1: Math handling
    math_result = solve_math(query)
    if math_result:
        return f"Answer: {math_result}"

    #  STEP 2: Retrieval
    retrieved_chunks = retrieve(query, chunks, index)
    context = "\n".join(retrieved_chunks[:3])
    context = context[:800]

    if not context.strip():
        return "I don't know"

    #  STEP 3: Prompt
    prompt = f"""
You are an AI tutor.

Answer ONLY from the given context.
If answer is not present, say "I don't know".

Explain in simple, clear language.

Context:
{context}

Question:
{query}

Answer:
"""

    #  STEP 4: LLM CALL
    answer = generate_answer(prompt)

    #  FREE MEMORY HERE (MOST IMPORTANT)
    del retrieved_chunks
    del context
    gc.collect()

    return answer