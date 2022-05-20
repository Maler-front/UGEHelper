import random

from FirstTask.FirstTaskClass import FirstTaskClass
from functions import degree


class SecondTemplate(FirstTaskClass):
    a = b = c = 1

    def __init__(self):
        a = random.randint(2, 7)
        b = random.randint(2, 7)
        c = random.randint(2, 7)
        while b == a:
            b = random.randint(2, 7)
        while c == a or c == b:
            c = random.randint(2, 7)
        self.Answer = a * b * c
        flag = {
            "a": 3,
            "b": 3,
            "c": 3
        }
        while flag['a'] != 0 or flag['b'] != 0 or flag['c'] != 0:
            num = 1
            match random.randint(1, 3):
                case 1:
                    if flag['a'] != 0:
                        flag['a'] -= 1
                        num = a
                case 2:
                    if flag['b'] != 0:
                        flag['b'] -= 1
                        num = b
                case 3:
                    if flag['c'] != 0:
                        flag['c'] -= 1
                        num = c
            match random.randint(1, 3):
                case 1:
                    self.a *= num
                case 2:
                    self.b *= num
                case 3:
                    self.c *= num

    def displayTask(self):
        print("Среднее геометрическое трёх чисел: a, b и c – вычисляется по формуле g = " + degree(3) + u"\u221a" + f"abc . Вычислите среднее геометрическое чисел {self.a}, {self.b} и {self.c}. ")