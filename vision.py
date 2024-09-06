from dotenv import load_dotenv
load_dotenv()  # loading for environment variables

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image  # Correct import statement

genai.configure(api_key=os.getenv("GOOGLE_API_KEy"))

# function to load gemini ai pro model
model = genai.GenerativeModel("gemini-pro-vision")

def get_gemini_response(input, image):
    if input != "":
        response = model.generate_content([input, image])
    else:
        response = model.generate_content(image)
    return response.text

st.set_page_config(page_title="Abhi's Image LLM")
st.header("ABHI LLM Application")

input_text = st.text_input("Input: ", key="input")

uploaded_file = st.file_uploader("Choose an image ...", type=["jpg", 'jpeg', 'png'])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)  # Corrected variable name
    st.image(image, caption="Uploaded image.", use_column_width=True)

submit = st.button("Tell me about the image")  # Corrected button spelling

# If submit is clicked
if submit:
    response = get_gemini_response(input_text, image)
    st.subheader("The response is ")
    st.write(response)
