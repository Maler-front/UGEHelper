import random
from FirstTask.FirstTaskClass import FirstTaskClass
from functions import get_count


class FirstTemplate(FirstTaskClass):

    all = russian = chinese = japanese = usa = 1
    
    def __init__(self):
        self.Answer = 0.1111
        while get_count(self.Answer) > 2:
            self.all = random.randrange(30, 50, 5)
            self.russian = random.randint(3, 8)
            self.japanese = random.randint(3, 8)
            self.usa = random.randint(3, 8)
            self.chinese = self.all - self.russian - self.japanese - self.usa
            self.Answer = self.russian / self.all

    def displayTask(self):
        print(f"В чемпионате по прыжкам в воду участвуют {self.all} спортсменов: {self.russian} из России, {self.chinese} из Китая, {self.japanese} из Японии и {self.usa} из США. Порядок, в котором выступают спортсмены, определяется жребием. Найдите вероятность того, что спортсмен, выступающий первым, окажется из России. ")
