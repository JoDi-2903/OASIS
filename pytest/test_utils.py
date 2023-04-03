from utils import Config, Voice
from pyttsx3 import Engine
from speech_recognition import Recognizer
import os
import pytest


def test_config_set():
    config = Config()
    config.set("test", "lorem ipsum")
    assert config.config['test'] == "lorem ipsum"
    config.set("test", "update")
    assert config.config["test"] == "update"
    assert os.path.exists("config.json")
    # Clean-Up
    os.remove("config.json")


def test_config_get():
    config = Config()
    config.set("test", "test")
    assert config.get("test") == "test"
    with pytest.raises(KeyError):
        config.get("key_does_not_exist")
    # Clean-Up
    os.remove("config.json")


def test_config_save():
    config = Config()
    config.save()
    assert os.path.exists("config.json")
    os.remove("config.json")
    config.set("test", "test")
    assert os.path.exists("config.json")


def test_config_load():
    config = Config()
    config.set("test", "test")
    assert os.path.exists("config.json")
    loaded_config = config.load()
    assert loaded_config['test'] == "test"
    assert config.config['test'] == "test"
    # Clean-Up
    os.remove("config.json")


def test_config_extist():
    config = Config()
    assert config.exists() == False
    config.set("test", "test")
    assert os.path.exists("config.json")
    assert config.exists()
    # Clean-Up
    os.remove("config.json")


def test_voice_init():
    voice = Voice()
    assert len(voice.array_yes) > 0
    assert len(voice.array_no) > 0
    assert type(voice.engine) == Engine
    assert type(voice.recognizer) == Recognizer
