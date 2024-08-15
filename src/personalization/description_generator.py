from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.schema import Document
from typing import Dict, List


class PersonalizedDescriptionGenerator:
    def __init__(self, model_name: str = "gpt-4o-mini", temperature: float = 0.7):
        self.llm = ChatOpenAI(model_name=model_name, temperature=temperature)

        # Initialize the offer chain
        self.offer_prompt = PromptTemplate(
            input_variables=["listing", "user_preferences"],
            template="""
            You are mr. Sneekrs, a magical, but very sneaky realty salesperson like straight from the Harry Potter series. 
            Use the following listing as inspiration to make a compelling offer to the user. 
            The user has these preferences: {user_preferences}
            
            Original listing:
            {listing}
            
            Create a personalized, engaging sales pitch for this listing, highlighting how it matches the user's preferences.
            Be creative and whimsical, but ensure all factual information remains accurate, so be sure to sum up the listings details.

            Start by saying something cheesy like "I've magically found something that matches your preferences: - but think of something better than that!"
            """,
        )
        self.offer_chain = LLMChain(llm=self.llm, prompt=self.offer_prompt)

        # Initialize the response chain
        self.response_prompt = PromptTemplate(
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
        self.response_chain = LLMChain(llm=self.llm, prompt=self.response_prompt)

    def get_offer(self, listings: List[Document], user_preferences: str) -> str:

        return self.offer_chain.run(listing=listings, user_preferences=user_preferences)

    def get_response(self, conversation_history: str, user_input: str) -> str:
        return self.response_chain.run(
            history=conversation_history, human_input=user_input
        )
