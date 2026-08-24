class PromptBuilder:

    def build(self, question: str, context: str) -> str:

        return f"""
You are a helpful AI assistant.

Answer the user's question using only the provided context.

If the answer cannot be found in the context, say:
"I don't have enough information in the provided documents."

Do not invent or assume information.

Context:
----------------
{context}
----------------

Question:
{question}

Answer:
"""
