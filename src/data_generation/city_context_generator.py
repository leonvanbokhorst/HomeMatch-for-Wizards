import pandas as pd
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI


class CityContextGenerator:
    def __init__(self, llm):
        self.llm = llm
        self.prompt = PromptTemplate(
            input_variables=["example"],
            template="""Generate a very short, realistic but completely made-up context description for a city or neighborhood that could be used in real estate listings for the Harry Potter series. Include:
            1. Neighborhood name (be creative and diverse)
            2. General location or region
            3. Population size category (small town, mid-size city, large metropolis, etc.)
            4. One or two defining characteristics or attractions
            5. Economic base or major industries

            Provide this in a concise paragraph format, suitable for use in generating real estate listings.

            Example: {example}

            Now, generate a fantastic unique new city context:""",
        )

    def generate_contexts(self, num_contexts: int = 10) -> pd.DataFrame:
        contexts = []
        for _ in range(num_contexts):
            context = self.llm.invoke(
                self.prompt.format(
                    example="Zenithville Dwarf Parking, nestled in the heart of the Purple Pot Midwest, is a charming mid-size city of about 150,000 broom stick students. Known for its vibrant magic arts scene and annual hot air soap bubble festival, Zenithville has recently become a hub for fairy tech wizards, blending its traditional wizardry schools with a growing innovation sector."
                )
            )
            contexts.append(context.content.strip())
        return pd.DataFrame({"city_context": contexts})

    def save_to_csv(self, df: pd.DataFrame, filename: str = "city_contexts.csv"):
        df.to_csv(filename, index=False)
        print(f"City contexts saved to {filename}")

    def load_from_csv(self, filename: str = "city_contexts.csv") -> pd.DataFrame:
        df = pd.read_csv(filename)
        print(f"City contexts loaded from {filename}")
        return df
