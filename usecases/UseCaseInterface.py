from abc import ABC, abstractmethod


class UseCaseInterface(ABC):
    @abstractmethod
    def is_triggered() -> bool:
        pass

    @abstractmethod
    def run() -> None:
        pass
