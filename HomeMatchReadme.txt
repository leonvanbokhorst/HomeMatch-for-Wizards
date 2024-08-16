# HomeMatch: Magical Real Estate Finder

HomeMatch is an innovative application that uses advanced AI techniques to help wizards and witches find their perfect magical dwelling. It leverages Large Language Models (LLMs) and vector databases to create personalized property searches and enchanting descriptions.

## Features

- **Magical Property Search**: Find your dream home by specifying your preferences, such as location, price, and number of rooms.
- **Enchanting Descriptions**: Get detailed descriptions of the properties, written by mister Sneekrs, our sneaky real estate agent.
- **Personalized Recommendations**: Discover similar properties based on your preferences and feedback.
- **Sneaky Salesperson**: Meet Mr. Sneekrs, the virtual salesperson who will guide you through the process and tries to sell you the best properties.

## Project Structure

- [`HomeMatch.py`](HomeMatch.py): Main application file containing the Streamlit interface.
- [`HomeMatch.ipynb`](HomeMatch.ipynb): Jupyter notebook with development code and explanations.
- `src/`: Source code directory
  - `personalization/`: Personalization logic
    - [`description_generator.py`](src/personalization/description_generator.py): Generates personalized property descriptions
  - `semantic_search/`: Semantic search functionality
    - [`vector_store.py`](src/semantic_search/vector_store.py): Handles vector storage and similarity search
- `tests/`: Unit tests
  - [`test_description_generator.py`](tests/test_description_generator.py): Tests for the description generator
  - [`test_vector_store.py`](tests/test_vector_store.py): Tests for the vector store
- `chroma.db/`: Directory for ChromaDB vector database (generated at runtime)
- [`homematch_listings.json`](homematch_listings.json) : JSON file containing generated property listings data
- [`homematch_city_contexts.csv`](homematch_city_contexts.csv): CSV file with city context data
- [`requirements.txt`](requirements.txt): List of Python dependencies
- [`README.md`](README.md): Project documentation and setup instructions
- [`homematch-app.jpg`](homematch-app.jpg): Screenshot of the application used in the readme file
- [`homematch-sneaky-salesperson.webp`](homematch-sneaky-salesperson.webp): Image of Mr. Sneekrs, the virtual salesperson used in the application
- [`pytest.ini`](pytest.ini): Configuration file for pytest

Note: The `.github` and `.vscode` directories contain configuration files for GitHub Actions and Visual Studio Code respectively.

## Additional Files

To meet specific submission requirements, the following files have been included:

- [`HomeMatchReadme.txt`](HomeMatchReadme.txt): A plain text version of the README.
- [`homematch_listings.txt`](homematch_listings.txt): A plain text version of the property listings data.
- [`homematch_city_contexts.txt`](homematch_city_contexts.txt): A plain text version of the city contexts data.

These files contain the same information as their JSON/CSV counterparts but in a plain text format for easier review if needed.

- [`screenshot-1.jpg`](screenshot-1.jpg): A screenshot of mr. Sneekrs in conversation to figure out your preferences and find the perfect home.
- [`screenshot-2.jpg`](screenshot-2.jpg): A screenshot of the personalized listing(s) offer mr. Sneekrs made crafted for the user.

## Technologies

- **Streamlit**: Open-source app framework for Machine Learning and Data Science projects.
- **OpenAI API**: Text generation API for creating property descriptions, conversation responses and personalized recommendations.
- **ChromaDB**: Vector database for similarity search and retrieval of property listings.
- **Langchain**: Framework for building AI-powered applications.

## Installation

- Clone the repository:

```bash
git clone https://github.com/your-username/homematch.git
cd homematch
```

- Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
```

- Install the required packages:

```bash
pip install -r requirements.txt
```

Get your OpenAI API key from the [OpenAI website](https://platform.openai.com/account/api-keys) and set it as an environment variable in a `.env` file:

```bash
echo "OPEN_AI_API_KEY=<your-api-key>" > .env
```

## Usage

To run the HomeMatch application, open a terminal and run the following command:

```bash
streamlit run HomeMatch.py
```

This will start the Streamlit app. Open your web browser and navigate to the URL provided in the terminal (usually <http://localhost:8501>).

## Contributing

Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.
