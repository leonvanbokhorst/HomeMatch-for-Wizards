# HomeMatch: Magical Real Estate Finder

[![RunTests](https://github.com/leonvanbokhorst/HomeMatch-for-Wizards/actions/workflows/python-app.yml/badge.svg)](https://github.com/leonvanbokhorst/HomeMatch-for-Wizards/actions/workflows/python-app.yml)
[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/leonvanbokhorst/homematch/main/HomeMatch.py)
[![OpenAI](https://img.shields.io/badge/OpenAI-API-08B9D1.svg)](https://platform.openai.com/docs/guides/)
[![ChromaDB](https://img.shields.io/badge/ChromaDB-local-08B9D1.svg)](https://chromadb.com/docs/guides/)

HomeMatch is an innovative application that uses advanced AI techniques to help wizards and witches find their perfect magical dwelling. It leverages Large Language Models (LLMs) and vector databases to create personalized property searches and enchanting descriptions.

![Mr. Sneekers](homematch-sneaky-salesperson.webp)

## Features

- Generate diverse magical city contexts and property listings
- Perform semantic searches based on user preferences
- Create personalized property descriptions
- Interactive chat interface for a magical house-hunting experience

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

To run the HomeMatch application:

```bash
python app.py
```

This will start the Streamlit app. Open your web browser and navigate to the URL provided in the terminal (usually <http://localhost:8501>).

## Project Structure

```ascii
homematch/
├── src/
│   ├── data_generation/
│   ├── vector_store/
│   ├── semantic_search/
│   ├── personalization/
│   └── ui/
├── tests/
│   ├── test_data_generation.py
│   ├── test_vector_store.py
│   ├── test_semantic_search.py
│   └── test_personalization.py
├── requirements.txt
├── README.md
└── HomeMatch.py
└── HomeMatch.ipynb
```

- `src/`: Contains the main components of the application
  - `data_generation/`: Modules for generating city contexts and property listings
  - `vector_store/`: Vector database integration for efficient searching
  - `semantic_search/`: Semantic search engine implementation
  - `personalization/`: Personalized description generator
  - `ui/`: Streamlit-based user interface
- `tests/`: Unit tests for each component
- `requirements.txt`: List of Python dependencies
- `HomeMatch.py`: Script to run the Streamlit app
- `HomeMatch.ipynb`: Jupyter notebook for exploring the application components

## Contributing

Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.
