import google.generativeai as genai
import streamlit as st
import os
from PIL import Image
from dotenv import load_dotenv
load_dotenv()


genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

model = genai.GenerativeModel("gemini-pro-vision")

def get_response(input, image):
    if input != "":
        response = model.generate_content([input, image])
    else:
        response = model.generate_content(image)
    return response.text

st.set_page_config(page_title="Gemini image generator")
st.header("Gemini application")
input = st.text_input("Input Prompt: ", key="input")

upload_file = st.file_uploader("Choose an image...", type=["jpg","jpeg","png"])
image = ""
if upload_file is not None:
    image = Image.open(upload_file)
    st.image(image, caption="Uploaded image", use_column_width=True)

submit = st.button("Tell me about the image")

#  if submit is clicked
if submit:
    response = get_response(input, image)

    st.subheader("Response:")
    st.write(response)
