import random

from GeneratingModule.BaseTaskClass import BaseTaskClass


class SecondTemplate(BaseTaskClass):
    difference: int

    def __init__(self):
        self.Answer = random.randint(1, 5) * 10
        self.difference = int((self.Answer / 10) ** 2)

    def get_text(self):
        return f"В понедельник акции компании подорожали на некоторое число процентов, а во вторник подешевели на то же самое число процентов." \
               f"В результате они стали стоить на {self.difference}% дешевле, чем при открытии торгов в понедельник. \n" \
               f"На сколько процентов подорожали акции компании в понедельник?"

    def get_image(self):
        return None