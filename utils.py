import os
import pyttsx3
import speech_recognition as sr
import json
import logging
import vlc
import time
import keyboard


class Voice():
    """This class includes all functions for TTS, STT and media playback"""

    def __init__(self) -> None:

        self.array_yes = [
            'yes', 'yeah', 'yep', 'sure', 'ok', 'okay'
        ]

        self.array_no = [
            'no', 'nope'
        ]

        self.engine = pyttsx3.init()
        self.engine.setProperty(
            'voice', 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-GB_HAZEL_11.0'
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
        """Plays a text as a voice

        Parameter
        --
        msg: string
            The text to be spoken
        """
        logging.info(f"Speaking: {msg}")
        self.engine.say(msg)
        self.engine.runAndWait()

    def play(self, url):
        """Plays a media from a given URL

        Parameter
        --
        url: string
            The URL to the media
        """
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
        """Listens over the microphone and tries to recognize the text.

        Returns
        --
        result: string
            The string with the recognized text.
        """
        with self.mic as source:
            audio = self.recognizer.listen(
                source, timeout=5, phrase_time_limit=5)

        result = json.loads(self.recognizer.recognize_vosk(audio))
        logging.info(f"Heard: {result['text']}")
        return result['text']

    def getUserConfirmation(self) -> bool:
        """Detects whether the user confirms or rejects a statement. If the text is not recognised, a new attempt is made to obtain confirmation

        Returns
        --
        confirmation: bool
            True if the user confirms nad False if not
        """
        while True:
            user_input = self.hear()
            if user_input in self.array_yes:
                return True
            elif user_input in self.array_no:
                return False
            else:
                self.speak(
                    "Sorry, either I didn't understand you or you didn't answer the question correctly."
                )


class Config():
    """Configuration class
    """

    def __init__(self) -> None:
        self.config = dict()

    def set(self, key, value) -> None:
        """Set a value to a key

        Parameter
        --
        key: string
            The unique key in the dictionary. If key already exists the old value is overwritten.
        value: any
            The corresponding value for the key.
        """
        self.config[key] = value
        # After a key is updated or set, save the file
        self.save()

    def get(self, key) -> any:
        """Get a value from a key. If key is not set KeyError is returned.

        Parameter
        --
        key: string
            The key

        Returns
        --
        value: any
            The value from the key. 
        """
        return self.config[key]

    def save(self) -> None:
        """Save the current configuration to the file.
        """
        with open('config.json', 'w') as fp:
            json.dump(self.config, fp)

    def load(self) -> dict:
        """Load a configuration from the file and return the loaded configuration.

        Returns
        --
        config: dict
            The loaded configuration.
        """
        with open('config.json', 'r') as fp:
            self.config = json.load(fp)

        return self.config

    def exists(self) -> bool:
        """Check if a configuration file exists

        Returns
        --
        exists: bool
            True if the file exists
        """
        return os.path.exists('config.json')
