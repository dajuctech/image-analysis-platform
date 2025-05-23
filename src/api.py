from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import os
import shutil

from config import RAW_IMAGE_DIR
from data_ingestion import preprocess_images
from logger import get_logger

logger = get_logger(__name__)
app = FastAPI(title="Image Processing API")

@app.post("/upload/")
async def upload_image(file: UploadFile = File(...)):
    """
    Uploads an image to the raw folder and runs preprocessing.
    """
    os.makedirs(RAW_IMAGE_DIR, exist_ok=True)
    file_path = os.path.join(RAW_IMAGE_DIR, file.filename)

    with open(file_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    logger.info(f"Uploaded file: {file.filename}")
    preprocess_images()

    return JSONResponse(content={"message": f"{file.filename} uploaded and processed."})

@app.get("/")
def root():
    return {"message": "Welcome to the Image Processing API"}
