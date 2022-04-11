from abc import abstractmethod


class FirstTaskClass:
    answer = 0

    @property
    def Answer(self):
        return self.answer

    @Answer.setter
    def Answer(self, newAnswer):
        if newAnswer.as_tuple().exponent < -3:
            self.answer = newAnswer
        #else:
            #print("Такой ответ не может использоваться в ЕГЭ")

    def __init__(self):
        print()

    @abstractmethod
    def displayTask():
        print()

    def displayAnswer(self):
        print(self.Answer)