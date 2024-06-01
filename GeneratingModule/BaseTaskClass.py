from abc import abstractmethod


class BaseTaskClass:
    answer: float

    @property
    def Answer(self):
        return self.answer

    @Answer.setter
    def Answer(self, newAnswer):
        self.answer = newAnswer

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_text(self):
        pass

    @abstractmethod
    def get_image(self):
        pass

    def get_answer(self):
        return self.Answer
