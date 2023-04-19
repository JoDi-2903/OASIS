from abc import ABC, abstractmethod


class UseCaseInterface(ABC):
    @abstractmethod
    def is_triggered(self) -> bool:
        pass

    @abstractmethod
    def run(self) -> None:
        pass
