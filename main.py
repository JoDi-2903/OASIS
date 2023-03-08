import os
from mediator import Mediator

from utils import Voice


def setup():
    config = {
        "name": "",
    }
    voice = Voice()
    voice.speak(
        "Hello I am OASIS, your new personal assistant. Before we can start, you have to answer some questions to me. This allows me to better adapt to your daily routine."
    )
    voice.speak(
        "Now please say your name or your designation as I should address you."
    )
    config['name'] = voice.hear()
    voice.speak(
        f"Alright. I will call you {config['name']}."
    )

    # TODO Further configuration and save to config.json

    mediator = Mediator(voice)
    mediator.check_for_trigger()


def start():
    voice = Voice()
    voice.speak("Welcome")
    mediator = Mediator(voice)
    mediator.check_for_trigger()


if __name__ == "__main__":

    # Check if configuration file exists
    if os.path.exists('config.json'):
        start()
    else:
        setup()
