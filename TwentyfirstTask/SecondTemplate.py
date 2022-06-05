import random
from PIL import Image, ImageDraw, ImageFont
from FirstTask.FirstTaskClass import FirstTaskClass


class SecondTemplate(FirstTaskClass):
    p1: int
    p2: int
    p3: int

    def __init__(self):
        while self.Answer < 1:
            self.p1 = random.randint(2, 50)
            self.p2 = random.randint(2, 50)
            self.p3 = random.randint(2, 50)
            self.Answer = self.p3 - self.p2 + self.p1

    def displayTask(self):
        new_img = Image.new('RGB', (400, 400), 'white')
        pencil = ImageDraw.Draw(new_img)
        font = ImageFont.load_default()

        pencil.line((0, 0, 0, 399), fill="black")
        pencil.line((0, 0, 399, 0), fill="black")
        pencil.line((0, 399, 399, 399), fill="black")
        pencil.line((399, 0, 399, 399), fill="black")
        pencil.line((300, 0, 300, 399), fill="black")
        pencil.line((0, 300, 399, 300), fill="black")

        pencil.text((150, 150), f"{self.p1}", font=font, fill='black', size=100)
        pencil.text((350, 150), f"{self.p2}", font=font, fill='black', size=100)
        pencil.text((350, 350), f"{self.p3}", font=font, fill='black', size=100)
        pencil.text((150, 350), "?", font=font, fill='black', size=100)

        new_img.show()

        print(f"Прямоугольник разбит на четыре меньших прямоугольника двумя прямолинейными разрезами. \nПериметры трёх из них, начиная с левого верхнего и далее по часовой стрелке, равны {self.p1}, {self.p2} и {self.p3}. \nНайдите периметр четвёртого прямоугольника")