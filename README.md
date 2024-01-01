# Summarize Wiki

## Introduction

This Python application utilizes Streamlit to create an interactive web-based tool for summarizing Wikipedia articles. The application fetches data from Wikipedia using the unstructured library and then utilizes open source models to generate a summary of the provided Wikipedia page.

![image](https://github.com/shresthashreejan/summarizeWiki/assets/79634187/3e3b86df-e76b-4f60-b4ac-4ed50f1cac70)


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

## Setup Models

Visit [GPT4All](https://gpt4all.io/index.html) and download required models. Extract downloaded models into `model` directory in the project root.

## Run the Application

Run the Streamlit application:

```bash
streamlit run main.py
```
