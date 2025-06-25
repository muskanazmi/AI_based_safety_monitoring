# preprocess.py placeholder
import cv2
import numpy as np

IMG_SIZE = (224, 224)

def preprocess_frame(frame):
    frame = cv2.resize(frame, IMG_SIZE)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = np.expand_dims(frame, axis=0)
    frame = frame / 255.0
    return frame

