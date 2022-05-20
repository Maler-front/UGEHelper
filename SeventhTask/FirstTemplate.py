from SeventhTask.SeventhTaskClass import SeventhTaskClass
import random
from functions import degree


class FirstTemplate(SeventhTaskClass):

    a = b = c = d = e = f = 0

    def __init__(self):
        while self.a == self.b and self.e == self.f:
            self.a = random.randint(4, 7)
            self.b = self.a - random.randint(1, 2)
            self.c = self.a * self.b
            self.d = random.randint(5, 20)
            self.e = self.d - random.randint(0, 3)
            self.f = self.d - random.randint(0, 3)
            self.Answer = self.a ** (self.d - self.e) * self.b ** (self.d - self.f)

    def displayTask(self):
        print(f"Найдите значение выражения \n({self.c}" + degree(self.d) + f") / ({self.a}" + degree(self.e) + f" * {self.b}" + degree(self.f) + ")")
