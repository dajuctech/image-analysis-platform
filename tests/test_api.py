from fastapi.testclient import TestClient
from src.api import app
import os

client = TestClient(app)

def test_upload_endpoint():
    test_image_path = "data/raw/sample.jpg"

    # Make sure test image exists
    if not os.path.exists(test_image_path):
        with open(test_image_path, "wb") as f:
            f.write(os.urandom(1024))  # Write random bytes

    with open(test_image_path, "rb") as f:
        response = client.post("/upload/", files={"file": ("sample.jpg", f, "image/jpeg")})

    assert response.status_code == 200
    assert "uploaded and processed" in response.json()["message"]
