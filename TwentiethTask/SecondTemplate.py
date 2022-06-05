import random

from FirstTask.FirstTaskClass import FirstTaskClass


class SecondTemplate(FirstTaskClass):
    difference: int

    def __init__(self):
        self.Answer = random.randint(1, 5) * 10
        self.difference = int((self.Answer / 10) ** 2)

    def displayTask(self):
        print(f"В понедельник акции компании подорожали на некоторое число процентов, а во вторник подешевели на то же самое число процентов. \nВ результате они стали стоить на {self.difference}% дешевле, чем при открытии торгов в понедельник. \nНа сколько процентов подорожали акции компании в понедельник?")