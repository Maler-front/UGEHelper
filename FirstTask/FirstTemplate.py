from FirstTask.FirstTaskClass import FirstTaskClass
import random
from functions import get_count


class FirstTemplate(FirstTaskClass):
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

            self.Answer = (self.a / self.b + self.c / self.d) / (self.e / self.f)

            if get_count(self.Answer) < 3:
                break

    def displayTask(self):
        print(f"({self.a} / {self.b} + {self.c} / {self.d}) / ({self.e} / {self.f})")
