import boto3
import os
from config import PROCESSED_IMAGE_DIR

def upload_folder_to_s3(bucket_name, folder=PROCESSED_IMAGE_DIR):
    s3 = boto3.client('s3')
    for root, _, files in os.walk(folder):
        for file in files:
            path = os.path.join(root, file)
            key = os.path.relpath(path, folder)
            s3.upload_file(path, bucket_name, key)
            print(f"✅ Uploaded: {key} to s3://{bucket_name}/{key}")
