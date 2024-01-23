import random
from GeneratingModule.BaseTaskClass import BaseTaskClass


class FirstTemplate(BaseTaskClass):
    variants = [0, 0, 0, 0]
    answer = [0, 0, 0, 0]
    text = "Установите соответствие между величинами и их возможными значениями: к каждому элементу первого столбца подберите соответствующий элемент из второго столбца"

    def __init__(self):
        self.variants = [0, 0, 0, 0]
        self.answer = [0, 0, 0, 0]

        self.abcd = {
            "A": "Рост ребенка",
            "B": "Толщина бумаги",
            "C": "Протяженность автобусного маршрута",
            "D": "Высота жилого дома"
        }
        variants = [
            str(random.randint(90, 120)) + "см",
            str(random.randint(1, 20) / 100) + "мм",
            str(random.randint(10, 50)) + "км",
            str(random.randint(10, 100)) + "м"
        ]

        for i in range(0, 4):
            while True:
                num = random.randint(0, 3)
                if self.variants[num] == 0:
                    self.variants[num] = variants[i]
                    self.Answer[i] = num
                    break

        self.text += "\n\tВеличины\t\tЗначения"
        number = 0

        for key in self.abcd:
            self.text += f"\n{key}) {self.abcd[key]}\t\t{number + 1}) {self.variants[number]}"
            number += 1

        answer = ""
        for num in range(0, 4):
            answer += str(self.Answer[num] + 1)

        self.Answer = int(answer)

    def get_text(self):
        return self.text

    def get_image(self):
        return None
