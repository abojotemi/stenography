from io import BytesIO
import os
import random
import string
import streamlit as st
from PIL import Image
from encode import decode, encode

st.title("Steganography")
img_types = ["jpg", "jpeg", "webp", "png", "svg", 'gif']

tab1, tab2 = st.tabs(["Encode", "Decode"])
with tab1:
    st.header("Encode Image Here")
    img1 = st.file_uploader("Original Image Here", img_types)
    if img1:
        width, height = Image.open(img1).size
        st.image(img1, width=width)
        img2 = st.file_uploader("Image to encode here", img_types)

        if img2:
            st.image(img2, width=width)
            button = st.button("encode")
            if button:
                res = encode(img1, img2, (width, height))
                st.image(res, "Resultant Image", width=width)
                enc_img = Image.fromarray(res)
                buff = BytesIO()
                enc_img.save(buff, format='PNG')
                byte_im = buff.getvalue()
                st.download_button(
                    label="Download Encoded Image",
                    data=byte_im,
                    file_name= f"{"".join(random.choices(string.ascii_lowercase, k=10))}.png",
                    mime = 'image/png'
                )
with tab2:
    st.header("Decode Image here")
    img = st.file_uploader("Image to decode here", img_types)
    
    if img:
        width, height = Image.open(img).size
        st.image(img, width=width)
    
        button = st.button('decode')    
        if button:
            res = decode(img, (width, height))
            st.image(res, width=width)
