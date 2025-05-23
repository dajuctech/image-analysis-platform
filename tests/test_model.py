from src.model import build_cnn_model
import tensorflow as tf
import numpy as np
from config import IMAGE_SIZE

def test_model_output_shape():
    model = build_cnn_model(num_classes=2)
    dummy_input = tf.random.uniform((1, IMAGE_SIZE[0], IMAGE_SIZE[1], 3))
    prediction = model(dummy_input)
    assert prediction.shape == (1, 2)

def test_model_trainability():
    model = build_cnn_model(num_classes=2)
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    X = tf.random.uniform((10, IMAGE_SIZE[0], IMAGE_SIZE[1], 3))
    y = tf.keras.utils.to_categorical(np.random.randint(0, 2, size=(10,)))

    history = model.fit(X, y, epochs=1, verbose=0)
    assert history.history["loss"]
