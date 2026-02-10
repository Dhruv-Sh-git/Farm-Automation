# detect.py
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
    
    # Draw bounding boxes on the frame
    detected_animal = None
    for _, row in detections.iterrows():
        label = row['name']
        confidence = row['confidence']
        x1, y1, x2, y2 = int(row['xmin']), int(row['ymin']), int(row['xmax']), int(row['ymax'])
        
        # Draw box and label for all detections
        color = (0, 255, 0) if label in ANIMALS else (255, 0, 0)
        cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
        cv2.putText(frame, f"{label} {confidence:.2f}", (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

        if label in ANIMALS and confidence > 0.5:
            print(f"🐾 Animal Detected: {label} ({confidence:.2f})")
            detected_animal = label
    
    # Save the frame to disk
    import datetime
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"capture_{timestamp}.jpg"
    cv2.imwrite(filename, frame)
    print(f"📸 Image saved as: {filename}")
    
    if not detected_animal:
        print("No animal detected")
    
    return detected_animal