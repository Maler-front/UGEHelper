import random
from GeneratingModule.BaseTaskClass import BaseTaskClass
from PIL import Image, ImageDraw


class FirstTemplate(BaseTaskClass):
    new_img: Image
    figure_coordinates: {}
    text: str

    def __init__(self):
        scale = 30
        size = {
            "width": random.randint(6, 12),
            "high": 0
        }
        size["high"] = size["width"]

        self.new_img = Image.new('RGB', (size["width"] * scale + 1, size["high"] * scale + 1), 'white')
        pencil = ImageDraw.Draw(self.new_img)

        for i in range(0, size["width"] + 1):
            pencil.line((0, (size["width"] - i) * scale, size["high"] * scale, (size["width"] - i) * scale),
                        fill="black")
        for i in range(0, size["high"] + 1):
            pencil.line(((size["high"] - i) * scale, 0, (size["high"] - i) * scale, size["width"] * scale),
                        fill="black")

        match random.randint(1, 3):
            case 1:
                ##Трапеция
                self.text = "План местности разбит на клетки. Каждая клетка обозначает квадрат 1 м × 1 м. Найдите площадь участка, изображённого на плане. Ответ дайте в квадратных метрах. "
                points = {"a": [1, 1], "b": [], "c": [], "d": []}
                points["b"] = [points["a"][0] + random.randint(1, size["width"] - 3), points["a"][1]]
                points["c"] = [size["width"] - 1, size["high"] - 1]
                points["d"] = [points["a"][0], points["c"][1]]

                pencil.line((points["a"][0] * scale, points["a"][1] * scale, points["b"][0] * scale, points["b"][1] * scale), fill="black", width=5)
                pencil.line((points["b"][0] * scale, points["b"][1] * scale, points["c"][0] * scale, points["c"][1] * scale), fill="black", width=5)
                pencil.line((points["c"][0] * scale, points["c"][1] * scale, points["d"][0] * scale, points["d"][1] * scale), fill="black", width=5)
                pencil.line((points["d"][0] * scale, points["d"][1] * scale, points["a"][0] * scale, points["a"][1] * scale), fill="black", width=5)

                self.Answer = (points["d"][1] - points["a"][1]) * (points["b"][0] - points["a"][0]) + (points["c"][1] - points["b"][1]) * (points["c"][0] - points["b"][0]) / 2

            case 2:
                ##Треугольник
                self.text = "План местности разбит на клетки. Каждая клетка обозначает квадрат 1 м × 1 м. Найдите площадь участка, изображённого на плане. Ответ дайте в квадратных метрах. "

                points = {
                    "a": [1, size["high"] - 1],
                    "b": [random.randint(1, size["width"] - 1), 1],
                    "c": [size["width"] - 1, size["high"] - 1]}

                pencil.line(
                    (points["a"][0] * scale, points["a"][1] * scale, points["b"][0] * scale, points["b"][1] * scale),
                    fill="black", width=5)
                pencil.line(
                    (points["b"][0] * scale, points["b"][1] * scale, points["c"][0] * scale, points["c"][1] * scale),
                    fill="black", width=5)
                pencil.line(
                    (points["c"][0] * scale, points["c"][1] * scale, points["a"][0] * scale, points["a"][1] * scale),
                    fill="black", width=5)

                self.Answer = (points["c"][0] - points["a"][0]) * (points["a"][1] - points["b"][1]) / 2

            case 3:
                ##Круг
                self.text = "План местности разбит на клетки. Каждая клетка обозначает квадрат 1 м × 1 м. Найдите площадь участка, изображённого на плане. Ответ дайте в квадратных метрах, сократите его на п. "

                r = (size["width"] - 2) / 2

                pencil.ellipse((scale, scale, (size["width"] - 1) * scale, (size["width"] - 1) * scale), outline="black", width=5)
                self.Answer = r ** 2

    def get_text(self):
        return self.text

    def get_image(self):
        return self.new_img

