import ThirdTaskClass
import random


class First3Template(ThirdTaskClass):
    def __init__(self):
        self.answer[0] = random.randint(1, 4)
        while True:
            self.answer[1] = random.randint(1, 4)
            if self.answer[0] != self.answer[1]:
                break
        while True:
            self.answer[2] = random.randint(1, 4)
            if self.answer[0] != self.answer[2] and self.answer[1] != self.answer[2]:
                break
        while True:
            self.answer[3] = random.randint(1, 4)
            if self.answer[0] != self.answer[3] and self.answer[1] != self.answer[3] and self.answer[2] != self.answer[3]:
                break
