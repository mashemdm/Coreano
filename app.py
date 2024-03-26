import streamlit as st
import cv2
import numpy as np
import pytesseract
from PIL import Image

import os

st.title("Cómo se pronuncia en coreano")


# img_file_buffer = st.camera_input("Toma una Foto")
uploaded_file = st.file_uploader("Sube tu imagen en español para traducirla", type=["jpg", "jpeg", "png"])



if uploaded_file is not None:
    # To read image file buffer with OpenCV:
    img_bytes = uploaded_file.read()
    nparr = np.frombuffer(img_bytes, np.uint8)
    cv2_img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

      

        
    img_rgb = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB)
    text=pytesseract.image_to_string(img_rgb)
    st.write(text) 

def text_to_speech(text):
    translator = Translator()
    translation = translator.translate(text, dest='ko')  # Traducir al coreano
    trans_text = translation.text

    # Es posible que necesites procesar el texto coreano aquí para que se muestre correctamente en letras coreanas

    tts = gTTS(trans_text, lang='ko', slow=False)  # Generar audio en coreano
    try:
        my_file_name = text[0:20]
    except:
        my_file_name = "audio"
    tts.save(f"temp/{my_file_name}.mp3")
    return my_file_name, trans_text
    
