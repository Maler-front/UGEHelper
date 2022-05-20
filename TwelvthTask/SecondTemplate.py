import random
from prettytable import PrettyTable

from TwelvthTask.TwelvthTaskClass import TwelvthTaskClass


class SecondTemplate(TwelvthTaskClass):
    case = []
    max_mass: float
    max_size: int

    def __init__(self):
        self.case.clear()
        self.Answer.clear()
        while len(self.Answer) < 1 or len(self.Answer) > 3:
            self.Answer.clear()

            max_mass = random.randint(42, 54)
            self.max_mass = max_mass / 2
            self.max_size = random.randint(200, 230)

            for i in range(6):
                length = random.randint(20, 90)
                high = random.randint(20, 90)
                width = random.randint(20, 90)
                mass = random.randint(34, max_mass + 4) / 2

                self.case.append({
                    "length": length,
                    "high": high,
                    "width": width,
                    "mass": mass
                })

                if length + high + width <= self.max_size and mass <= self.max_mass:
                    self.Answer.append(i + 1)

    def displayTask(self):
        print("В таблице приведены данные о шести чемоданах.")
        table = PrettyTable()
        table.field_names = ["Номер чемодана", "Длина(см)", "Высота(см)", "Ширина(см)", "Масса(кг)"]
        for i in range(6):
            table.add_row([i + 1, self.case[i]["length"], self.case[i]["high"], self.case[i]["width"], self.case[i]["mass"]])
        print(table)
        print(f"По правилам авиакомпании сумма трёх измерений (длина, высота, ширина) чемодана,\nсдаваемого в багаж, не должна превышать {self.max_size} см, а масса не должна быть больше {self.max_mass} кг. \nКакие чемоданы можно сдать в багаж по правилам этой авиакомпании?\nВ ответе укажите номера всех выбранных чемоданов (без пробелов, запятых и других дополнительных символов).")