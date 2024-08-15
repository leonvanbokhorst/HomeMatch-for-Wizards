import streamlit as st
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
import warnings

warnings.filterwarnings("ignore")

# Initialize LLM and vector store (assuming these are set up as in HomeMatchv2.ipynb)
llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.7)
embeddings = OpenAIEmbeddings()
vectorstore = Chroma(
    collection_name="homematch_listings_store",
    embedding_function=embeddings,
    persist_directory="chroma.db",
)


def get_sneaky_salesperson_response(conversation_history, user_input):
    prompt = PromptTemplate(
        input_variables=["history", "human_input"],
        template="""
        You are mister Sneekrs, a magical, sneaky realty salesperson from the Harry Potter series. You help users find their ideal fantasy home. 
        Based on the conversation history and the user's latest input, extract relevant preferences for a home search.
        
        Keep the conversation magical, engaging, short, and a bit weird. Ask short questions or make suggestions to gather more information about the user's preferences.
        If you have enough information to perform a search or if the user asks to see options, say "READY TO SEARCH" at the end of your response.

        Conversation history:
        {history}

        Human: {human_input}
        AI: """,
    )

    chain = LLMChain(llm=llm, prompt=prompt)
    return chain.run(history="\n".join(conversation_history), human_input=user_input)


def search_listings(conversation_history):
    prompt = PromptTemplate(
        input_variables=["history"],
        template="""
        Based on the following conversation history, summarize the user's preferences for a home search query:
        
        {history}
        
        Summary:
        """,
    )

    chain = LLMChain(llm=llm, prompt=prompt)
    search_query = chain.run(history="\n".join(conversation_history))
    return vectorstore.similarity_search_with_relevance_scores(search_query, k=3)


def personalize_listings(listings, user_preferences):
    prompt = PromptTemplate(
        input_variables=["listings", "preferences"],
        template="""
        You are a magical, sneaky realty salesperson from the Harry Potter series. Use the following listings to make a compelling offer to the user. 
        The user has these preferences: {preferences}
        
        Listings:
        {listings}
        
        Create a personalized, engaging sales pitch for these listings, highlighting how they match the user's preferences. Start by saying something like "I've found some magical homes that match your preferences:" 
        """,
    )

    chain = LLMChain(llm=llm, prompt=prompt)
    return chain.run(listings=str(listings), preferences=user_preferences)


# Streamlit UI
st.set_page_config(page_title="HomeMatch", page_icon="🏠", layout="wide")

st.title("🧙‍♂️ HomeMatch: Magical Real Estate Finder")

# Display sneaky salesperson image
st.sidebar.image(
    "homematch-sneaky-salesperson.webp",
    caption="Meet mister Sneekrs, your magical real estate agent",
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
user_input = st.chat_input("What kind of magical home are you looking for?")

if user_input:
    # Add user message to chat history
    st.session_state.conversation_history.append(
        {"role": "user", "content": user_input}
    )

    # Get AI response
    ai_response = get_sneaky_salesperson_response(
        [msg["content"] for msg in st.session_state.conversation_history], user_input
    )

    # Check if it's time to search
    if "READY TO SEARCH" in ai_response:
        ai_response = ai_response.replace("READY TO SEARCH", "")
        st.session_state.search_performed = True

    # Add AI response to chat history
    st.session_state.conversation_history.append(
        {"role": "assistant", "content": ai_response}
    )

    # Rerun to update the chat display
    st.rerun()

# Perform search if ready
if st.session_state.search_performed:
    st.session_state.search_performed = False  # Reset the flag

    with st.progress(0.33, "Searching for your dream home..."):
        search_results = search_listings(
            [msg["content"] for msg in st.session_state.conversation_history]
        )

    if search_results:
        st.progress(0.66, "Simsalabim! I found you some magical homes... 🪄")
        st.spinner("Crafting a magical sales pitch...")

        personalized_pitch = personalize_listings(
            search_results,
            "\n".join(
                [
                    msg["content"]
                    for msg in st.session_state.conversation_history
                    if msg["role"] == "user"
                ]
            ),
        )

        st.session_state.conversation_history.append(
            {"role": "assistant", "content": personalized_pitch}
        )
        st.chat_message("assistant").write(personalized_pitch)

        # Display search results
        st.progress(
            1.0, "Here are some magical homes for you! ✨"
        )  # Complete progress bar
        st.info("🫣 Showing listings that match your preferences:")
        for doc, score in search_results:
            with st.expander(
                f"{doc.metadata['neighborhood']} - ${doc.metadata['price']}"
            ):
                st.write(f"**Relevance Score:** {score:.2f}")
                st.write(f"**Bedrooms:** {doc.metadata['bedrooms']}")
                st.write(f"**Bathrooms:** {doc.metadata['bathrooms']}")
                st.write(f"**Square Feet:** {doc.metadata['sqft']}")
                st.write(f"**Description:** {doc.page_content}")

        # Rerun to update the chat display with search results
        st.rerun()

    else:
        st.warning("No magical homes found matching your preferences. Let's try again!")
