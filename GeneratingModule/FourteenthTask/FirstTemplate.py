from GeneratingModule.BaseTaskClass import BaseTaskClass
import random
from functions import get_count


class FirstTemplate(BaseTaskClass):
    a = b = c = d = e = f = 1

    def __init__(self):
        super().__init__()
        while True:
            self.a = random.randint(-15, 15)
            self.b = random.randint(1, 50)
            self.c = random.randint(-15, 15)
            self.d = random.randint(1, 50)
            self.e = random.randint(1, 15)
            self.f = random.randint(1, 50)

            self.Answer = str((self.a / self.b + self.c / self.d) / (self.e / self.f))

            if get_count(self.Answer) < 3:
                break

    def get_text(self):
        return f"Найдите значение выражения: ({self.a} / {self.b} + {self.c} / {self.d}) / ({self.e} / {self.f})"

    def get_image(self):
        return None