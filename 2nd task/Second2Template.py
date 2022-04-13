import SecondTaskClass
import random
from decimal import Decimal


class Second2Template(SecondTaskClass):
    price = kg = gr = total = ""

    def __init__(self):
        while True:
            self.price = random.randint(1, 50)
            self.kg = random.randint(1, 5)
            self.gr = random.randrange(100, 900, 100)
            self.total = random.randrange(100, 500, 100)

            self.Answer = self.total - self.price * (self.kg + self.gr / 1000)

            if self.Answer:
                break

        self.text = f"Килограмм моркови стоит {self.price} рублей Олег купил {self.kg} кг {self.gr} г моркови. Сколько рублей сдачи он должен получить с {self.total} рублей?"