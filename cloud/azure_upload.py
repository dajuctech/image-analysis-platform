from azure.storage.blob import BlobServiceClient
import os
from config import PROCESSED_IMAGE_DIR

def upload_to_azure(container_name, conn_str, folder=PROCESSED_IMAGE_DIR):
    blob_service = BlobServiceClient.from_connection_string(conn_str)
    container = blob_service.get_container_client(container_name)

    for root, _, files in os.walk(folder):
        for file in files:
            path = os.path.join(root, file)
            blob_name = os.path.relpath(path, folder)
            with open(path, "rb") as data:
                container.upload_blob(name=blob_name, data=data, overwrite=True)
                print(f"✅ Uploaded: {file} to Azure Blob Storage")
