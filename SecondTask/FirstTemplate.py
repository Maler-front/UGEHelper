from SecondTask.SecondTaskClass import SecondTaskClass
import random


class First2Template(SecondTaskClass):
    rub = cop = total = ""

    def __init__(self):
        while True:
            self.rub = random.randint(1, 20)
            self.cop = random.randrange(1, 90, 10)
            self.total = random.randrange(100, 500, 10)

            self.Answer = self.total // (self.rub + self.cop / 100)

            if self.Answer:
                break;

        self.text = f"Баночка йогурта стоит {self.rub} рублей {self.cop} копеек. Какое наибольшее количество баночек йогурта можно купить на {self.total} рублей? "