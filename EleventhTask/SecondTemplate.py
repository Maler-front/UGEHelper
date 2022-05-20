import random
from FirstTask.FirstTaskClass import FirstTaskClass
from functions import get_count


class SecondTemplate(FirstTaskClass):
    all = broken = 1
    type_text = ""

    def __init__(self):
        self.Answer = 0.111
        while get_count(self.Answer) > 2:
            self.all = random.randint(1, 2) * 50
            self.broken = random.randint(2, 10)
            type = random.randint(1, 2)
            if type == 1:
                self.type_text = "неисправной"
                self.Answer = self.broken / self.all
            else:
                self.type_text = "исправной"
                self.Answer = 1 - self.broken / self.all


    def displayTask(self):
        print(f"Из каждых {self.all} лампочек, поступающих в продажу, в среднем {self.broken} неисправных. Какова вероятность того, что случайно выбранная в магазине лампочка окажется {self.type_text}?")
