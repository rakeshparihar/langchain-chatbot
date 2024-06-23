# LangChain Chatbot

A chatbot application leveraging LangChain, OpenAI, and Streamlit for creating an interactive AI assistant.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Environment Variables](#environment-variables)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This repository contains a chatbot application built using LangChain, OpenAI, and Streamlit. The chatbot serves as an interactive AI assistant that can respond to user queries. The application demonstrates the integration of various AI tools and frameworks to create a functional chatbot.

## Features

- Interactive AI assistant
- Utilizes LangChain for language model management
- Built with Streamlit for easy web deployment
- Uses OpenAI's GPT-3.5-turbo for generating responses

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/rakeshparihar/langchain-chatbot.git
    cd langchain-chatbot
    ```

2. **Create a virtual environment:**

    ```sh
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

3. **Install dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. **Set up environment variables:**

    Create a `.env` file in the root directory and add your API keys:

    ```plaintext
    OPENAI_API_KEY=your_openai_api_key
    LANGCHAIN_API_KEY=your_langchain_api_key
    LANGCHAIN_PROJECT=langchain_tut
    ```

2. **Run the application:**

    ```sh
    streamlit run chatbot/app.py
    ```

3. **Access the chatbot:**

    Open your web browser and go to `http://localhost:8501` to interact with the chatbot.

## Environment Variables

The following environment variables need to be set in the `.env` file:

- `OPENAI_API_KEY`: Your OpenAI API key.
- `LANGCHAIN_API_KEY`: Your LangChain API key.
- `LANGCHAIN_PROJECT`: Your LangChain project name.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for review.

1. **Fork the repository**
2. **Create a new branch:**

    ```sh
    git checkout -b feature/your-feature-name
    ```

3. **Make your changes and commit them:**

    ```sh
    git commit -m 'Add some feature'
    ```

4. **Push to the branch:**

    ```sh
    git push origin feature/your-feature-name
    ```

5. **Submit a pull request**

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
