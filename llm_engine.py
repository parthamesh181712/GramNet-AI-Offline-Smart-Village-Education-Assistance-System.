from llama_cpp import Llama

llm = Llama(
    model_path="models/tinyllama.gguf",
    n_ctx=1024
)

def generate_answer(prompt):
    output = llm(
        prompt,
        max_tokens=200,
        temperature=0.3,
        stop=["Question:", "Context:"]
    )
    return output["choices"][0]["text"].strip()