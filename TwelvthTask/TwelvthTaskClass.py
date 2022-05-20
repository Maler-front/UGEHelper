from abc import abstractmethod


class TwelvthTaskClass:
    answer = []

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
