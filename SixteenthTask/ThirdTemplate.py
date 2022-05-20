import random
from PIL import Image
import os
from FirstTask.FirstTaskClass import FirstTaskClass


class ThirdTemplate(FirstTaskClass):

    r: int
    R: int

    def __init__(self):
        self.r = random.randint(2, 9)
        self.Answer = random.randint(2, 9)
        self.R = self.Answer * self.r
        self.Answer = self.Answer ** 2

    def displayTask(self):
        image = Image.open(os.path.dirname(os.path.abspath(__file__)) + "/Images/Ball.png")
        image.show()
        print(f"Даны два шара радиусами {self.R} и {self.r}. Во сколько раз площадь поверхности большего шара больше площади поверхности меньшего? ")

