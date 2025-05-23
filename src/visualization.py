import os
import cv2
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from config import METADATA_CSV

def plot_class_distribution():
    """Plot the distribution of image classes (if 'label' column exists)."""
    df = pd.read_csv(METADATA_CSV)
    if 'label' in df.columns:
        sns.countplot(x='label', data=df)
        plt.title("Class Distribution")
        plt.xlabel("Class")
        plt.ylabel("Count")
        plt.show()
    else:
        print("[INFO] No 'label' column found in metadata.")

def show_sample_images(n=5):
    """Display sample images from metadata CSV."""
    df = pd.read_csv(METADATA_CSV)
    sample = df.sample(min(n, len(df)))

    for _, row in sample.iterrows():
        path = row['processed_path']
        img = cv2.imread(path)
        if img is not None:
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            plt.imshow(img_rgb)
            plt.title(row['filename'])
            plt.axis('off')
            plt.show()

def plot_brightness_distribution():
    """Plot histogram of image brightness values."""
    df = pd.read_csv(METADATA_CSV)
    if 'brightness' in df.columns:
        sns.histplot(df['brightness'], bins=30, kde=True)
        plt.title("Image Brightness Distribution")
        plt.xlabel("Brightness")
        plt.ylabel("Frequency")
        plt.show()
    else:
        print("[INFO] No 'brightness' column found.")

def plot_image_dimensions():
    """Scatter plot of image dimensions (width vs. height)."""
    df = pd.read_csv(METADATA_CSV)
    if 'width' in df.columns and 'height' in df.columns:
        plt.scatter(df['width'], df['height'], alpha=0.5)
        plt.title("Image Dimensions")
        plt.xlabel("Width")
        plt.ylabel("Height")
        plt.grid(True)
        plt.show()
    else:
        print("[INFO] No 'width' or 'height' columns found.")

def plot_contrast_sample(image_path):
    """Display image and its contrast-enhanced version."""
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print(f"Could not read image: {image_path}")
        return
    equalized = cv2.equalizeHist(img)

    plt.figure(figsize=(10, 4))
    plt.subplot(1, 2, 1)
    plt.imshow(img, cmap='gray')
    plt.title("Original")
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(equalized, cmap='gray')
    plt.title("Contrast Enhanced")
    plt.axis('off')
    plt.show()
