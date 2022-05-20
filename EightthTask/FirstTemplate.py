import random
from FirstTask.FirstTaskClass import FirstTaskClass
from functions import degree


class FirstTemplate(FirstTaskClass):
    I = R = 0

    def __init__(self):
        self.I = random.randint(2, 10)
        self.R = random.randint(4, 25)
        self.Answer = (self.I ** 2) * self.R

    def displayTask(self):
        print("Мощность постоянного тока (в ваттах) вычисляется по формуле P = I" + degree(2) + f"R , где I — сила тока (в амперах), R — сопротивление (в омах). Пользуясь этой формулой, найдите P (в ваттах), если R = {self.R} Ом и I = {self.I} А.")
