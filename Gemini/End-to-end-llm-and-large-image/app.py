import google.generativeai as genai
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()


genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

model = genai.GenerativeModel("gemini-pro")

def get_response(question):
    response = model.generate_content(question)
    return response.text

# Streamlit:
st.set_page_config(page_title="Q&A Demo")
st.header("Gemini Pro Application")
input = st.text_input("Input: ", key="input")
submit = st.button("Ask the question...")

# When submit is clicked
if submit:
    response = get_response(input)
    st.subheader("Result: ")
    st.write(response)