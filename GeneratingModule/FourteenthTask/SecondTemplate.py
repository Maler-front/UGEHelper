from GeneratingModule.BaseTaskClass import BaseTaskClass
import random
from functions import get_count


class SecondTemplate(BaseTaskClass):
    a = b = c = 1

    def __init__(self):
        super().__init__()
        while True:
            self.a = random.randint(1, 100) / 10
            self.b = random.randint(1, 100) / 10
            self.c = random.randint(1, 100) / 10

            self.Answer = str((self.a + self.b) * self.c)

            if get_count(self.Answer) < 3:
                break

    def get_text(self):
        return f"Найдите значение выражения: ({self.a} + {self.b}) * {self.c}"

    def get_image(self):
        return None
