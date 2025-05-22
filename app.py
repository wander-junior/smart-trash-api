# app.py
from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
from PIL import Image
import io
import os

app = Flask(__name__)

# Load TFLite model and labels
interpreter = tf.lite.Interpreter(model_path="model_unquant.tflite")
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

with open("labels.txt", "r") as f:
    labels = [line.strip() for line in f.readlines()]

def preprocess_image(image_bytes):
    img = Image.open(io.BytesIO(image_bytes)).convert('RGB')
    img = img.resize((224, 224))  # adjust if needed
    img = np.expand_dims(img, axis=0)
    img = np.array(img, dtype=np.float32) / 255.0
    return img

@app.route("/classify", methods=["POST"])
def classify():
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    image = request.files['image'].read()
    input_data = preprocess_image(image)

    interpreter.set_tensor(input_details[0]['index'], input_data)
    interpreter.invoke()

    output_data = interpreter.get_tensor(output_details[0]['index'])[0]
    prediction = labels[np.argmax(output_data)]

    return jsonify({
        "prediction": prediction,
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
