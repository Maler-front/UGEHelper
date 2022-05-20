from abc import abstractmethod


class SecondTaskClass:
    text = answer = ""

    @property
    def Answer(self):
        return self.answer

    @Answer.setter
    def Answer(self, newAnswer):
        if 2 < newAnswer < 100:
            self.answer = newAnswer

    def __init__(self):
        pass

    def displayTask(self):
        print(self.text)

    def displayAnswer(self):
        print(self.Answer)
