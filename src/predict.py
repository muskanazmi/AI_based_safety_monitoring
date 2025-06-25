# predict.py placeholder
from tensorflow.keras.models import load_model

def load_trained_model(path):
    return load_model(path)

def predict_violence(model, processed_frame):
    prediction = model.predict(processed_frame)
    return prediction[0][0]

