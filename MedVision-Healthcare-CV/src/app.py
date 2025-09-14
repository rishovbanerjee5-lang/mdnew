import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.title("MedVision - Healthcare CV Demo")
st.write("Upload a medical image (e.g., X-ray) for anomaly detection.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Medical Image', use_column_width=True)
    
    # Dummy prediction (replace with actual model)
    st.write("Analyzing image...")
    st.success("Result: Possible abnormality detected in highlighted region.")
