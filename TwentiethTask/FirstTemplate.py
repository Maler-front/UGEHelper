import random

from FirstTask.FirstTaskClass import FirstTaskClass


class FirstTemplate(FirstTaskClass):
    total_distance: int
    time_dif: int
    second_car_speed: int
    first_car_distance: int

    def __init__(self):
        self.Answer = random.randint(4, 12) * 10
        first_car_time = random.randint(2, 8)
        self.first_car_distance = self.Answer * first_car_time

        self.second_car_speed = random.randint(4, 12) * 10
        second_car_time = random.randint(2, 8)
        while second_car_time >= first_car_time:
            second_car_time = random.randint(2, 8)
        second_car_distance = self.second_car_speed * second_car_time

        self.total_distance = self.first_car_distance + second_car_distance
        self.time_dif = first_car_time - second_car_time

    def displayTask(self):
        print(f"Расстояние между городами А и В равно {self.total_distance} км. Из города А в город В выехал первый автомобиль, \nа через {self.time_dif} часа после этого навстречу ему из города В выехал со скоростью {self.second_car_speed} км/ч второй автомобиль. \nНайдите скорость первого автомобиля, если автомобили встретились на расстоянии {self.first_car_distance} км от города А. Ответ дайте в км/ч")