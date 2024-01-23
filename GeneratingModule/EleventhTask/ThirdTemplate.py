import os.path
import random
from PIL import Image
from GeneratingModule.BaseTaskClass import BaseTaskClass


class ThirdTemplate(BaseTaskClass):
    a: int
    c: int

    def __init__(self):
        match random.randint(1, 4):
            case 1:
                self.a = 13
                self.c = 5
                self.answer = 12
                if random.randint(1,2) == 1:
                    self.c, self.answer = self.answer, self.c
            case 2:
                self.a = 5
                self.c = 4
                self.answer = 3
                if random.randint(1, 2) == 1:
                    self.c, self.answer = self.answer, self.c
            case 3:
                self.a = 25
                self.c = 24
                self.answer = 7
                if random.randint(1, 2) == 1:
                    self.c, self.answer = self.answer, self.c
            case 4:
                self.a = 17
                self.c = 15
                self.answer = 8
                if random.randint(1, 2) == 1:
                    self.c, self.answer = self.answer, self.c
        k = random.randint(1, 3)
        self.a *= k
        self.c *= k
        self.answer *= k

    def get_text(self):
        return f"Известно, что в треугольнике ABC AB=BC={self.a}, AC={self.c * 2}.\n" \
               f"Найдите длину медианы BM."

    def get_image(self):
        return Image.open(os.path.dirname(os.path.abspath(__file__)) + "/Images/Triangle.png")
