import random
from PIL import Image, ImageDraw, ImageFont
from FirstTask.FirstTaskClass import FirstTaskClass

class FirstTemplate(FirstTaskClass):

    a = b = 0

    def __init__(self):
        self.a = 5 * random.randint(4, 20)
        self.b = 5 * random.randint(4, 20)
        while self.b == self.a:
            self.b = 5 * random.randint(4, 20)
        self.Answer = 3 * self.a + 2 * self.b

    def displayTask(self):
        print(f"Дачный участок имеет форму прямоугольника со сторонами {self.a} метров и {self.b} метров. Хозяин планирует обнести его забором и разделить таким же забором на две части, одна из которых имеет форму квадрата. Найдите суммарную длину забора в метрах.")
        new_img = Image.new('RGB', (400, 400), 'white')
        pencil = ImageDraw.Draw(new_img)
        font = ImageFont.load_default()
        pencil.text((0, self.a), f'{self.a}m', font=font, fill='black', size=30)
        pencil.text((self.b, 0), f'{self.b}m', font=font, fill='black', size=30)
        if self.a > self.b:
            pencil.rectangle((20, 10, 2 * self.b, 2 * self.b), outline='black')
        else:
            pencil.rectangle((20, 10, 2 * self.a, 2 * self.a), outline='black')
        pencil.rectangle((20, 10, 2 * self.b, 2 * self.a), outline='black')
        new_img.show()
