import random
import functions
from GeneratingModule.BaseTaskClass import BaseTaskClass


class FirstTemplate(BaseTaskClass):
    a = b = c = d = 0

    def __init__(self):
        while self.b == 0 or functions.get_count(self.Answer) > 2:
            self.a = random.randint(2, 10)
            self.b = random.randint(2, 10)
            self.c = random.randint(1, 10) * (1 if random.randint(0, 1) == 0 else -1)
            self.d = random.randint(1, 4)
            self.Answer = (self.d - self.c) / self.b

    def get_text(self):
        if self.c > 0:
            s = str(self.b) + "n+" + str(self.c)
        else:
            s = str(self.b) + "n" + str(self.c)
        return f"Найдите корень уравнения: {self.a}{functions.degree(s)} = {self.a ** self.d}"

    def get_image(self):
        return None

        