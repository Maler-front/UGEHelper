import random
from GeneratingModule.BaseTaskClass import BaseTaskClass
from PIL import Image
import os


class SecondTemplate(BaseTaskClass):
    a: int
    l: int

    def __init__(self):
        match random.randint(1, 2):
            case 1:
                self.a = random.randint(1, 5) * 3
                h = random.randint(2, 10)
            case 2:
                self.a = random.randint(2, 10)
                h = random.randint(1, 5) * 3

        self.l = h ** 2 + (self.a ** 2) / 2
        self.Answer = (1 / 3) * (self.a ** 2) * h

    def get_text(self):
        return f"Найдите объём правильной четырёхугольной пирамиды, сторона основания которой равна {self.a}, а боковое ребро равно " + u"\u221a" + f"{self.l}"

    def get_image(self):
        return Image.open(os.path.dirname(os.path.abspath(__file__)) + "/Images/Pyramid.png")
