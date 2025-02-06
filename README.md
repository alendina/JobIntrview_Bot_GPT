# Job Interview ChatBot


## Overview

Job Interview ChatBot is an AI-powered assistant that simulates an HR interview process. It collects information about your experience and skills, asks clarifying questions, and evaluates how well you fit a target job position. The app leverages OpenAI's API and features an interactive user interface built with Streamlit.

This project is the main assignment of the course "LLM Engineering in Practice with Streamlit & OpenAI" by [365DataScience.com](https://learn.365datascience.com/courses/llm-engineering-in-practice-with-streamlit-and-openai/introduction-to-the-course/) platform

## Live Demo

  Check out the live demo of the Job Interview Bot: [jobintrviewbotgpt-alendina.streamlit.app](https://jobintrviewbotgpt-alendina.streamlit.app)

<p align="center">
  <img width="658" alt="UI" src="https://github.com/user-attachments/assets/13da769d-2d51-43ec-9565-a3793734cfa8" />
</p>

## Features

- Conducts a structured job interview

- Gathers candidate experience and skills

- Asks follow-up questions for clarification

- Assesses candidate suitability for a given job position

- Provides AI-generated feedback

- Built with Streamlit for an interactive UI

- Uses OpenAI API for natural language processing

## Installation

To run the project locally, follow these steps:

### 1. Clone the repository

    git clone <your-repository-url>
    cd <your-repository-folder>

### 2. Install dependencies

Ensure you have Python installed (version 3.8 or later recommended). Then, install the required packages:

    pip install -r requirements.txt

### 3. Set up API Key

Create a .streamlit/secrets.toml file and add your OpenAI API key:

    [secrets]
    OPENAI_API_KEY = "your-api-key-here"

### 4. Run the application

    streamlit run my_app.py

## Project Structure

    📂 Job Interview Bot
    ├── 📄 my_app.py           # Main application file
    ├── 📄 requirements.txt    # List of dependencies
    └── 📂 .streamlit
        └── 📄 secrets.toml    # API key configuration

## Requirements

The project requires the following dependencies:

    openai>=1.61.0
    streamlit>=1.41.1
    streamlit-js-eval>=0.1.7

## Deployment

The app is deployed on Streamlit Cloud at [share.streamlit.io](https:\\share.streamlit.io.) You can deploy your own version by following Streamlit’s deployment documentation.

## License

This project is licensed under the MIT License. Feel free to use and modify it as needed.

### 🚀 Enjoy your AI-powered job interview experience!




