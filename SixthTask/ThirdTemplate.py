import random

from FirstTask.FirstTaskClass import FirstTaskClass


class ThirdTemplate(FirstTaskClass):
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

    def displayTask(self):
        print(f"Площадь земель фермерского хозяйства, отведённых под посадку сельскохозяйственных культур, составляет {self.space} гектара и распределена между зерновыми\nи овощными культурами в отношении {self.grain}:{self.vegetables} соответственно. Сколько гектаров занимают {self.text} культуры? ")