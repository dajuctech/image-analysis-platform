import pytest
import os
import pandas as pd
from src import visualization
from config import METADATA_CSV, PROCESSED_IMAGE_DIR

# Sample test data setup
@pytest.fixture(scope="module", autouse=True)
def setup_sample_metadata():
    # Create dummy metadata file if not exists
    if not os.path.exists(METADATA_CSV):
        sample_data = {
            "filename": ["img1.jpg", "img2.jpg"],
            "processed_path": [f"{PROCESSED_IMAGE_DIR}/img1.jpg", f"{PROCESSED_IMAGE_DIR}/img2.jpg"],
            "brightness": [0.6, 0.7],
            "width": [128, 128],
            "height": [128, 128],
            "label": ["cat", "dog"],
            "predicted_class": ["cat", "dog"]
        }
        df = pd.DataFrame(sample_data)
        os.makedirs(PROCESSED_IMAGE_DIR, exist_ok=True)
        df.to_csv(METADATA_CSV, index=False)
    yield
    if os.path.exists(METADATA_CSV):
        os.remove(METADATA_CSV)

def test_plot_class_distribution():
    try:
        visualization.plot_class_distribution()
    except Exception as e:
        pytest.fail(f"plot_class_distribution failed: {e}")

def test_show_sample_images():
    try:
        visualization.show_sample_images(n=1)
    except Exception as e:
        pytest.fail(f"show_sample_images failed: {e}")

def test_plot_brightness_distribution():
    try:
        visualization.plot_brightness_distribution()
    except Exception as e:
        pytest.fail(f"plot_brightness_distribution failed: {e}")

def test_plot_image_dimensions():
    try:
        visualization.plot_image_dimensions()
    except Exception as e:
        pytest.fail(f"plot_image_dimensions failed: {e}")
