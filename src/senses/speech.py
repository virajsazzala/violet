import os

import pygame
import speech_recognition as sr

from src.consts import LOG_FILE, VOICE_DATA

# setting up speech to text
r = sr.Recognizer()


# setting up text to speech
''' Voices:
    'ja-JP-NanamiNeural'
    'en-AU-NatashaNeural'
    'en-GB-SoniaNeural'
    'en-IN-NeerjaExpressiveNeural'
'''


def say(audio):
    voice = 'en-AU-NatashaNeural'
    command = f'edge-tts --voice "{voice}" --text "{audio}" --write-media "{VOICE_DATA}"'
    os.system(command)

    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(VOICE_DATA)

    try:
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    except Exception as e:
        print(e)
    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()


def listen():
    # listen for audio and convert it to text
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("processing...")

            # NOTE: use recognize_google for faster but less accurate recognition. (set = language="en-US")
            # NOTE: use recognize_whisper for slower but accurate recognition.
            text = r.recognize_whisper(audio)
            print(f"you said: {text.lower()}")

            # write the text to a log file
            with open(LOG_FILE, "a") as f:
                f.write(f"you said: {text}\n")

            return text.lower()
        except Exception as e:
            raise Exception(str(e))


def main():
    pass


if __name__ == "__main__":
    main()
