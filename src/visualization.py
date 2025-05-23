import os
import cv2
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from config import METADATA_CSV

def plot_class_distribution():
    """Plot the distribution of image classes (if label column exists)."""
    df = pd.read_csv(METADATA_CSV)
    if 'label' in df.columns:
        sns.countplot(x='label', data=df)
        plt.title("Class Distribution")
        plt.xlabel("Class Label")
        plt.ylabel("Count")
        plt.show()
    else:
        print("[INFO] No 'label' column found in metadata.")

def show_sample_images(n=5):
    """Display a sample of preprocessed images."""
    df = pd.read_csv(METADATA_CSV)
    sample = df.sample(min(n, len(df)))

    for _, row in sample.iterrows():
        img_path = row['processed_path']
        img = cv2.imread(img_path)
        if img is not None:
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            plt.imshow(img_rgb)
            plt.title(row['filename'])
            plt.axis('off')
            plt.show()

def plot_brightness_distribution():
    """Plot the distribution of average brightness."""
    df = pd.read_csv(METADATA_CSV)
    if 'brightness' in df.columns:
        sns.histplot(df['brightness'], bins=30, kde=True)
        plt.title("Image Brightness Distribution")
        plt.xlabel("Average Brightness")
        plt.ylabel("Frequency")
        plt.show()
    else:
        print("[INFO] No 'brightness' column found in metadata.")

def plot_image_dimensions():
    """Scatter plot of image width vs. height."""
    df = pd.read_csv(METADATA_CSV)
    if 'width' in df.columns and 'height' in df.columns:
        plt.scatter(df['width'], df['height'], alpha=0.5)
        plt.title("Image Dimensions")
        plt.xlabel("Width")
        plt.ylabel("Height")
        plt.grid(True)
        plt.show()
    else:
        print("[INFO] No 'width'/'height' columns found in metadata.")
