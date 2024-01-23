import random

from GeneratingModule.BaseTaskClass import BaseTaskClass


class FirstTemplate(BaseTaskClass):
    salary: int

    def __init__(self):
        self.salary = random.randint(15, 50) * 1000
        self.Answer = self.salary * 0.87

    def get_text(self):
        return f"Ивану Кузьмичу начислена заработная плата {self.salary} рублей. Из этой суммы вычитается налог на доходы физических лиц в размере 13%. \n" \
               f"Сколько рублей Иван Кузьмич получит после уплаты этого налога? "

    def get_image(self):
        return None
