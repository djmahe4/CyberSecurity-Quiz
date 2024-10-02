# CyberSecurity-Quiz

## Project Setup

This project uses Streamlit and Google Generative AI. Follow the steps below to set up the environment, install dependencies, and run the application.

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/djmahe4/CyberSecurity-Quiz
    cd CyberSecurity-Quiz
    ```

2. **Create and activate a virtual environment (optional but recommended):**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```sh
    pip install -r requirements.txt
    ```

### Configuration

1. **Set up the Google Generative AI API key:**

    - Go to https://ai.google.dev to get the API key.
    - Add your API key to the `.env` file:

    ```env
    GENERATIVE_AI_KEY='your_api_key_here'
    ```

### Running the Application

1. **Run the `main.py` script:**

    ```sh
    streamlit run main.py
    ```

### Notes

- Ensure that your `.env` file is not included in version control to keep your API key secure.
- For more information on obtaining a Google Generative AI API key, refer to the [Google AI documentation](https://ai.google.dev/gemini-api/docs/api-key).
