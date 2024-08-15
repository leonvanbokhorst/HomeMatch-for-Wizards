# from chromadb.config import Settings
# from langchain.vectorstores import Chroma
# from langchain_openai import OpenAIEmbeddings
# from langchain.schema import Document
# from langchain.chains import LLMChain
# from langchain.prompts import PromptTemplate
# from langchain_openai import ChatOpenAI

# import chromadb
import streamlit as st
import warnings
import time

from src.personalization.description_generator import PersonalizedDescriptionGenerator
from src.semantic_search.vector_store import VectorStore

warnings.filterwarnings("ignore")

listings = VectorStore()
mr_sneekrs = PersonalizedDescriptionGenerator()


st.set_page_config(page_title="HomeMatch", page_icon="🏠", layout="wide")
st.title("🧙‍♂️ HomeMatch: Magical Real Estate Finder")

# Display sneaky salesperson image
st.sidebar.image(
    "homematch-sneaky-salesperson.webp",
    caption="Meet mr. Sneekrs, your trusted real estate agent",
)

# Initialize session state
if "conversation_history" not in st.session_state:
    st.session_state.conversation_history = []
if "search_performed" not in st.session_state:
    st.session_state.search_performed = False

# Display chat history
for message in st.session_state.conversation_history:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input
user_input = st.chat_input("What kind of magical place are you looking for?")

if user_input:
    st.session_state.conversation_history.append(
        {"role": "user", "content": user_input}
    )

    response = mr_sneekrs.get_response(
        [msg["content"] for msg in st.session_state.conversation_history], user_input
    )

    # Check if the assistant is ready to perform a search
    if "READY TO SEARCH" in response:
        response = response.replace("READY TO SEARCH", "")
        st.session_state.search_performed = True
    else:
        # Only add the assistant's response to the conversation history if it's not a search trigger
        st.session_state.conversation_history.append(
            {"role": "assistant", "content": response}
        )

    st.rerun()

# Perform search if ready
if st.session_state.search_performed:
    st.session_state.search_performed = False  # Reset the flag

    with st.spinner(
        "Searching cribs...",
    ):
        # Get a 'sneaky' summary of the user's preferences to search the vector store for listings
        preferences_summary = mr_sneekrs.get_response(
            [msg["content"] for msg in st.session_state.conversation_history],
            "Please craft a short and precise summary of the user's preferences for a home search query.",
        )

        # Search for listings based on the user's preferences
        search_results = listings.search(preferences_summary)

        if search_results:
            st.success("Overpriced housing found 🪄")
        else:
            st.error("No magical places found 😢")

    with st.spinner("Thinking about selling... the Sneekers way 😈"):

        # Generate a personalized pitch for the user based on the search results
        personalized_pitch = mr_sneekrs.get_offer(
            search_results,
            "\n\nPreferences:\n"
            + preferences_summary
            + "\n\n".join(
                [
                    msg["content"]
                    for msg in st.session_state.conversation_history[
                        -3:
                    ]  # Only consider last 3 messages
                    if msg["role"] == "user"
                ],
            ),
        )

    if not personalized_pitch:
        st.error("No magical offers found 😢")
    else:
        st.success("Ghehe! Crafted that very special offer ✨🤑✨ Let's go!")
        time.sleep(3)  # Add some suspense

        st.session_state.conversation_history.append(
            {"role": "assistant", "content": personalized_pitch}
        )

        st.chat_message("assistant").write(personalized_pitch)

    # Rerun to update the chat display with search results
    st.rerun()
