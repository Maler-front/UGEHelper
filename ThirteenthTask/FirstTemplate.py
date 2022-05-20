import os.path
import random
from PIL import Image
from FirstTask.FirstTaskClass import FirstTaskClass
from functions import get_count


class FirstTemplate(FirstTaskClass):
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
                while get_count(self.h) > 3:
                    self.Answer = random.randint(2, 15)
                    self.h = self.Answer * (1 / (self.k ** 2))

    def displayTask(self):
        image = Image.open(os.path.dirname(os.path.abspath(__file__)) + "/Images/Cylinder.png")
        image.show()
        print(f"Вода в сосуде цилиндрической формы находится на уровне h = {self.h} см. \nНа каком уровне окажется вода, если её перелить в другой цилиндрический сосуд, у которого радиус основания в {self.k} раза {self.text}, чем у данного?\nОтвет дайте в сантиметрах.")