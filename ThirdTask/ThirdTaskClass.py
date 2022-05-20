import random

class ThirdTaskClass:
    variants = [0, 0, 0, 0]
    answer = [0, 0, 0, 0]
    text = "Установите соответствие между величинами и их возможными значениями: к каждому элементу первого столбца подберите соответствующий элемент из второго столбца"

    @property
    def Answer(self):
        return self.answer

    def displayTask(self):
        print(self.text)
        print("\tВеличины\t\tЗначения")
        number = 0

        for key in self.abcd:
            print(f"{key}) {self.abcd[key]}\t\t{number + 1}) {self.variants[number]}")
            number += 1

    def displayAnswer(self):
        for num in range(0, 4):
            print(self.Answer[num] + 1)
