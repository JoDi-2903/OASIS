import os
from mediator import Mediator

from utils import Voice

import json

config = {
    "name": "",
}


def setup():
    voice = Voice()
    voice.speak(
        "Hello I am OASIS, your new personal assistant. Before we can start, you have to answer some questions to me. Now please say your name or your designation as I should address you."
    )
    config['name'] = voice.hear()
    voice.speak(
        f"Alright. I will call you {config['name']}."
    )

    # TODO Further configuration and save to config.json
    with open('config.json', 'w') as fp:
        json.dump(config, fp)

    mediator = Mediator(voice)
    mediator.check_for_trigger()


def start():
    with open('config.json', 'r') as fp:
        config = json.load(fp)
    voice = Voice()
    voice.speak(f"Welcome back, {config['name']}")
    mediator = Mediator(voice)
    mediator.check_for_trigger()


if __name__ == "__main__":

    # Check if configuration file exists
    if os.path.exists('config.json'):
        start()
    else:
        setup()
