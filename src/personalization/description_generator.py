from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from typing import Dict


class PersonalizedDescriptionGenerator:
    def __init__(self, model_name: str = "gpt-4o-mini", temperature: float = 0.7):
        self.llm = ChatOpenAI(model_name=model_name, temperature=temperature)
        self.prompt = PromptTemplate(
            input_variables=["listing", "user_preferences"],
            template="""
            You are a magical, but sneaky, realty salesperson from the Harry Potter series. 
            Use the following listing as inspiration to make a compelling offer to the user. 
            The user has these preferences: {user_preferences}
            
            Original listing:
            {listing}
            
            Create a personalized, engaging sales pitch for this listing, highlighting how it matches the user's preferences.
            Be creative and whimsical, but ensure all factual information remains accurate.
            Your response should be in the style of a magical real estate agent addressing the potential buyer directly.
            """,
        )
        self.chain = LLMChain(llm=self.llm, prompt=self.prompt)

    def generate_description(self, listing: Dict, user_preferences: str) -> str:
        listing_info = f"""
        Neighborhood: {listing['neighborhood']}
        Price: ${listing['price']}
        Bedrooms: {listing['bedrooms']}
        Bathrooms: {listing['bathrooms']}
        Square Feet: {listing['sqft']}
        Description: {listing['description']}
        """
        return self.chain.run(listing=listing_info, user_preferences=user_preferences)
