# HomeMatch: Magical Real Estate Finder

HomeMatch is an innovative application that uses advanced AI techniques to help wizards and witches find their perfect magical dwelling. It leverages Large Language Models (LLMs) and vector databases to create personalized property searches and enchanting descriptions.

![Mr. Sneekers](homematch-sneaky-salesperson.webp)

## Features

- Generate diverse magical city contexts and property listings
- Perform semantic searches based on user preferences
- Create personalized property descriptions
- Interactive chat interface for a magical house-hunting experience

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/homematch.git
cd homematch
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

To run the HomeMatch application:

```bash
python app.py
```

This will start the Streamlit app. Open your web browser and navigate to the URL provided in the terminal (usually http://localhost:8501).

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
└── app.py
```

- `src/`: Contains the main components of the application
  - `data_generation/`: Modules for generating city contexts and property listings
  - `vector_store/`: Vector database integration for efficient searching
  - `semantic_search/`: Semantic search engine implementation
  - `personalization/`: Personalized description generator
  - `ui/`: Streamlit-based user interface
- `tests/`: Unit tests for each component
- `requirements.txt`: List of Python dependencies
- `app.py`: Script to run the Streamlit app

## Contributing

Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.
