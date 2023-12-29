import streamlit as st
import json
import shutil

from unstructured.ingest.connector.wikipedia import SimpleWikipediaConfig
from unstructured.ingest.interfaces import PartitionConfig, ProcessorConfig, ReadConfig
from unstructured.ingest.runner import WikipediaRunner

def fetch_wikipedia_data(page_title):
    runner = WikipediaRunner(
        processor_config=ProcessorConfig(
            verbose=True,
            output_dir="output",
            num_processes=2,
        ),
        read_config=ReadConfig(),
        partition_config=PartitionConfig(),
        connector_config=SimpleWikipediaConfig(
            page_title=page_title,
            auto_suggest=False,
        ),
    )
    runner.run()

    # Replace spaces with underscores in the filename
    filename = f"{page_title.replace(' ', '-')}-summary.json"

    # Concatenate text values from json
    summary_file_path = f"./output/{filename}"
    with open(summary_file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    concatenated_text = " ".join([element["text"] for element in data])

    # Remove output folder
    shutil.rmtree("output")

    return concatenated_text

def main():
    st.set_page_config(page_title="Summarize Wiki")
    st.title("Summarize Wiki")
    page_title = st.text_input("Enter the Wikipedia page title:")

    if st.button("Summarize"):
        if page_title:
            with st.spinner('Fetching data...'):
                concatenated_text = fetch_wikipedia_data(page_title)
                st.toast('Success!')
                st.header(page_title)
                st.markdown(concatenated_text)
        else:
            st.warning("Please enter a valid page title.")

if __name__ == "__main__":
    main()