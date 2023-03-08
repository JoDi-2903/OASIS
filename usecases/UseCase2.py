from usecases.UseCaseInterface import UseCaseInterface


class UseCase2(UseCaseInterface):
    def __init__(self, voice):
        self.voice = voice

    def run(self) -> None:
        pass

    def is_triggered(self) -> bool:
        pass
