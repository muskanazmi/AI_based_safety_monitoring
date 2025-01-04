import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt
from IPython.display import display, clear_output

# Load the trained model
model_path = 'model path'
model = load_model(model_path)

# Define the video path
video_path = 'path of video to process'

# Define constants
IMG_SIZE = (224, 224)  # MobileNetV2 input size

# Helper function to preprocess each frame before passing it into the model
def preprocess_frame(frame):
    frame = cv2.resize(frame, IMG_SIZE)  # Resize to 224x224
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert to RGB
    frame = np.expand_dims(frame, axis=0)  # Add batch dimension
    frame = frame / 255.0  # Normalize pixel values
    return frame

# Open the video file
cap = cv2.VideoCapture(video_path)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Preprocess the frame
    processed_frame = preprocess_frame(frame)

    # Predict violence using the model
    prediction = model.predict(processed_frame)

    # Determine the label (violent or non-violent)
    label = 'Violent' if prediction >= 0.5 else 'Non-Violent'
    color = (0, 0, 255) if label == 'Violent' else (0, 255, 0)

    # Display the prediction label on the frame
    cv2.putText(frame, f'{label}: {prediction[0][0]:.2f}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2, cv2.LINE_AA)

    # Convert frame to RGB format (for displaying in matplotlib)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Display the frame in the Colab notebook
    plt.imshow(frame_rgb)
    plt.axis('off')  # Turn off axis
    display(plt.gcf())
    clear_output(wait=True)  # Clear the previous frame
    plt.pause(0.01)  # Pause for a short time to update the plot

# Release the video capture
cap.release()
