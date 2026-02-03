# sound.py
import pygame
import os

# Initialize pygame mixer
pygame.mixer.init()

SOUND_FILES = {
    "cow": "sounds/cow.mp3",
    "elephant": "sounds/elephant.mp3",
    "pig": "sounds/pig.mp3"
}

def play_animal_sound(animal_name, repeat=5):
    """Play the corresponding animal sound alert"""
    if animal_name not in SOUND_FILES:
        print(f"⚠️ No sound file for {animal_name}")
        return
    
    sound_path = SOUND_FILES[animal_name]
    
    if not os.path.exists(sound_path):
        print(f"⚠️ Sound file not found: {sound_path}")
        return
    
    print(f"🔊 Playing {animal_name} alert sound {repeat} times...")
    
    try:
        sound = pygame.mixer.Sound(sound_path)
        for i in range(repeat):
            print(f"  Playing sound {i+1}/{repeat}")
            sound.play()
            # Wait for sound to finish playing
            while pygame.mixer.get_busy():
                pygame.time.wait(100)
    except Exception as e:
        print(f"❌ Error playing sound: {e}")
