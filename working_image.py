import streamlit as st
from google import genai
from dotenv import load_dotenv
import os
from PIL import Image



# loading the environment variable

load_dotenv()

my_api_key = os.getenv("GEMINI_API_KEY")

# initializing a client

client = genai.Client(api_key = my_api_key)


images = st.file_uploader(
       "Upload the photos of your notes",
       type=['jpg','jpeg','png'],
       accept_multiple_files = True
                     )

if images:
    
    
    # converting streamlit image to pillow image tha is readable to machine
    pil_images =[]

    for img in images:
        pil_img = Image.open(img)
        pil_images.append(pil_img)

    

    
    prompt ="""Summerize the picture in note fo rmae at max 100 woord ,make sure to add necessary markdown to differentiate different section"""


    response = client.models.generate_content(
        model = "gemini-3-flash-preview",
        contents = [images,prompt]
    )

    st.text(response.text)