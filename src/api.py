from flask import Flask, request, jsonify
import os
import cv2
import numpy as np
import tensorflow as tf
from werkzeug.utils import secure_filename

from config import RAW_IMAGE_DIR, IMAGE_SIZE
from logger import get_logger
from model import build_cnn_model

logger = get_logger(__name__)
app = Flask(__name__)

# Load trained model
MODEL_PATH = "model.h5"
model = tf.keras.models.load_model(MODEL_PATH)
class_names = ["Cat", "Dog"]  # Adjust this based on your model training

@app.route("/", methods=["GET"])
def root():
    return jsonify({"message": "Welcome to the Image Classification API"})

@app.route("/upload/", methods=["POST"])
def upload_image():
    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "Empty filename"}), 400

    filename = secure_filename(file.filename)
    file_path = os.path.join(RAW_IMAGE_DIR, filename)
    os.makedirs(RAW_IMAGE_DIR, exist_ok=True)
    file.save(file_path)

    logger.info(f"Received file: {filename}")

    # Read image and preprocess
    img = cv2.imread(file_path)
    if img is None:
        return jsonify({"error": "Invalid image"}), 400

    resized = cv2.resize(img, IMAGE_SIZE)
    normalized = resized / 255.0
    brightness = float(np.mean(normalized))
    input_tensor = np.expand_dims(normalized, axis=0)

    # Predict
    preds = model.predict(input_tensor)
    predicted_class = class_names[int(np.argmax(preds))]

    logger.info(f"Prediction: {predicted_class}, Brightness: {brightness:.2f}")

    return jsonify({
        "filename": filename,
        "predicted_class": predicted_class,
        "brightness": brightness,
        "width": img.shape[1],
        "height": img.shape[0]
    })

if __name__ == "__main__":
    app.run(debug=True)
