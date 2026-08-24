from app.models.chunks import Chunk


class ContextBuilder:
    def build(self, chunks: list[Chunk]) -> str:
        context_parts = []
        for index, chunk in enumerate(chunks, start=1):
            context_parts.append(f"""[source{index}] \n
                Document Id:{chunk.document_id}\n
                Chunk:{chunk.chunk_index}\n
                {chunk.text}\n
                """)
        return "\n\n".join(context_parts)
