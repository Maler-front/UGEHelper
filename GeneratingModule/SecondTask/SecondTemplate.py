import random
from GeneratingModule.BaseTaskClass import BaseTaskClass


class SecondTemplate(BaseTaskClass):
    variants = [0, 0, 0, 0]
    answer = [0, 0, 0, 0]
    text = "Установите соответствие между величинами и их возможными значениями: к каждому элементу первого столбца подберите соответствующий элемент из второго столбца"

    def __init__(self):
        self.variants = [0, 0, 0, 0]
        self.answer = [0, 0, 0, 0]

        self.abcd = {
            "A": "Масса взрослого человека",
            "B": "Масса грузового автомобиля",
            "C": "Масса книги",
            "D": "Масса пуговицы"
        }
        variants = [
            str(random.randint(50, 100)) + "кг",
            str(random.randint(5, 10)) + "т",
            str(random.randint(150, 500)) + "г",
            str(random.randint(2, 10)) + "г"
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
