# animal_detector.py
import torch
import cv2

# Load YOLOv5 model (pretrained on COCO)
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

ANIMALS = ["cow", "elephant", "pig"]

def detect_animal():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("❌ Webcam not accessible")
        return None

    ret, frame = cap.read()
    cap.release()

    if not ret:
        print("❌ Failed to capture frame")
        return None

    results = model(frame)
    detections = results.pandas().xyxy[0]

    for _, row in detections.iterrows():
        label = row['name']
        confidence = row['confidence']

        if label in ANIMALS and confidence > 0.5:
            print(f"🐾 Animal Detected: {label} ({confidence:.2f})")
            return label

    print("No animal detected")
    return None
