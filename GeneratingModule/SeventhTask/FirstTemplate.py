import random
import numpy
from PIL import Image, ImageDraw, ImageFont
from GeneratingModule.BaseTaskClass import BaseTaskClass


class FirstTemplate(BaseTaskClass):
    points: []
    coefficients: []

    def __init__(self):
        self.Answer = []
        while not self.Answer:
            self.points = []
            k = 0
            for i in range(4):
                self.points.append({
                    "x": random.randint(-9, 9),
                    "y": random.randint(-7, 7),
                    "derivative": 0
                })
            for i in range(4):
                for j in range(i + 1, 4):
                    if self.points[i]['x'] == self.points[j]['x']:
                        k += 1
            if k > 0:
                continue

            der_points = [
                random.randint(2, 5),
                random.randint(1, 4) / random.randint(3, 4),
                -random.randint(2, 5),
                -random.randint(1, 4) / random.randint(3, 4)
            ]

            for i in range(4):
                self.points[i]["derivative"] = der_points[i]

            matrix = [
                [],
                [],
                [],
                [],
                [],
                [],
                [],
                []
            ]
            for i in range(4):
                for j in range(8):
                    matrix[i].append(self.points[i]["x"] ** j)
            for i in range(4):
                matrix[4 + i].append(0)
                for j in range(1, 8):
                    matrix[4 + i].append(j * (self.points[i]["x"] ** (j - 1)))

            answer_matrix = []
            for i in range(4):
                answer_matrix.append(self.points[i]["y"])
            for i in range(4):
                answer_matrix.append(self.points[i]["derivative"])

            try:
                self.coefficients = numpy.linalg.solve(matrix, answer_matrix)
            except BaseException:
                continue

            error = 0
            for i in range(-1000, 1000):
                if abs(self.func_y_count(i / 100)) >= 10:
                    error += 1
            if error != 0:
                continue

            self.points.sort(key=lambda x: x["derivative"])

            k_negative_big = k_positive_big = 0
            minimum = maximum = self.points[0]["x"]
            for i in range(len(self.points)):
                if self.points[i]["x"] < minimum:
                    minimum = self.points[i]["x"]
                    k_negative_big = i
                if self.points[i]["x"] > maximum:
                    maximum = self.points[i]["x"]
                    k_positive_big = i

            x_array = []
            for i in range(4):
                if i != k_negative_big and i != k_positive_big:
                    x_array.append([i, self.points[i]["x"]])
            if x_array[0][1] < x_array[1][1]:
                k_negative_small = x_array[0][0]
                k_positive_small = x_array[1][0]
            else:
                k_negative_small = x_array[1][0]
                k_positive_small = x_array[0][0]

            self.Answer.clear()
            self.Answer = [k_negative_big + 1, k_negative_small + 1, k_positive_small + 1, k_positive_big + 1]

            self.Answer = int(''.join([str(i) for i in self.Answer]))

    def func_y_count(self, x: float):
        y = 0
        for i in range(len(self.coefficients)):
            y += self.coefficients[i] * (x ** i)
        return y

    def get_text(self):
        text = "На рисунке изображены график функции и касательные, проведённые к нему в точках с абсциссами A, B, C и D.\n" \
               "В правом столбце указаны значения производной функции в точках A, B, C и D.\n " \
               "Пользуясь графиком, поставьте в соответствие каждой точке значение производной функции в ней.\n" \
               "ТОЧКИ\tЗНАЧЕНИЯ ПРОИЗВОДНОЙ"

        letters = [
            "A",
            "B",
            "C",
            "D"
        ]
        self.points.sort(key=lambda x: x["derivative"])
        for i in range(4):
            text += f"\n{letters[i]}\t\t{i + 1}) {round(self.points[i]['derivative'], 2)}"

        text += "\nВ таблице под каждой буквой укажите соответствующий номер."

        return text

    def get_image(self):
        letters = [
            "A",
            "B",
            "C",
            "D"
        ]
        img_x = 400
        img_y = 400
        standart_line_width = 1
        new_img = Image.new('RGB', (img_x, img_y), 'white')
        pencil = ImageDraw.Draw(new_img)
        font = ImageFont.load_default()

        pencil.line((img_x / 2, 0, img_x / 2, img_y), fill="black", width=standart_line_width)
        pencil.line((0, img_y / 2, img_x, img_y / 2), fill="black", width=standart_line_width)
        arrow_sizes_k = 1 / 50
        pencil.line((img_x / 2, 0, img_x / 2 - img_x * arrow_sizes_k, img_y * arrow_sizes_k), fill="black",
                    width=standart_line_width)
        pencil.line((img_x / 2, 0, img_x / 2 + img_x * arrow_sizes_k, img_y * arrow_sizes_k), fill="black",
                    width=standart_line_width)
        pencil.line((img_x, img_y / 2, img_x - img_x * arrow_sizes_k, img_y / 2 - img_y * arrow_sizes_k), fill="black",
                    width=standart_line_width)
        pencil.line((img_x, img_y / 2, img_x - img_x * arrow_sizes_k, img_y / 2 + img_y * arrow_sizes_k), fill="black",
                    width=standart_line_width)

        prev_x = x = 0
        prev_y = y = self.func_y_count(prev_x)
        iterations = 200
        for i in range(iterations):
            prev_x = x
            prev_y = y
            x = -10 / iterations * i
            y = self.func_y_count(x)
            pencil.line((img_x / 2 + img_x / 20 * prev_x, img_y / 2 - img_y / 20 * prev_y, img_x / 2 + img_x / 20 * x, img_y / 2 - img_y / 20 * y), fill="black", width=1)
        prev_x = x = 0
        prev_y = y = self.func_y_count(prev_x)
        for i in range(iterations):
            prev_x = x
            prev_y = y
            x = 10 / iterations * i
            y = self.func_y_count(x)
            pencil.line((img_x / 2 + img_x / 20 * prev_x, img_y / 2 - img_y / 20 * prev_y, img_x / 2 + img_x / 20 * x, img_y / 2 - img_y / 20 * y), fill="black", width=1)

        dot_radius = 5
        letter_index = 0
        self.points.sort(key=lambda x: x["x"])
        for item in self.points:
            b = item["y"] - item["derivative"] * item["x"]
            first_point = {
                "x": item["x"] - 1,
                "y": item["derivative"] * (item["x"] - 1) + b
            }
            second_point = {
                "x": item["x"] + 1,
                "y": item["derivative"] * (item["x"] + 1) + b
            }

            x_coord = img_x / 2 + img_x / 20 * item["x"]
            y_coord = img_y / 2 - img_y / 20 * item["y"]
            if y_coord < img_y / 2:
                k = 1
            else:
                k = -1

            pencil.line((img_x / 2 + img_x / 20 * first_point["x"], img_y / 2 - img_y / 20 * first_point["y"], img_x / 2 + img_x / 20 * second_point["x"], img_y / 2 - img_y / 20 * second_point["y"]), fill="black", width=2)
            pencil.ellipse((x_coord - dot_radius, y_coord - dot_radius, x_coord + dot_radius, y_coord + dot_radius), fill="black")
            pencil.text((x_coord, img_y / 2 + k * img_y / 20), f"{letters[letter_index]}", font=font, fill='black', size=200)
            letter_index += 1

            segment_dotted_lines_width = 20
            dotted_lines = round(abs(y_coord - img_y / 2) / segment_dotted_lines_width)
            if abs(y_coord - img_y / 2) / segment_dotted_lines_width < dotted_lines:
                dotted_lines -= 1

            for i in range(dotted_lines):
                pencil.line((x_coord, y_coord + k * segment_dotted_lines_width * (i + 0.5), x_coord, y_coord + k * segment_dotted_lines_width * (i + 1)), fill="black", width=1)

        return new_img
