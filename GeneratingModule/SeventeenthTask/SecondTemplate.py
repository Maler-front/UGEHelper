import random
import functions
from GeneratingModule.BaseTaskClass import BaseTaskClass


class SecondTemplate(BaseTaskClass):
    a = b = c = d = 1

    def __init__(self):
        coefficient = random.randrange(-1, 1, 2)
        while True:
            self.a = random.randint(2, 5) ** coefficient
            self.b = random.randint(-40, 40)
            self.c = random.randint(-10, 10)
            self.d = random.randint(1, 5) * coefficient

            if self.b != 0 and self.c != 0:
                self.Answer = (self.a ** self.d - self.c) / (self.b / 4)

            if functions.get_count(self.Answer) < 5:
                self.b /= 4
                break

    def get_text(self):
        return f"Найдите корень уравнения: log{functions.downDegree(round(self.a, 5))}({self.b}x+({self.c})) = {self.d}"

    def get_image(self):
        return None
