import random

import matplotlib.pyplot as plt
from FourthTask.FourthTaskClass import FourthTaskClass


class FirstTemplate(FourthTaskClass):
    def __init__(self):
        self.rives = {
            "Амур": 0,
            "Вилюй": 0,
            "Волга": 0,
            "Енисей": 0,
            "Иртыш": 0,
            "Лена": 0,
            "Нижняя Тунгусска": 0,
            "Обь": 0
        }
        self.Answer = 1
        for key in self.rives.keys():
            self.rives[key] = random.randint(100, 500) / 100
            if self.rives[key] > self.rives["Амур"]:
                self.Answer += 1

    def displayTask(self):
        print("На диаграмме приведены данные о длине восьми крупнейших рек России (в тысячах километров). Первое место по длине занимает река Лена\nНа каком месте по длине находится река Амур?")
        plt.bar(self.rives.keys(), self.rives.values())
        plt.show()
