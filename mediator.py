
from usecases.UseCase1 import UseCase1
from usecases.UseCase2 import UseCase2
from usecases.UseCase3 import UseCase3
from usecases.UseCase4 import UseCase4
from utils import Config, Voice


class Mediator():

    def __init__(self, voice: Voice, config: Config) -> None:
        self.voice = voice
        self.config = config

        self.use_case_1 = UseCase1(voice=self.voice, config=self.config)
        self.use_case_2 = UseCase2(voice=self.voice, config=self.config)
        self.use_case_3 = UseCase3(voice=self.voice, config=self.config)
        self.use_case_4 = UseCase4(voice=self.voice, config=self.config)

    def check_for_trigger(self):
        while True:
            if self.use_case_1.is_triggered():
                self.use_case_1.run()
            if self.use_case_2.is_triggered():
                self.use_case_2.run()
            if self.use_case_3.is_triggered():
                self.use_case_3.run()
            if self.use_case_4.is_triggered():
                self.use_case_4.run()
