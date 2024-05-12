import google.generativeai as genai
import streamlit as st
import os
from dotenv import load_dotenv
from PIL import Image


load_dotenv()

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# function to load gemini pro vision
model = genai.GenerativeModel('gemini-pro-vision')


def get_gemini_response(input, image, prompt):
    try:
        response = model.generate_content([input, image[0], prompt])
        return response.text
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        return "Failed to process the request."

def input_image_details(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")


# Initialize the streamlit app
st.set_page_config(page_title="Multi Language Invoice Extraction")
st.header("Gemini app")

input = st.text_input("Input prompt: ", key="input",)
uploaded_file = st.file_uploader(
    "Choose a image of invoice", type=['jpg', 'jpeg', 'png'])
image = ""

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded image:", use_column_width=True)

submit = st.button("Tell me about the invoice")

input_prompt = """
You are an expert in understanding invoice of onlice shopping. We will upload image as invoices and you will have to answer based on the uploaded invoice image.
"""
# When submit is clicked

if submit:
    image_data = input_image_details(uploaded_file)
    response = get_gemini_response(input_prompt, image_data, input) #!
    st.subheader("Response:")
    st.write(response)
