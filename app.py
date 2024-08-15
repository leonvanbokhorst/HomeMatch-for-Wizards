import streamlit as st
from src.data_generation.city_context_generator import CityContextGenerator
from src.vector_store.vector_store import VectorStore
from src.semantic_search.search_engine import SemanticSearchEngine
from src.personalization.description_generator import PersonalizedDescriptionGenerator
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def main():
    st.set_page_config(page_title="HomeMatch", page_icon="🏠", layout="wide")
    st.title("🧙‍♂️ HomeMatch: Magical Real Estate Finder")

    # Initialize components
    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.7)
    vector_store = VectorStore("chroma_persist", "homematch_listings")
    search_engine = SemanticSearchEngine(vector_store)
    description_generator = PersonalizedDescriptionGenerator()

    # Sidebar for generating new data (optional)
    if st.sidebar.button("Generate New Listings"):
        with st.spinner("Generating new magical listings..."):
            city_generator = CityContextGenerator(llm)
            contexts = city_generator.generate_contexts(num_contexts=10)
            # Here you would generate listings based on these contexts
            # and add them to your vector store
            st.sidebar.success("New listings generated!")

    # Chat interface
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("What kind of magical home are you looking for?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Perform search
        results = search_engine.search(prompt)

        # Generate personalized descriptions
        personalized_listings = []
        for doc, score in results:
            personalized_description = description_generator.generate_description(
                doc.metadata, prompt
            )
            personalized_listings.append(
                {**doc.metadata, "description": personalized_description}
            )

        # Display results
        with st.chat_message("assistant"):
            st.markdown("I've found some magical properties that might interest you!")
            for listing in personalized_listings:
                with st.expander(f"{listing['neighborhood']} - ${listing['price']}"):
                    st.markdown(listing["description"])

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": "I've found some magical properties that might interest you!",
            }
        )


if __name__ == "__main__":
    main()
