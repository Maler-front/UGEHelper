from NinthTask.NinthTaskClass import NinthTaskClass
import random
import functions


class FirstTemplate(NinthTaskClass):
    a = b = c = d = 0

    def __init__(self):
        while self.b == 0 or functions.get_count(self.Answer) > 2:
            self.a = random.randint(2, 10)
            self.b = random.randint(2, 10)
            self.c = random.randint(-10, 10)
            self.d = random.randint(1, 4)
            self.Answer = (self.d + self.c) / self.b

    def displayTask(self):
        s = str(self.b) + "n+" + str(self.c)
        print(f"Найдите корень уравнения: {self.a}{functions.degree(s)} = {self.a ** self.d}")

    def displayAnswer(self):
        print(self.Answer)
        