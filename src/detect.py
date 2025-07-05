from ultralytics import YOLO
import cv2

model = YOLO('models/best.pt')

def detect_players(frame):
    results = model.predict(source=frame, save=False, conf=0.4)
    boxes = []
    for r in results:
        for box in r.boxes.data:
            x1, y1, x2, y2, conf, cls = box
            boxes.append((int(x1), int(y1), int(x2), int(y2), int(cls)))
    return boxes
