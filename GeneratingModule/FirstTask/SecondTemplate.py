import random
from GeneratingModule.BaseTaskClass import BaseTaskClass


class SecondTemplate(BaseTaskClass):
    price = kg = gr = total = ""

    def __init__(self):
        super().__init__()
        while True:
            self.price = random.randint(1, 50)
            self.kg = random.randint(1, 5)
            self.gr = random.randrange(100, 900, 100)
            self.total = random.randrange(100, 500, 100)

            self.Answer = self.total - self.price * (self.kg + self.gr / 1000)

            if self.Answer:
                break

    def get_text(self):
        return f"Килограмм моркови стоит {self.price} рублей Олег купил {self.kg} кг {self.gr} г моркови.\n" \
               f"Сколько рублей сдачи он должен получить с {self.total} рублей?"

    def get_image(self):
        return None
