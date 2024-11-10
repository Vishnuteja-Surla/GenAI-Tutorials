# Narada AI - Your AI Chat Bot

Narada AI is an interactive web application powered by Google’s Generative AI model, "Gemini," built using LangChain and Streamlit. This app allows users to ask questions and receive intelligent, AI-generated responses. It serves as a helpful tool for answering queries across a wide range of topics.

## Features

- **AI-Powered Responses**: Uses the "Gemini" model from Google Generative AI for intelligent, conversational responses.
- **User-Friendly Interface**: Built with Streamlit for a simple and clean user interface.
- **Customizable**: Prompt templates and output parsing can be easily modified for specific use cases.

## Installation

To set up Narada AI on your local machine, follow these steps:

1. **Clone the repository**:

    ```bash
    git clone https://github.com/Vishnuteja-Surla/GenAI-Tutorials/tree/master/ChatBot
    ```

2. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

## Setup

1. **API Keys**:

    - Obtain your `GOOGLE_API_KEY` from the Google Cloud Console.
    - Set up an API key for LangChain if required.

2. **Environment Variables**:

    - Create a `.env` file in the root directory of your project with the following content:

        ```.env
        GOOGLE_API_KEY=your_google_api_key
        LANGCHAIN_API_KEY=your_langchain_api_key
        ```

    - The script uses `python-dotenv` to load these API keys into environment variables, making them accessible in the code.

## Usage

1. **Run the application**:

    Start the Streamlit app by running the following command:

    ```bash
    streamlit run app.py
    ```

2. **Interact with Narada AI**:

    - After launching, you’ll see a text input box titled “Ask anything you want.”
    - Enter a question, and Narada AI will provide an AI-generated response.

## Code Structure

- **API Key Setup**: Sets up API keys using environment variables, allowing for secure and modular configuration.
- **Prompt Template**: Defines a prompt template for structuring the conversation. It guides the AI assistant to respond helpfully to user questions.
- **Streamlit Interface**: A Streamlit-based web interface allows user interaction with a simple input box for questions.
- **Gemini Language Model**: Integrates Google’s "Gemini" model for AI-powered responses.
- **Execution Chain**: Combines the prompt, language model, and output parser in a chain to generate and display responses.

## Technologies Used

- **LangChain**: A framework for language model applications, used for prompt templates and output parsing.
- **Streamlit**: A Python framework for creating interactive web apps.
- **Google Generative AI (Gemini)**: Google’s state-of-the-art language model for natural language processing tasks.
- **dotenv**: Used to manage environment variables securely.
