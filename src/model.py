import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, accuracy_score
import matplotlib.pyplot as plt
import numpy as np

from config import IMAGE_SIZE
from logger import get_logger

logger = get_logger(__name__)

def build_cnn_model(input_shape=(IMAGE_SIZE[0], IMAGE_SIZE[1], 3), num_classes=2):
    """Builds and compiles a simple CNN model."""
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=input_shape),
        MaxPooling2D(2, 2),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D(2, 2),
        Flatten(),
        Dense(128, activation='relu'),
        Dropout(0.5),
        Dense(num_classes, activation='softmax')
    ])

    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    logger.info("CNN model built and compiled.")
    return model

def train_model(model, train_data, val_data, epochs=15, model_path='model.h5'):
    """Train the model with early stopping and save it."""
    early_stop = EarlyStopping(patience=3, restore_best_weights=True)
    reduce_lr = ReduceLROnPlateau(patience=2, factor=0.2)

    logger.info("Starting training...")
    history = model.fit(
        train_data,
        validation_data=val_data,
        epochs=epochs,
        callbacks=[early_stop, reduce_lr]
    )

    model.save(model_path)
    logger.info(f"Model saved to {model_path}")
    return history

def evaluate_model(model, test_data):
    """Evaluate accuracy and show confusion matrix."""
    logger.info("Evaluating model...")
    y_true = []
    y_pred = []

    for images, labels in test_data:
        preds = model.predict(images)
        y_true.extend(tf.argmax(labels, axis=1).numpy())
        y_pred.extend(np.argmax(preds, axis=1))

    acc = accuracy_score(y_true, y_pred)
    cm = confusion_matrix(y_true, y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm)
    disp.plot(cmap='Blues')
    plt.title(f"Accuracy: {acc:.2%}")
    plt.show()

    logger.info(f"Test Accuracy: {acc:.2%}")
