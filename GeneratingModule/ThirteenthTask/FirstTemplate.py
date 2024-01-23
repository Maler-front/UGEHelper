import random
import os
from PIL import Image
from GeneratingModule.BaseTaskClass import BaseTaskClass


class FirstTemplate(BaseTaskClass):
    l: int
    r: int
    p: int

    def __init__(self):
        self.l = random.randint(5, 20)
        match random.randint(1, 4):
            case 1:
                self.r = 5
                self.p = 3 or 4
                if self.p == 4:
                    a = 3
                else:
                    a = 4
            case 2:
                self.r = 13
                self.p = 5 or 12
                if self.p == 12:
                    a = 5
                else:
                    a = 12
            case 3:
                self.r = 17
                self.p = 8 or 15
                if self.p == 15:
                    a = 8
                else:
                    a = 15
            case 4:
                self.r = 25
                self.p = 7 or 24
                if self.p == 24:
                    a = 7
                else:
                    a = 24

        self.Answer = a * 2 * self.l

    def get_text(self):
        return f"Радиус основания цилиндра равен {self.r}, а его образующая равна {self.l}. " \
               f"Сечение, параллельное оси цилиндра, удалено от неё на расстояние, равное {self.p}. \n" \
               f"Найдите площадь этого сечения."

    def get_image(self):
        return Image.open(os.path.dirname(os.path.abspath(__file__)) + "/Images/Cylinder.png")