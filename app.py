import streamlit as st
import cv2
import numpy as np
import pytesseract
from PIL import Image

import os
from gtts import gTTS
from googletrans import Translator

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
    
      if st.button("Generar Audio en Coreano"):
        result, output_text = text_to_speech(text)
        audio_file_path = f"temp/{result}.mp3"
        audio_file = open(audio_file_path, "rb")
        audio_bytes = audio_file.read()
        st.markdown("## Reproducir Audio en Coreano:")
        st.audio(audio_bytes, format="audio/mp3")

        st.markdown(f"## Texto traducido al coreano:")
        st.write(output_text)

def text_to_speech(text):
    translator = Translator()
    translation = translator.translate(text, dest='ko')  # Traducir al coreano
    trans_text = translation.text

    tts = gTTS(trans_text, lang='ko', slow=False)  # Generar audio en coreano
    try:
        my_file_name = text[0:20]
    except:
        my_file_name = "audio"
    tts.save(f"temp/{my_file_name}.mp3")
    return my_file_name, trans_text
    
  
    
