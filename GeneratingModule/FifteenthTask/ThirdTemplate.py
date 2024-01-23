import random

from GeneratingModule.BaseTaskClass import BaseTaskClass


class ThirdTemplate(BaseTaskClass):
    space: int
    grain: int
    vegetables: int
    text: str

    def __init__(self):
        self.grain = random.randint(2, 7)
        self.vegetables = random.randint(2, 7)

        while self.grain % self.vegetables == 0 or self.vegetables % self.grain == 0:
            self.grain = random.randint(2, 7)
            self.vegetables = random.randint(2, 7)

        self.space = (self.grain + self.vegetables) * random.randint(2, 8)

        match random.randint(1, 2):
            case 1:
                self.text = "зерновые"
                self.Answer = self.space * self.grain / (self.grain + self.vegetables)
            case 2:
                self.text = "овощные"
                self.Answer = self.space * self.vegetables / (self.grain + self.vegetables)

    def get_text(self):
        return f"Площадь земель фермерского хозяйства, отведённых под посадку сельскохозяйственных культур, составляет {self.space} гектара и распределена между зерновыми и овощными культурами в отношении {self.grain}:{self.vegetables} соответственно. \n" \
               f"Сколько гектаров занимают {self.text} культуры?"

    def get_image(self):
        return None
