# main.py
import time
from distance import get_distance_cm, cleanup
from animal_detector import detect_animal

DISTANCE_THRESHOLD_CM = 100  # 1 metre

try:
    while True:
        dist = get_distance_cm()

        if dist is None:
            continue

        print(f"Distance: {dist} cm")

        if dist < DISTANCE_THRESHOLD_CM:
            print("🚨 Object within 1 meter!")
            detect_animal()
            time.sleep(3)  # avoid continuous triggering

        time.sleep(0.5)

except KeyboardInterrupt:
    print("Stopping system...")
    cleanup()
