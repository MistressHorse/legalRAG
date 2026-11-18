from typing import Optional
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

def chunk_text(
    text: str,
    chunk_size: int = 2000,
    chunk_overlap: int = 200,
    metadata: Optional[dict] = None
) -> list[Document]:

    if chunk_size <= 0:
        raise ValueError(f"chunk_size должен быть положительным, получено: {chunk_size}")

    if chunk_overlap < 0:
        raise ValueError(f"chunk_overlap должен быть неотрицательным, получено: {chunk_overlap}")

    if chunk_overlap >= chunk_size:
        raise ValueError(
            f"chunk_overlap ({chunk_overlap}) должен быть меньше chunk_size ({chunk_size})"
        )

    if not text or not text.strip():
        return []

    if metadata is None:
        metadata = {}


    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
        separators=["\n\n", "\n", ". ", " ", ""],
        add_start_index=True
    )

    chunks = text_splitter.create_documents(
        texts=[text],
        metadatas=[metadata]
    )

    return chunks