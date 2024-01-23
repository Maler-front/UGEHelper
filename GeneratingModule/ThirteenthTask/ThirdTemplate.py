import random
from PIL import Image
import os
from GeneratingModule.BaseTaskClass import BaseTaskClass


class ThirdTemplate(BaseTaskClass):

    r: int
    R: int

    def __init__(self):
        self.r = random.randint(2, 9)
        self.Answer = random.randint(2, 9)
        self.R = self.Answer * self.r
        self.Answer = self.Answer ** 2

    def get_text(self):
        return f"Даны два шара радиусами {self.R} и {self.r}. " \
               f"Во сколько раз площадь поверхности большего шара больше площади поверхности меньшего?"

    def get_image(self):
        return Image.open(os.path.dirname(os.path.abspath(__file__)) + "/Images/Ball.png")

