import pytest
from src.personalization.description_generator import PersonalizedDescriptionGenerator


@pytest.fixture
def description_generator():
    return PersonalizedDescriptionGenerator()


def test_generate_description(description_generator):
    listing = {
        "neighborhood": "Enchanted Forest",
        "price": 250000,
        "bedrooms": 2,
        "bathrooms": 1,
        "sqft": 1000,
        "description": "A charming cottage with magical amenities.",
    }
    user_preferences = "I'm looking for a cozy home near nature."

    personalized_description = description_generator.generate_description(
        listing, user_preferences
    )

    assert isinstance(personalized_description, str)
    assert len(personalized_description) > 0
    assert "Enchanted Forest" in personalized_description
    assert "cozy" in personalized_description.lower()
