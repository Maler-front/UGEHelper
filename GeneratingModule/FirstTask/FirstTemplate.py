import random
from GeneratingModule.BaseTaskClass import BaseTaskClass


class FirstTemplate(BaseTaskClass):
    rub = cop = total = ""

    def __init__(self):

        self.rub = random.randint(1, 20)
        self.cop = random.randrange(1, 90, 10)
        self.total = random.randrange(100, 500, 10)

        self.Answer = self.total // (self.rub + self.cop / 100)

    def get_text(self):
        return f"Баночка йогурта стоит {self.rub} рублей {self.cop} копеек.\n" \
               f"Какое наибольшее количество баночек йогурта можно купить на {self.total} рублей?"

    def get_image(self):
        return None
