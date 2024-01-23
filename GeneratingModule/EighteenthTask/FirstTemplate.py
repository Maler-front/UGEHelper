import random
from math import log, sqrt
from fractions import Fraction
from PIL import Image, ImageDraw, ImageFont
from GeneratingModule.BaseTaskClass import BaseTaskClass
from functions import downDegree, degree


class FirstTemplate(BaseTaskClass):

    line: [] ##Границы
    log_a: int
    log_b: int
    frac: Fraction
    root: int
    reverse_frac: Fraction

    def __init__(self):
        self.line = [0, 0]
        self.line[0] = random.randint(-2, 0)
        self.line[1] = random.randint(6, 8)
        points_range = 1

        self.log_a = random.randint(2, 15)
        self.log_b = random.randint(2, 15)
        while self.log_a == self.log_b or log(self.log_b, self.log_a) < self.line[0] or log(self.log_b, self.log_a) > self.line[1]:
            self.log_a = random.randint(2, 15)
            self.log_b = random.randint(2, 15)

        self.frac = Fraction(random.randint(-20, 20), random.randint(1, 20))
        while self.frac % 1 == 0 or self.frac == 0 or self.frac <= self.line[0] or self.frac >= self.line[1] or abs(log(self.log_b, self.log_a) - self.frac) < points_range:
            self.frac = Fraction(random.randint(-20, 20), random.randint(1, 20))

        self.reverse_frac = Fraction(random.randint(1, 10), random.randint(1, 10))
        while self.reverse_frac % 1 == 0 or self.reverse_frac ** -1 <= self.line[0] or self.reverse_frac ** -1 >= self.line[1] or abs(log(self.log_b, self.log_a) - self.reverse_frac) < points_range or abs(self.reverse_frac - self.frac) < points_range:
            self.reverse_frac = Fraction(random.randint(1, 10), random.randint(1, 10))

        self.root = random.randint(self.line[0] + 1, self.line[1] - 1) ** 2 + random.randint(1, 5)
        while abs(log(self.log_b, self.log_a) - self.root) < points_range or abs(self.root - self.reverse_frac) < points_range or abs(self.root - self.frac) < points_range:
            self.root = random.randint(self.line[0] + 1, self.line[1] - 1) ** 2 + random.randint(1, 5)

        mass = {
            1: log(self.log_b, self.log_a),
            2: self.frac,
            3: sqrt(self.root),
            4: self.reverse_frac ** -1
        }

        answer = []
        for i in range(4):
            minimal = 1000
            minimal_key = 0
            for key, value in mass.items():
                if value < minimal:
                    minimal = value
                    minimal_key = key
            answer.append(minimal_key)
            mass.pop(minimal_key)
        self.Answer = int(''.join([str(i) for i in answer]))

    def get_text(self):
        return f"На координатной прямой отмечены точки A, B, C и D. Каждой точке соответствует одно из чисел в правом столбце. " \
               f"\nУстановите соответствие между указанными точками и числами.\n" \
               f"Точки\tЧисла\nA\t\t" \
               f"1) log{downDegree(self.log_a)}{self.log_b}\nB\t\t" \
               f"2) {self.frac}\nC\t\t" \
               f"3) " + u"\u221a" + f"{self.root}\nD\t\t" \
                f"4) ({self.reverse_frac}){degree(-1)}\n" \
                f"В таблице под каждой буквой укажите соответствующий номер"

    def get_image(self):
        img_x = 400
        img_y = 200
        iterations = self.line[1] - self.line[0]
        current_num = self.line[0]
        letter = '1'
        radius = 5
        case_counter = 0
        optimal_space = 10
        mass = {
            1: log(self.log_b, self.log_a),
            2: self.frac,
            3: sqrt(self.root),
            4: self.reverse_frac ** -1
        }
        new_img = Image.new('RGB', (img_x, img_y), 'white')
        pencil = ImageDraw.Draw(new_img)
        font = ImageFont.load_default()

        pencil.line((10, img_y / 2, img_x - 10, img_y / 2), fill="black")

        for i in range(iterations):
            pencil.line((img_x / iterations * i + optimal_space, img_y / 2 + 5, img_x / iterations * i + optimal_space, img_y / 2 - 5), fill="black")
            pencil.text((img_x / iterations * i + optimal_space, img_y / 2 + 20), f"{current_num}", font=font, fill='black')
            current_num += 1

        for i in [int(i) for i in str(self.answer)]:
            x = -self.line[0] + mass[i] / iterations * img_x
            pencil.ellipse(((-self.line[0] + mass[i]) / iterations * img_x - radius + optimal_space, img_y / 2 - radius, (-self.line[0] + mass[i]) / iterations * img_x + radius + optimal_space, img_y / 2 + radius), fill="black")
            match case_counter:
                case 0:
                    letter = 'A'
                case 1:
                    letter = 'B'
                case 2:
                    letter = 'C'
                case 3:
                    letter = 'D'
            case_counter += 1
            pencil.text(((-self.line[0] + mass[i]) / iterations * img_x + optimal_space, img_y / 2 - 20), f"{letter}", font=font, fill='black', size=100)

        return new_img