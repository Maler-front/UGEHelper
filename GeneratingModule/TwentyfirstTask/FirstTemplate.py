import random

from GeneratingModule.BaseTaskClass import BaseTaskClass


class FirstTemplate(BaseTaskClass):
    k: int
    all_cookies: int

    def __init__(self):
        self.k = random.randint(2, 6)
        cookies_coefficient = random.randint(2, 20)
        self.all_cookies = (self.k ** 2 + 1) * cookies_coefficient
        self.Answer = (self.k ** 2) * cookies_coefficient

    def get_text(self):
        return f"Маша и Медведь съели {self.all_cookies} печений и банку варенья, начав и закончив одновременно. " \
               f"Сначала Маша ела варенье, а Медведь — печенье, но в какой-то момент они поменялись. " \
               f"Медведь и то и другое ест в {self.k} раза быстрее Маши. \n" \
               f"Сколько печений съел Медведь, если варенья они съели поровну?"

    def get_image(self):
        return None
