import time
import cv2
from distance import get_distance
from detect import detect_animal
from sound import play_sound

print("System started. Waiting for object within 2 meters...")

while True:
    dist = get_distance()
    print(f"Distance: {dist} m")

    if dist <= 2.0:
        print("Object detected. Activating camera...")
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        cap.release()

        if ret:
            animal = detect_animal(frame)

            if animal:
                print(f"{animal.upper()} detected. Playing sound...")
                play_sound(animal)
            else:
                print("No target animal detected")

        time.sleep(1)

        # Re-check distance
        if get_distance() > 2.0:
            print("Object left. Returning to idle state")

    time.sleep(0.5)

