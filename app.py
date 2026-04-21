import streamlit as st
import tensorflow as tf
import json
import numpy as np
from PIL import Image

# ===== Load model =====
model = tf.keras.models.load_model("garbage_classifier.h5")

with open("class_indices.json") as f:
    class_indices = json.load(f)

inv_class_map = {v: k for k, v in class_indices.items()}

IMG_SIZE = (224, 224)

st.title("♻️ Garbage Classification")
st.write("Upload an image of waste")

uploaded_file = st.file_uploader(
    "Choose an image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded image", width=300)

    img = image.resize(IMG_SIZE)
    img_array = np.expand_dims(np.array(img) / 255.0, axis=0)

    prediction = model.predict(img_array)
    class_id = prediction.argmax()
    label = inv_class_map[class_id]
    confidence = prediction[0][class_id]

    st.success(f"🧠 Prediction: **{label}**")
    st.write(f"Confidence: {confidence:.2%}")