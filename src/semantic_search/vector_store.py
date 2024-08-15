from typing import List, Dict
from langchain.schema import Document
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings


class VectorStore:
    def __init__(
        self,
        persist_directory: str = "chroma.db",
        collection_name: str = "homematch_listings_store",
    ):
        self.embeddings = OpenAIEmbeddings()
        self.vectorstore = Chroma(
            collection_name=collection_name,
            embedding_function=self.embeddings,
            persist_directory=persist_directory,
        )

    def search(self, query: str, filter: Dict = None, k: int = 3) -> List[Document]:
        return self.vectorstore.similarity_search(query, k=k, filter=filter)
