import os
import cv2
import numpy as np
import pandas as pd
from tqdm import tqdm
import boto3  # Optional: for cloud storage
from botocore.exceptions import NoCredentialsError

from config import RAW_IMAGE_DIR, PROCESSED_IMAGE_DIR, METADATA_CSV, IMAGE_SIZE, CLOUD_BUCKET_NAME
from logger import get_logger

logger = get_logger(__name__)

def download_images_from_s3(bucket_name, local_path=RAW_IMAGE_DIR):
    s3 = boto3.client('s3')
    os.makedirs(local_path, exist_ok=True)

    try:
        for obj in s3.list_objects_v2(Bucket=bucket_name).get('Contents', []):
            filename = obj['Key']
            local_file = os.path.join(local_path, filename)
            s3.download_file(bucket_name, filename, local_file)
            logger.info(f"Downloaded {filename} from S3.")
    except NoCredentialsError:
        logger.error("AWS credentials not found. Skipping cloud download.")

def preprocess_images(input_dir=RAW_IMAGE_DIR, output_dir=PROCESSED_IMAGE_DIR, image_size=IMAGE_SIZE):
    os.makedirs(output_dir, exist_ok=True)
    metadata = []

    logger.info(f"Processing images from {input_dir}")
    for filename in tqdm(os.listdir(input_dir)):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            file_path = os.path.join(input_dir, filename)
            img = cv2.imread(file_path)
            if img is None:
                logger.warning(f"Unable to read {filename}")
                continue

            resized = cv2.resize(img, image_size)
            normalized = resized / 255.0
            brightness = np.mean(normalized)

            processed_path = os.path.join(output_dir, filename)
            cv2.imwrite(processed_path, (normalized * 255).astype(np.uint8))

            metadata.append({
                "filename": filename,
                "original_path": file_path,
                "processed_path": processed_path,
                "width": img.shape[1],
                "height": img.shape[0],
                "brightness": brightness
            })

    pd.DataFrame(metadata).to_csv(METADATA_CSV, index=False)
    logger.info(f"Metadata saved to {METADATA_CSV}")

if __name__ == "__main__":
    download_images_from_s3(CLOUD_BUCKET_NAME)  # Optional
    preprocess_images()
