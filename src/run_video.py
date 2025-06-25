# run_video.py placeholder
import cv2
import numpy as np
from preprocess import preprocess_frame
from predict import load_trained_model, predict_violence

# Load model
model = load_trained_model("models/violence_model.h5")

# Path to your test video
video_path = "demo_video.mp4"

# Open the video file
cap = cv2.VideoCapture(video_path)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    processed = preprocess_frame(frame)
    pred = predict_violence(model, processed)

    label = "Violent" if pred >= 0.5 else "Non-Violent"
    color = (0, 0, 255) if label == "Violent" else (0, 255, 0)

    # Add prediction label to frame
    cv2.putText(frame, f"{label}: {pred:.2f}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2, cv2.LINE_AA)

    cv2.imshow("Violence Detection", frame)

    # Press 'q' to quit early
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
