import streamlit as st
from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv
import os

load_dotenv()

endpoint = "xxxxxxxx"
key = "https://xxxxx.cognitiveservices.azure.com/"

client = DocumentAnalysisClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(key)
)

st.title("Azure OCR App")

uploaded_file = st.file_uploader(
    "画像をアップロードしてください",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file is not None:

    st.image(uploaded_file, caption="Uploaded Image")

    poller = client.begin_analyze_document(
        "prebuilt-read",
        document=uploaded_file
    )

    result = poller.result()

    extracted_text = ""

    for page in result.pages:
        for line in page.lines:
            extracted_text += line.content + "\n"

    st.subheader("OCR Result")
    st.text_area(
        "Extracted Text",
        extracted_text,
        height=300
    )