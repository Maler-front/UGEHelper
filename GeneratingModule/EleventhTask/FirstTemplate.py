import os.path
import random
from PIL import Image
from GeneratingModule.BaseTaskClass import BaseTaskClass
from functions import get_count


class FirstTemplate(BaseTaskClass):
    h: int
    k: int
    text: str

    def __init__(self):
        self.k = random.randint(2, 5)
        match random.randint(1, 2):
            case 1:
                self.text = "больше"
                self.Answer = random.randint(2, 15)
                self.h = self.Answer * (self.k ** 2)
            case 2:
                self.text = "меньше"
                self.Answer = random.randint(2, 15)
                self.h = self.Answer * (1 / (self.k ** 2))
                while get_count(self.h) > 3:
                    self.Answer = random.randint(2, 15)
                    self.h = self.Answer * (1 / (self.k ** 2))

    def get_text(self):
        return f"Вода в сосуде цилиндрической формы находится на уровне h = {self.h} см.\n" \
               f"На каком уровне окажется вода, если её перелить в другой цилиндрический сосуд, у которого радиус основания в {self.k} раза {self.text}, чем у данного?\n" \
               f"Ответ дайте в сантиметрах."

    def get_image(self):
        return Image.open(os.path.dirname(os.path.abspath(__file__)) + "/Images/Cylinder.png")
