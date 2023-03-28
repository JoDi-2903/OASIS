from usecases.UseCaseInterface import UseCaseInterface
from utils import Config, Voice


class UseCase1(UseCaseInterface):
    def __init__(self, voice: Voice, config: Config):
        self.voice = voice
        self.config = config

    def run(self) -> None:
        pass

    def is_triggered(self) -> bool:
        pass
