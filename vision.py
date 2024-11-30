from dotenv import load_dotenv
import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

load_dotenv()  # take environment variables from .env.

# Configure the Google Generative AI with the API key
genai.configure(api_key=os.getenv("Your_Key"))

# Function to load the new Gemini model and get responses
def get_gemini_response(input_text, image):
    model = genai.GenerativeModel('gemini-1.5-flash')  # Updated to use gemini-1.5-flash
    if input_text != "":
        response = model.generate_content([input_text, image])
    else:
        response = model.generate_content(image)
    return response.text

# Initialize our Streamlit app
st.set_page_config(page_title="Gemini Image Demo")

st.header("Gemini Application")
input_text = st.text_input("Input Prompt: ", key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image = ""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit = st.button("Tell me about the image")

# If the submit button is clicked
if submit:
    response = get_gemini_response(input_text, image)
    st.subheader("The Response is")
    st.write(response)
