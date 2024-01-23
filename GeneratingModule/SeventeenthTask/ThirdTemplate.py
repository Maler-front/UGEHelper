import random
import functions
from GeneratingModule.BaseTaskClass import BaseTaskClass


class ThirdTemplate(BaseTaskClass):
    a = b = c = d = 1
    type = -1
    text = ""

    def __init__(self):
        while True:
            self.b = random.randint(-10, 10)
            self.c = random.randint(-100, 100)
            d = random.randint(1, 20)
            if self.b == 0 & self.c == 0:
                continue
            self.c /= 10
            self.a = ((self.b ** 2 - d ** 2) / (4 * self.c))

            a = functions.get_count(self.a)
            if self.a != 0 and functions.get_count(self.a) < 3:
                self.type = random.randint(0, 1)
                if self.type == 0:
                    self.Answer = (-self.b + d) / 2
                    self.text = "Если уравнение имеет более одного корня, в ответе укажите больший из них"
                else:
                    self.Answer = (-self.b - d) / 2
                    self.text = "Если уравнение имеет более одного корня, в ответе укажите меньший из них"
                break

    def get_text(self):
        return f"Найдите корень уравнения: {self.a}x{functions.degree(2)} + {self.b}x + {self.c} = 0\n" + self.text

    def get_image(self):
        return None
