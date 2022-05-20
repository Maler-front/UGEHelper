from ThirdTask.ThirdTaskClass import ThirdTaskClass
import random


class Second3Template(ThirdTaskClass):
    def __init__(self):
        self.abcd = {
            "A": "Масса взрослого человека",
            "B": "Масса грузового автомобиля",
            "C": "Масса книги",
            "D": "Масса пуговицы"
        }
        variants = [
            str(random.randint(50, 100)) + "кг",
            str(random.randint(5, 10)) + "т",
            str(random.randint(150, 500)) + "г",
            str(random.randint(2, 10)) + "г"
        ]

        for i in range(0, 4):
            while True:
                num = random.randint(0, 3)
                if self.variants[num] == 0:
                    self.variants[num] = variants[i]
                    self.Answer[i] = num
                    break
