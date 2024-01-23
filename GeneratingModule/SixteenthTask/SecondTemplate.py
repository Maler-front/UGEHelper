from math import sqrt
from fractions import Fraction
from GeneratingModule.BaseTaskClass import BaseTaskClass
import random


class SecondTemplate(BaseTaskClass):

    par_sin = 0
    alpha = beta = -1

    def __init__(self):
        self.alpha = random.randrange(0, 270, 90)
        self.beta = self.alpha + 90
        match random.randint(1, 4):
            case 1:
                self.par_sin = (random.randint(3, 4) / 5)
            case 2:
                self.par_sin = Fraction(random.randrange(8, 15, 7), 17)
            case 3:
                self.par_sin = Fraction(random.randrange(5, 12, 7), 13)
            case 4:
                self.par_sin = (random.randrange(7, 24, 17) / 25)
        if self.alpha >= 180:
            self.par_sin *= -1
        self.Answer = round(sqrt(1 - self.par_sin ** 2), 2)
        if self.alpha == 90 or self.alpha == 180:
            self.Answer *= -1

    def get_text(self):
        return f"Найдите cosa, если sina = {self.par_sin} и {self.alpha} < a < {self.beta}\n" \
               f"Ответ округлите до сотых"

    def get_image(self):
        return None
