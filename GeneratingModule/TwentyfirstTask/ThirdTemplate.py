import random
from GeneratingModule.BaseTaskClass import BaseTaskClass


class ThirdTemplate(BaseTaskClass):
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

    def get_text(self):
        return f"В доме всего {self.all_flats} квартир с номерами от 1 до {self.all_flats}. " \
               f"В каждой квартире живёт не менее 1 и не более {self.max_peoples_in_flat} человек. " \
               f"В квартирах с 1 по {self.second_border} включительно живёт суммарно {self.first_peoples_num} человек, " \
               f"а в квартирах с {self.first_border} по {self.all_flats} включительно живёт суммарно {self.second_peoples_num} человек. \n" \
               f"Сколько всего человек живут в этом доме?"

    def get_image(self):
        return None
