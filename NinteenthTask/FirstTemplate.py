import random

from FirstTask.FirstTaskClass import FirstTaskClass


class FirstTemplate(FirstTaskClass):
    sum_num: int
    sum_square_multiplicity: int
    sum_square_not_multiplicity: int

    def __init__(self):
        self.Answer = []
        while len(self.Answer) == 0:
            self.sum_num = random.randint(10, 23)
            self.sum_square_multiplicity = random.randint(2, 7)
            self.sum_square_not_multiplicity = self.sum_square_multiplicity * random.randint(2, 4)

            for i in range(100, 1000):
                a = i // 100
                b = i % 100 // 10
                c = i % 10
                sum_squares = a ** 2 + b ** 2 + c ** 2

                if (a + b + c) != self.sum_num:
                    continue
                elif sum_squares % self.sum_square_multiplicity != 0:
                    continue
                elif sum_squares % self.sum_square_not_multiplicity == 0:
                    continue

                self.Answer.append(i)

    def displayTask(self):
        print(f"Найдите трёхзначное число, сумма цифр которого равна {self.sum_num}, а сумма квадратов цифр делится на {self.sum_square_multiplicity}, но не делится на {self.sum_square_not_multiplicity}. В ответе укажите какое либо одно такое число.")