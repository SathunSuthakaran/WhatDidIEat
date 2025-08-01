from fastapi import FastAPI, File, UploadFile
from ml_models.detect_and_classify import analyze_image
import shutil
from pathlib import Path

app = FastAPI()

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    image_path = UPLOAD_DIR / file.filename
    with image_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = analyze_image(str(image_path))
    return {"detections": result}
