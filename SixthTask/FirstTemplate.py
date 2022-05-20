import random

from FirstTask.FirstTaskClass import FirstTaskClass


class FirstTemplate(FirstTaskClass):
    salary: int

    def __init__(self):
        self.salary = random.randint(15, 50) * 1000
        self.Answer = self.salary * 0.87

    def displayTask(self):
        print(f"Ивану Кузьмичу начислена заработная плата {self.salary} рублей. Из этой суммы вычитается налог на доходы физических лиц в размере 13%. \nСколько рублей Иван Кузьмич получит после уплаты этого налога? ")
