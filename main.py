from mediator import Mediator

from utils import Voice, Config

import os
import json
import logging
import argparse


def setup(config: Config):
    voice = Voice()
    voice.speak(
        "Hello, I am OASIS, your new personal assistant. Before we can start, you have to answer some questions to me. Now please say your name or your designation as I should address you."
    )
    config.set("name", voice.hear())
    voice.speak(
        f"Alright. I will call you {config.get('name')}."
    )

    # Start mediator
    mediator = Mediator(voice, config)
    mediator.check_for_trigger()


def start(config: Config):
    config.load()
    # Initialise voice module
    voice = Voice()
    voice.speak(f"Welcome back, {config.get('name')}!")

    # Start mediator
    mediator = Mediator(voice, config)
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
    config = Config()
    if config.exists():
        start(config)
    else:
        setup(config)
