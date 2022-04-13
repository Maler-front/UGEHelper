import FirstTaskClass
import random
from decimal import Decimal


class FirstTemplate(FirstTaskClass):
    a = b = c = d = e = f = 1

    def __init__(self):
        super().__init__()
        while True:
            self.a = random.randint(-15, 15)
            self.b = random.randint(1, 50)
            self.c = random.randint(-15, 15)
            self.d = random.randint(1, 50)
            self.e = random.randint(-15, 15)
            self.f = random.randint(1, 50)

            self.Answer = Decimal((self.a / self.b + self.c / self.d) / (self.e / self.f))

            if self.Answer.as_tuple().exponent > -3:
                break

    def displayTask(self):
        print(f"({self.a} / {self.b} + {self.c} / {self.d}) / ({self.e} / {self.f})")