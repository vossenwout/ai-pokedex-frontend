# Pokedex Frontend

This project is a chat interface for my AI Pokédex, built with Streamlit.

<img src="data/banner.png" alt="Pokedex Frontend Screenshot" width="300"/>

## AI Pokedex Project Repos

These are the repos that are used to create and run the AI Pokedex.

- [Knowledgebase and Scraper](https://github.com/vossenwout/ai-pokedex-scraper)
- [Assistant API](https://github.com/vossenwout/ai-pokedex-assistant-api)
- [Frontend](https://github.com/vossenwout/ai-pokedex-frontend)
- [Evaluation Framework](https://github.com/vossenwout/ai-pokedex-rag-evaluation)

I created a youtube video where I explain the project: https://www.youtube.com/watch?v=dQw4w9WgXcQ

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.10 or higher
- [Poetry](https://python-poetry.org/docs/#installation) for dependency management. You can install it with the following commands:
  - **macOS, Linux, or WSL:**
    ```bash
    curl -sSL https://install.python-poetry.org | python3 -
    ```
  - **Windows (PowerShell):**
    ```powershell
    (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
    ```
- A running instance of my [Pokedex RAG API](https://github.com/vossenwout/ai-pokedex-assistant-api).

## Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/vossenwout/ai-pokedex-frontend
    cd ai-pokedex-frontend
    ```

2.  **Install dependencies:**

    Use Poetry to install the required Python packages.

    ```bash
    poetry install
    ```

## Configuration

This frontend requires a connection to the Pokedex RAG API. The URL of this service is configured via an environment variable.

Create a `.env` file in the root of the project:

```
touch .env
```

Add the following line to the `.env` file, pointing to the URL where your backend service is running:

```
ASSISTANT_API_URL=http://localhost:8000/chat/
```

If your backend is running on a different URL, make sure to update it accordingly.

## Running the Frontend

To start the Streamlit application, run the following command in your terminal:

```bash
streamlit run src/pokedex_frontend/frontend.py
```

Open your web browser and navigate to the local URL provided by Streamlit (usually `http://localhost:8501`).
