import random
#not done

class ThirdTaskClass:
    abcd = []
    variants = []
    answer = []
    text = ""

    @property
    def Answer(self):
        return self.answer

    def __init__(self):
        self.text = "Установите соответствие между величинами и их возможными значениями: к каждому элементу первого столбца подберите соответствующий элемент из второго столбца"
        self.answer[0] = random.randint(1, 4)
        while True:
            self.answer[1] = random.randint(1, 4)
            if self.answer[0] != self.answer[1]:
                break
        while True:
            self.answer[2] = random.randint(1, 4)
            if self.answer[0] != self.answer[2] and self.answer[1] != self.answer[2]:
                break
        while True:
            self.answer[3] = random.randint(1, 4)
            if self.answer[0] != self.answer[3] and self.answer[1] != self.answer[3] and self.answer[2] != self.answer[
                3]:
                break

    def displayTask(self):
        print(self.text)
        print("\tВеличины\t\tЗначения")
        letter = 'A'
        number = 1
        for item in self.abcd:
            print(f"{letter}) {item}\t\t{number}) {self.variants[number]}")
            letter = letter + 1
            number = number + 1

    def displayAnswer(self):
        print(self.Answer)
