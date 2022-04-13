import FirstTaskClass
from decimal import Decimal
import random


class SecondTemplate(FirstTaskClass):
    a = b = c = 1

    def __init__(self):
        super().__init__()
        while True:
            self.a = random.randint(1, 100) / random.randint(10)
            self.b = random.randint(1, 100) / random.randint(10)
            self.c = random.randint(1, 100) / random.randint(10)

            self.Answer = Decimal((self.a + self.b) * self.c)

            if self.Answer.as_tuple().exponent > -3:
                break

    def displayTask(self):
        print(f"({self.a} + {self.b}) * {self.c}")
