import pytest
from src.data_generation.city_context_generator import CityContextGenerator
from langchain_openai import ChatOpenAI


@pytest.fixture
def city_generator():
    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.7)
    return CityContextGenerator(llm)


def test_generate_contexts(city_generator):
    contexts = city_generator.generate_contexts(num_contexts=3)
    assert len(contexts) == 3
    for context in contexts:
        assert isinstance(context, str)
        assert len(context) > 0


def test_save_and_load_contexts(city_generator, tmp_path):
    contexts = city_generator.generate_contexts(num_contexts=5)
    csv_file = tmp_path / "test_contexts.csv"
    city_generator.save_to_csv(contexts, filename=str(csv_file))
    loaded_contexts = city_generator.load_from_csv(filename=str(csv_file))
    assert len(loaded_contexts) == 5
    assert loaded_contexts.equals(contexts)
