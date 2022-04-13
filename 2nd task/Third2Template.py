import SecondTaskClass
import random
from decimal import Decimal


class Third2Template(SecondTaskClass):
    volume = total = ""

    def __init__(self):
        while True:
            self.total = random.randint(20, 100)
            self.volume = random.randint(1, 10)

            if self.total % self.volume != 0:
                self.Answer = self.total / self.volume + 1

            if self.Answer:
                break

        self.text = f"Для ремонта требуется {self.total} рулона обоев. Какое наименьшее количество пачек обойного клея нужно для такого ремонта, если 1 пачка клея рассчитана на {self.volume} рулонов?"