import pyttsx3
import speech_recognition as sr
import json
import logging
import vlc
import time
import keyboard


class Voice():

    def __init__(self) -> None:
        self.engine = pyttsx3.init()
        self.engine.setProperty(
            'voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0'
        )

        self.recognizer = sr.Recognizer()
        self.mic = sr.Microphone()

        with self.mic as source:
            self.speak(
                "First I need to calibrate your microphone. So please be quiet for the next 3 seconds."
            )
            # listen for 5 seconds and create the ambient noise energy level
            self.recognizer.adjust_for_ambient_noise(source, duration=3)
            self.recognizer.dynamic_energy_threshold = True

    def speak(self, msg):
        logging.info(f"Speaking: {msg}")
        self.engine.say(msg)
        self.engine.runAndWait()

    def play(self, url):
        logging.info(f"Playing: {url}")

        player = vlc.MediaPlayer()
        player.set_media(vlc.Media(url))
        player.play()
        time.sleep(0.5)
        while player.is_playing():
            if keyboard.read_key() == "enter":
                break
            time.sleep(1)

        player.stop()

    def hear(self) -> str:
        with self.mic as source:
            audio = self.recognizer.listen(
                source, timeout=5, phrase_time_limit=5)

        result = json.loads(self.recognizer.recognize_vosk(audio))
        logging.info(f"Heard: {result['text']}")
        return result['text']
