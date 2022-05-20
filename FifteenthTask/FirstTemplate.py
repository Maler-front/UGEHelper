import random
from FirstTask.FirstTaskClass import FirstTaskClass
from PIL import Image
import os

class FirstTemplate(FirstTaskClass):

    ab: int
    ac: int

    def __init__(self):
        coefficient = random.randint(1, 4)
        match random.randint(1, 4):
            case 1:
                self.ab = 5 * coefficient
                self.Answer = 3 * coefficient or 4 * coefficient
                if self.Answer == 4 * coefficient:
                    self.ac = 3 * 2 * coefficient
                else:
                    self.ac = 4 * 2 * coefficient
            case 2:
                self.ab = 13 * coefficient
                self.Answer = 5 * coefficient or 12 * coefficient
                if self.Answer == 12 * coefficient:
                    self.ac = 5 * 2 * coefficient
                else:
                    self.ac = 12 * 2 * coefficient
            case 3:
                self.ab = 17 * coefficient
                self.Answer = 8 * coefficient or 15 * coefficient
                if self.Answer == 15 * coefficient:
                    self.ac = 8 * 2 * coefficient
                else:
                    self.ac = 15 * 2 * coefficient
            case 4:
                self.ab = 25 * coefficient
                self.Answer = 7 * coefficient or 24 * coefficient
                if self.Answer == 24 * coefficient:
                    self.ac = 7 * 2 * coefficient
                else:
                    self.ac = 24 * 2 * coefficient

    def displayTask(self):
        image = Image.open(os.path.dirname(os.path.abspath(__file__)) + "/img.png")
        image.show()
        print(f"Известно, что в треугольнике ABC AB = BC = {self.ab}, AC = {self.ac} . Найдите длину медианы BM .")
