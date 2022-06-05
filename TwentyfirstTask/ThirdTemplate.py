import random
from FirstTask.FirstTaskClass import FirstTaskClass


class ThirdTemplate(FirstTaskClass):
    all_flats: int
    first_border: int
    second_border: int
    first_peoples_num: int
    second_peoples_num: int
    max_peoples_in_flat: int

    def __init__(self):
        self.max_peoples_in_flat = random.randint(3, 5)
        self.all_flats = random.randint(10, 30)
        self.second_border = self.first_border = -1
        while self.first_border <= 0 or self.second_border <= 0:
            self.second_border = self.all_flats - random.randint(3, 10)
            self.first_border = self.second_border - random.randint(2, 4)

        k = random.randint(2, self.max_peoples_in_flat - 1)

        self.Answer = (self.first_border - 1) + ((self.second_border - self.first_border + 1) * k) + ((self.all_flats - self.second_border) * self.max_peoples_in_flat)
        self.first_peoples_num = (self.first_border - 1) + ((self.second_border - self.first_border + 1) * k)
        self.second_peoples_num = ((self.second_border - self.first_border + 1) * k) + ((self.all_flats - self.second_border) * self.max_peoples_in_flat)

    def displayTask(self):
        print(f"В доме всего {self.all_flats} квартир с номерами от 1 до {self.all_flats}. \nВ каждой квартире живёт не менее 1 и не более {self.max_peoples_in_flat} человек. \nВ квартирах с 1 по {self.second_border} включительно живёт суммарно {self.first_peoples_num} человек, а в квартирах с {self.first_border} по {self.all_flats} включительно живёт суммарно {self.second_peoples_num} человек. \nСколько всего человек живут в этом доме?")