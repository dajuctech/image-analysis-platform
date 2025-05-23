from google.cloud import storage
import os
from config import PROCESSED_IMAGE_DIR

def upload_to_gcs(bucket_name, folder=PROCESSED_IMAGE_DIR):
    client = storage.Client()
    bucket = client.bucket(bucket_name)

    for root, _, files in os.walk(folder):
        for file in files:
            path = os.path.join(root, file)
            blob = bucket.blob(os.path.relpath(path, folder))
            blob.upload_from_filename(path)
            print(f"✅ Uploaded: {file} to gs://{bucket_name}/{blob.name}")
