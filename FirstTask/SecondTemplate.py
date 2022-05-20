from FirstTask.FirstTaskClass import FirstTaskClass
from decimal import Decimal
import random
from functions import get_count


class SecondTemplate(FirstTaskClass):
    a = b = c = 1

    def __init__(self):
        super().__init__()
        while True:
            self.a = random.randint(1, 100) / 10
            self.b = random.randint(1, 100) / 10
            self.c = random.randint(1, 100) / 10

            self.Answer = (self.a + self.b) * self.c

            if get_count(self.Answer) < 3:
                break

    def displayTask(self):
        print(f"({self.a} + {self.b}) * {self.c}")
