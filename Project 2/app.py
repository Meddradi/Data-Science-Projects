import streamlit as st
import numpy as np
import cv2
from tensorflow.keras.models import load_model

model = load_model("digit_recognizer.h5")

st.title("🖊️ Digit Recognizer")
uploaded = st.file_uploader("Upload a digit image", type=["png","jpg","jpeg"])

if uploaded:
    file_bytes = np.asarray(bytearray(uploaded.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (28, 28)).reshape(1, 28, 28, 1) / 255.0
    pred = model.predict(img)
    st.write("Predicted Digit:", np.argmax(pred))
