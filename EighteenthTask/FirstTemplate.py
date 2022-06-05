import random

from FirstTask.FirstTaskClass import FirstTaskClass


class FirstTemplate(FirstTaskClass):

    all_students: int
    first_club: int
    second_club: int
    question_par1: int
    question_par2: int

    def __init__(self):
        self.Answer = ""
        while self.Answer == "":
            self.first_club = random.randint(3, 15)
            self.second_club = random.randint(3, 15)
            while self.second_club < self.first_club:
                self.second_club = random.randint(3, 15)
            self.all_students = self.first_club + self.second_club - random.randint(0, self.first_club)
            self.question_par1 = random.randint(2, 4)
            self.question_par2 = random.randint(5, 15)

            if self.all_students - self.first_club - self.second_club <= -self.question_par1:
                self.Answer += "2"
            if self.first_club == self.all_students or self.second_club == self.all_students:
                self.Answer += "3"
            if self.first_club >= self.question_par2 and self.second_club >= self.question_par2:
                self.Answer += "4"

    def displayTask(self):
        print(f"В классе учится {self.all_students} человек, из них {self.first_club} человек посещают кружок по истории, а {self.second_club} — кружок по математике. Выберите утверждения, которые верны при указанных условиях.")
        print("1) Каждый ученик этого класса посещает оба кружка")
        print(f"2)  Найдётся хотя бы {self.question_par1} учеников из этого класса, посещающих оба кружка.")
        print("3)  Если ученик из этого класса ходит на кружок по истории, то он обязательно ходит на кружок по математике.")
        print(f"4) Не найдётся {self.question_par2} человек из этого класса, которые посещают оба кружка.")
        print("В ответе запишите номера выбранных утверждений без пробелов, запятых и других дополнительных символов.")