from typing import List, Tuple, Dict
from langchain.schema import Document
from ..vector_store.vector_store import VectorStore


class SemanticSearchEngine:
    def __init__(self, vector_store: VectorStore):
        self.vector_store = vector_store

    def search(self, query: str, k: int = 5) -> List[Tuple[Document, float]]:
        return self.vector_store.search(query, k)

    def filter_results(
        self, results: List[Tuple[Document, float]], filters: Dict
    ) -> List[Tuple[Document, float]]:
        filtered_results = []
        for doc, score in results:
            if all(doc.metadata.get(key) == value for key, value in filters.items()):
                filtered_results.append((doc, score))
        return filtered_results
