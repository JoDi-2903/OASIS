from usecases.UseCaseInterface import UseCaseInterface


class UseCase3(UseCaseInterface):
    def __init__(self, voice):
        self.voice = voice

    def run() -> None:
        pass

    def is_triggered() -> bool:
        pass
