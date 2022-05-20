from abc import abstractmethod


class NinthTaskClass:
    answer = 0

    @property
    def Answer(self):
        return self.answer

    @Answer.setter
    def Answer(self, newAnswer):
        self.answer = newAnswer

    def __init__(self):
        pass

    @abstractmethod
    def displayTask(self):
        pass

    def displayAnswer(self):
        print(self.Answer)
