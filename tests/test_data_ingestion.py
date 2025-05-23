from src.data_ingestion import preprocess_images
import os
import pandas as pd
from config import METADATA_CSV, PROCESSED_IMAGE_DIR

def test_preprocess_images():
    preprocess_images()

    # Check metadata CSV exists and is not empty
    assert os.path.exists(METADATA_CSV)
    df = pd.read_csv(METADATA_CSV)
    assert not df.empty
    assert 'brightness' in df.columns

    # Check at least one image is processed
    processed_files = os.listdir(PROCESSED_IMAGE_DIR)
    assert len(processed_files) > 0
