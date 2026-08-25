class PromptBuilder:

    def build(self, question: str, context: str, history: str = "") -> str:

        return f"""
You are a helpful AI assistant.

Answer the user's question using only the provided document context.

Use the conversation history to understand references such as:
"he", "she", "it", "that person", etc.

If the answer cannot be found in the document context, say:
"I don't have enough information in the provided documents."

Do not invent or assume information.

Conversation History:
----------------
{history}
----------------

Document Context:
----------------
{context}
----------------

Current Question:
{question}

Answer:
""".strip()
