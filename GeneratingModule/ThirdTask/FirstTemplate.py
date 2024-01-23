import io
import random
import matplotlib.pyplot as plt
from GeneratingModule.BaseTaskClass import BaseTaskClass

class FirstTemplate(BaseTaskClass):
    def __init__(self):
        self.rivers = {
            "Амур": 0,
            "Вилюй": 0,
            "Волга": 0,
            "Енисей": 0,
            "Иртыш": 0,
            "Лена": 0,
            "Нижняя Тунгусска": 0,
            "Обь": 0
        }
        self.Answer = 1
        for key in self.rivers.keys():
            self.rivers[key] = random.randint(100, 500) / 100
            if self.rivers[key] > self.rivers["Амур"]:
                self.Answer += 1

    def get_text(self):
        return "На диаграмме приведены данные о длине восьми крупнейших рек России (в тысячах километров). Первое место по длине занимает река Лена\n" \
               "На каком месте по длине находится река Амур?"

    def get_image(self):
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)

        plt.clf()
        plt.bar(self.rivers.keys(), self.rivers.values())
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        plot_bytes = buffer.getvalue()
        buffer.close()
        return plot_bytes
