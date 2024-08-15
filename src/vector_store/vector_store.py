from typing import List, Dict
from langchain.schema import Document
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings


class VectorStore:
    def __init__(self, persist_directory: str, collection_name: str):
        self.embeddings = OpenAIEmbeddings()
        self.vectorstore = Chroma(
            collection_name=collection_name,
            embedding_function=self.embeddings,
            persist_directory=persist_directory,
        )

    def add_listings(self, listings: List[Dict]):
        documents = []
        for listing in listings:
            content = f"{listing['description']} {listing['neighborhood_description']}"
            metadata = {
                k: v
                for k, v in listing.items()
                if k not in ["description", "neighborhood_description"]
            }
            documents.append(Document(page_content=content, metadata=metadata))
        self.vectorstore.add_documents(documents)

    def search(self, query: str, k: int = 5) -> List[Document]:
        return self.vectorstore.similarity_search(query, k=k)
