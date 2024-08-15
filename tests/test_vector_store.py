import pytest
from src.vector_store.vector_store import VectorStore
from langchain.schema import Document


@pytest.fixture
def vector_store(tmp_path):
    return VectorStore(str(tmp_path), "test_collection")


def test_add_and_search_listings(vector_store):
    listings = [
        Document(
            page_content="A cozy cottage in the woods", metadata={"price": 100000}
        ),
        Document(
            page_content="A magical treehouse with a view", metadata={"price": 150000}
        ),
        Document(
            page_content="A modern apartment in the city center",
            metadata={"price": 200000},
        ),
    ]
    vector_store.add_listings(listings)

    results = vector_store.search("cottage in the woods", filter_dict=None, k=1)
    assert len(results) == 1
    assert "cozy cottage" in results[0].page_content


def test_filter_search_results(vector_store):
    listings = [
        Document(page_content="Affordable cottage", metadata={"price": 100000}),
        Document(page_content="Luxury mansion", metadata={"price": 1000000}),
    ]
    vector_store.add_listings(listings)

    results = vector_store.search(
        "cottage", filter_dict={"price": {"$lt": 150000}}, k=1
    )
    assert len(results) == 1
    assert results[0].metadata["price"] == 100000
