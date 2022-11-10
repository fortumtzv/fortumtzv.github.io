import streamlit as st
from PIL import Image



#opening the image
image = Image.open(r"C:\Users\42mar\OneDrive\Pictures\CV_Fortunato_Martinez.png")



#displaying the image on streamlit app

st.title('CV Fortunato Martinez')
st.image(image)