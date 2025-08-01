import json
import torch
from ultralytics import YOLO
from pathlib import Path
from PIL import Image

weights_path = Path(__file__).parent / "weights" / "yolov8_food.pt"
model = YOLO(str(weights_path))

with open(Path(__file__).parent / "nutrition_db.json") as f:
    NUTRITION_DB = json.load(f)



def analyze_image(image_path: str):
    results = model.predict(image_path, conf=0.3)
    detections = []

    for r in results:
        for box in r.boxes:
            cls_name = model.names[int(box.cls)]
            nutrition = NUTRITION_DB.get(cls_name, {})
            detections.append({
                "food": cls_name,
                **nutrition
            })
    
    return detections
