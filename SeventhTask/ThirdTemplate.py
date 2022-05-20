from SeventhTask.SeventhTaskClass import SeventhTaskClass
import random
from functions import get_count, downDegree


class ThirdTemplate(SeventhTaskClass):

    a = b = c = 0

    def __init__(self):
        self.a = random.randint(2, 7)
        self.b = random.randint(2, 4)
        self.c = random.randint(2, 10)
        self.k = 0
        while self.c == self.a or get_count(self.b / self.c) > 3:
            self.c = random.randint(2, 10)
            self.k += 1
        self.Answer = self.b

    def displayTask(self):
        print("Найдите значение выражения: log" + downDegree(self.a) + f"({(self.a ** self.b) / self.c}) + log" + downDegree(self.a) + f"({self.c})")
