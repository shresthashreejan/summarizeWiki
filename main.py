import streamlit as st
import json
import shutil
import os

from unstructured.ingest.connector.wikipedia import SimpleWikipediaConfig
from unstructured.ingest.interfaces import PartitionConfig, ProcessorConfig, ReadConfig
from unstructured.ingest.runner import WikipediaRunner

from langchain.chains import LLMChain
from langchain.llms import GPT4All
from langchain.prompts import PromptTemplate

def fetch_wikipedia_data(page_title, selected_model):
    with st.spinner('Fetching data...'):
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

    with st.spinner('Loading model...'):
        template = """Summarize the following text: {concatenated_text} Answer: """
        prompt = PromptTemplate(template=template, input_variables=["concatenated_text"])
        model_path = f"./model/{selected_model}"
        llm = GPT4All(model=model_path, device='gpu', verbose=True)
        llm_chain = LLMChain(prompt=prompt, llm=llm)
        output = llm_chain.run(concatenated_text)

    return output

def main():
    st.set_page_config(page_title="Summarize Wiki")
    st.title("Summarize Wiki")
    page_title = st.text_input("Enter Wikipedia page title")

    model_folder_path = './model'
    model_files = os.listdir(model_folder_path)
    selected_model = st.selectbox("Select model", model_files)
    st.write("You are using", selected_model)

    if st.button("Summarize"):
        if page_title:
            summary = fetch_wikipedia_data(page_title, selected_model)
            st.toast('Success!')
            st.header(page_title)
            st.markdown(summary)
        else:
            st.warning("Please enter a valid page title.")

if __name__ == "__main__":
    main()