import random

from FirstTask.FirstTaskClass import FirstTaskClass


class FirstTemplate(FirstTaskClass):
    k: int
    all_cookies: int

    def __init__(self):
        self.k = random.randint(2, 6)
        cookies_coefficient = random.randint(2, 20)
        self.all_cookies = (self.k ** 2 + 1) * cookies_coefficient
        self.Answer = (self.k ** 2) * cookies_coefficient

    def displayTask(self):
        print(f"Маша и Медведь съели {self.all_cookies} печений и банку варенья, начав и закончив одновременно. Сначала Маша ела варенье, а Медведь — печенье, но в какой-то момент они поменялись. \nМедведь и то и другое ест в {self.k} раза быстрее Маши. Сколько печений съел Медведь, если варенья они съели поровну?")
