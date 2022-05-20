from ThirdTask.ThirdTaskClass import ThirdTaskClass
import random


class First3Template(ThirdTaskClass):
    def __init__(self):
        self.abcd = {
            "A": "Рост ребенка",
            "B": "Толщина бумаги",
            "C": "Протяженность автобусного маршрута",
            "D": "Высота жилого дома"
        }
        variants = [
            str(random.randint(90, 120)) + "см",
            str(random.randint(1, 20) / 100) + "мм",
            str(random.randint(10, 50)) + "км",
            str(random.randint(10, 100)) + "м"
        ]

        for i in range(0, 4):
            while True:
                num = random.randint(0, 3)
                if self.variants[num] == 0:
                    self.variants[num] = variants[i]
                    self.Answer[i] = num
                    break
