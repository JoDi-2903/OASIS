from mediator import Mediator

from utils import Voice

import os
import json
import logging
import argparse

config = {
    "name": "",
}


def setup():
    voice = Voice()
    voice.speak(
        "Hello, I am OASIS, your new personal assistant. Before we can start, you have to answer some questions to me. Now please say your name or your designation as I should address you."
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
    voice.speak(f"Welcome back, {config['name']}!")

    mediator = Mediator(voice)
    mediator.check_for_trigger()


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        prog="OASIS - Online Assistant for Support, Information and Services"
    )

    parser.add_argument(
        '-v',
        '--verbose',
        dest='verbose',
        help='Logging the spoken and heard text',
        action='store_true'
    )

    args = parser.parse_args()

    if args.verbose:
        logging.basicConfig(encoding='utf-8', level=logging.INFO)

    # Check if configuration file exists
    if os.path.exists('config.json'):
        start()
    else:
        setup()
