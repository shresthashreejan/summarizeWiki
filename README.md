# Summarize Wiki

## Introduction

This Python application utilizes Streamlit to create an interactive web-based tool for summarizing Wikipedia articles. The application fetches data from Wikipedia using the unstructured library and then utilizes GPT4All models to generate a summary of the provided Wikipedia page.

## Prerequisites

- Python 3.x installed on your system

## Setup

1. Clone the repository (if you haven't already):

    ```bash
    git clone https://github.com/shresthashreejan/summarizeWiki.git
    cd summarizeWiki
    ```

2. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

4. Install dependencies using pip:

    ```bash
    pip install -r requirements.txt
    ```

## Download Models

Visit the [GPT4All page](https://gpt4all.io/index.html) and download required models. Extract downloaded models into `model` directory in the project root.

## Run the Application

Run the Streamlit application:

```bash
streamlit run main.py
```