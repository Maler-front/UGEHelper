import random
from GeneratingModule.BaseTaskClass import BaseTaskClass


class SecondTemplate(BaseTaskClass):
    students: int
    text = ""

    def __init__(self):
        self.Answer = 0.12
        cont = 0

        while cont == 0:
            self.students = random.randint(10, 30)

            for i in range(4):

                if ((self.students * (7 - i - 1)) % (7 - i)) == 0:
                    cont = 1
                    self.Answer = self.students * ((7 - i - 1) / (7 - i))
                    match i:
                        case 0:
                            self.text = "седьмую"
                        case 1:
                            self.text = "шестую"
                        case 2:
                            self.text = "пятую"
                        case 3:
                            self.text = "четвертую"
                        case 4:
                            self.text = "третью"
                    break

    def get_text(self):
        return f"ЕГЭ по физике сдавали {self.students} выпускников школы, что составляет одну {self.text} от общего числа выпускников.\n" \
               f"Сколько выпускников этой школы не сдавали экзамена по физике?"

    def get_image(self):
        return None