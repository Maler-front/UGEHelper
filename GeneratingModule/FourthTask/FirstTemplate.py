import random
from GeneratingModule.BaseTaskClass import BaseTaskClass
from functions import degree


class FirstTemplate(BaseTaskClass):
    I = R = 0

    def __init__(self):
        self.I = random.randint(2, 10)
        self.R = random.randint(4, 25)
        self.Answer = (self.I ** 2) * self.R

    def get_text(self):
        return "Мощность постоянного тока (в ваттах) вычисляется по формуле P = I" + degree(2) + f"R , где I — сила тока (в амперах), R — сопротивление (в омах). Пользуясь этой формулой, найдите P (в ваттах), если R = {self.R} Ом и I = {self.I} А."

    def get_image(self):
        return None
