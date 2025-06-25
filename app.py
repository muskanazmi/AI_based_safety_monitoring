# Streamlit app will be generated here
import streamlit as st
import cv2
import numpy as np
from src.preprocess import preprocess_frame
from src.predict import load_trained_model, predict_violence
import tempfile

st.set_page_config(layout="wide")
st.title("🔍 Violence Detection in Video")
st.markdown("Upload a video and let the model detect violent scenes in real-time.")

uploaded_file = st.file_uploader("Upload a video", type=["mp4", "avi"])
model = load_trained_model("models/violence_model.h5")

if uploaded_file is not None:
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(uploaded_file.read())
    cap = cv2.VideoCapture(tfile.name)
    stframe = st.empty()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        processed = preprocess_frame(frame)
        pred = predict_violence(model, processed)
        label = "Violent" if pred <= 0.5 else "Non-Violent"
        color = (0, 0, 255) if label == "Violent" else (0, 255, 0)

        cv2.putText(frame, f'{label} ({pred:.2f})', (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
        stframe.image(frame, channels="BGR")

    cap.release()

