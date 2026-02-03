# main.py
import time
from distance import get_distance_cm, cleanup
from detect import detect_animal
from sound import play_animal_sound

DISTANCE_THRESHOLD_CM = 100  # 1 metre

try:
    while True:
        dist = get_distance_cm()

        if dist is None:
            continue

        print(f"Distance: {dist} cm")

        if dist < DISTANCE_THRESHOLD_CM:
            print("🚨 Object within 1 meter!")
            animal = detect_animal()
            if animal:
                play_animal_sound(animal)
            time.sleep(3)  # avoid continuous triggering

        time.sleep(0.5)

except KeyboardInterrupt:
    print("Stopping system...")
    cleanup()
