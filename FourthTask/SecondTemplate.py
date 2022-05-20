import random

from prettytable import PrettyTable

from FourthTask.FourthTaskClass import FourthTaskClass


class SecondTemplate(FourthTaskClass):
    price = {
        "ОК-Техника": 0,
        "Скоростной": 0,
        "Магия связи": 0,
        "Про-фон": 0,
        "Смартфон и Ко": 0,
        "Прогресс-Э": 0,
        "999 телефонов": 0,
        "Макропоиск": 0,
        "Вселенная телефонов": 0,
    }

    def __init__(self):
        middle_price = random.randint(4, 10) * 1000
        self.Answer = middle_price + 1000
        for key in self.price.keys():
            self.price[key] = middle_price + random.randint(-500, 500)
            if self.Answer > self.price[key]:
                self.Answer = self.price[key]

    def displayTask(self):
        print("В таблице представлены данные о стоимости некоторой модели смартфона в различных магазинах")
        table = PrettyTable()
        table.field_names = ["Магазин", "Цена(руб)"]
        for key in self.price.keys():
            table.add_row([key, self.price[key]])
        print(table)
        print("Найдите наименьшую стоимость смартфона среди представленных предложений. Ответ дайте в рублях. ")
