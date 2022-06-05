import math
import random
from math import cos, sin

from PIL import Image, ImageFont, ImageDraw
from FirstTask.FirstTaskClass import FirstTaskClass


class FirstTemplate(FirstTaskClass):
    points: []
    derivatives: []

    def __init__(self):
        ##Поле для ответов
        self.Answer = []
        ##Точки экстремума генерируемой функции
        self.points = []
        ##Значение коэффициента угла наклона производной и номер левой крайней точки экстремума
        self.derivatives = []
        ##Все положительные расстояния (по оси ординат)
        positive_distance = []
        ##Все отрицательные расстояния (по оси ординат)
        negative_distance = []
        ##Все расстояния
        distance_array = []

        ##Генерируем, пока не будут соблюдаться все условия
        while True:
            self.points.clear()
            ##Чтобы первая точка не всегда была в положительной части
            coef = 1 or -1
            ##Генерируем точки экстремума
            for i in range(random.randint(5, 8)):
                self.points.append(random.randint(1, 10) * coef)
                coef *= -1

            positive_distance.clear()
            negative_distance.clear()
            distance_array.clear()
            ##Заполняем массивы с положительными, отрицательными и вообще всеми расстояниями
            for i in range(1, len(self.points)):
                distance = self.points[i] - self.points[i - 1]
                if distance > 0:
                    positive_distance.append(distance)
                    distance_array.append(distance)
                if distance < 0:
                    negative_distance.append(distance)
                    distance_array.append(distance)

            ##Находим максимальные и минимальные положительные и отрицательные значения
            minimum_pos = min(positive_distance)
            maximum_pos = max(positive_distance)
            minimum_neg = min(negative_distance)
            maximum_neg = max(negative_distance)
            ##Если разница между ними меньше двух, то начинаем генерировать заново
            if maximum_pos - minimum_pos < 2 or abs(minimum_neg - maximum_neg) < 2:
                continue

            self.derivatives.clear()
            ##Считаем производные на самых различающихся расстояниях, что посчитали выше
            for i in range(len(distance_array)):
                if minimum_pos == distance_array[i] or maximum_pos == distance_array[i] or minimum_neg == \
                        distance_array[i] or maximum_neg == distance_array[i]:
                    self.derivatives.append([round(sin(math.pi / 3 or -math.pi / 3) * distance_array[i] / 2), i])
            ##Если подсчитаны не все производные, то генерируем заново
            if len(self.derivatives) != 4:
                continue

            ##Сортируем производные по их появлению справа налево (по второму ключу)
            self.derivatives.sort(key=lambda x: x[1])

            ##Формируем ответ
            for value in self.derivatives:
                if value[0] != max(self.derivatives, key=lambda x: x[0])[0] and value[0] > 0:
                    self.Answer.append(1)
                elif value[0] == max(self.derivatives, key=lambda x: x[0])[0]:
                    self.Answer.append(2)
                elif value[0] != min(self.derivatives, key=lambda x: x[0])[0] and value[0] < 0:
                    self.Answer.append(3)
                elif value[0] == min(self.derivatives, key=lambda x: x[0])[0]:
                    self.Answer.append(4)
            break

    def displayTask(self):
        ##Выводим все данные в консоль
        print(
            "На рисунке изображены график функции и касательные, проведённые к нему в точках с абсциссами A, B, C и D.\nВ правом столбце указаны значения производной функции в точках A, B, C и D. \nПользуясь графиком, поставьте в соответствие каждой точке значение производной функции в ней")
        print("Точки\tЗначения производной")
        print(f"A\t1) {self.derivatives[0][0]}")
        print(f"B\t2) {self.derivatives[1][0]}")
        print(f"C\t3) {self.derivatives[2][0]}")
        print(f"D\t4) {self.derivatives[3][0]}")
        print("Для каждой буквы укажите соответствующий номер")

        '''Тут указаны размеры фотографий, так же сама фотография, инструмент для работы с ней, шрифт и ширина линий'''
        img_x = 1000
        img_y = 1000
        new_img = Image.new('RGB', (img_x, img_y), 'white')
        pencil = ImageDraw.Draw(new_img)
        font = ImageFont.load_default()
        standart_line_width = 1

        ##Рисуем две оси
        pencil.line((0, img_y / 2, img_x, img_y / 2), fill="black", width=standart_line_width)
        pencil.line((img_x / 2, 0, img_x / 2, img_y), fill="black", width=standart_line_width)

        ##Рисуем стрелки на осях
        pencil.line((img_x, img_y / 2, img_x - (img_x / 25), img_y / 2 - (img_y / 25)), fill="black",
                    width=standart_line_width)
        pencil.line((img_x, img_y / 2, img_x - (img_x / 25), img_y / 2 + (img_y / 25)), fill="black",
                    width=standart_line_width)
        pencil.line((img_x / 2, 0, img_x / 2 - (img_x / 25), img_y / 25), fill="black", width=standart_line_width)
        pencil.line((img_x / 2, 0, img_x / 2 + (img_x / 25), img_y / 25), fill="black", width=standart_line_width)

        ##Плавность графика
        iterations = 100
        k = 0
        ##Для каждого промежутка рисуем часть графика на основе косинусоиды
        for x in range(1, len(self.points)):
            space_y_start = img_y / 2 - (img_y / 20 * self.points[x - 1])
            space_y_end = img_y / 2 - (img_y / 20 * self.points[x])
            x_d = img_x / len(self.points) * (x - 1)

            k = abs(space_y_end - space_y_start) / 2
            if space_y_start > space_y_end:
                for i in range(0, iterations):
                    x_start = x_d + img_x / len(self.points) / iterations * i
                    y_start = space_y_start - k - cos(math.pi / iterations * (iterations - i)) * k
                    x_end = x_d + img_x / len(self.points) / iterations * (i + 1)
                    y_end = space_y_start - k - cos(math.pi / iterations * (iterations - i - 1)) * k
                    pencil.line((x_start, y_start, x_end, y_end), fill="black", width=standart_line_width)
            else:
                for i in range(0, iterations):
                    x_start = x_d + img_x / len(self.points) / iterations * i
                    y_start = space_y_start + k - cos(math.pi / iterations * i) * k
                    x_end = x_d + img_x / len(self.points) / iterations * (i + 1)
                    y_end = space_y_start + k - cos(math.pi / iterations * (i + 1)) * k
                    pencil.line((x_start, y_start, x_end, y_end), fill="black", width=standart_line_width)

        ##Рисуем производные (только это и не работает)
        for array in self.derivatives:
            k = 0.25 or 0.75
            touch_point = {
                "x": 0,
                "y": img_y / 2 - (img_y / 20 * self.points[array[1]]) + k * (
                            (img_y / 2 - (img_y / 20 * self.points[array[1] + 1])) - (
                                img_y / 2 - (img_y / 20 * self.points[array[1]])))
            }
            if array[0] > 0:
                match k:
                    case 0.25:
                        touch_point['x'] = img_x / len(self.points) * (array[1] + math.pi * 5 / 6)
                    case 0.75:
                        touch_point['x'] = img_x / len(self.points) * (array[1] + math.pi / 6)
            else:
                match k:
                    case 0.25:
                        touch_point['x'] = img_x / len(self.points) * (array[1] + math.pi / 6)
                    case 0.75:
                        touch_point['x'] = img_x / len(self.points) * (array[1] + math.pi * 5 / 6)

            x_start = touch_point['x'] - img_x / len(self.points) / 4
            y_start = touch_point['y'] - array[0] * (- img_x / len(self.points) / 4)
            x_end = touch_point['x'] + img_x / len(self.points) / 4
            y_end = touch_point['y'] - array[0] * (img_x / len(self.points) / 4)

            pencil.line((x_start, y_start, x_end, y_end), fill="black", width=standart_line_width)

        ##Показываем картинку
        new_img.show()
