import random
from FirstTask.FirstTaskClass import FirstTaskClass
from functions import get_count


class SecondTemplate(FirstTaskClass):
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



    def displayTask(self):
        print(f"ЕГЭ по физике сдавали {self.students} выпускников школы, что составляет одну {self.text} от общего числа выпускников.\nСколько выпускников этой школы не сдавали экзамена по физике? ")