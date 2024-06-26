import random
from cmath import sin, cos, pi

from PIL import Image, ImageDraw, ImageFont
from GeneratingModule.BaseTaskClass import BaseTaskClass


class SecondTemplate(BaseTaskClass):

    hours = minutes = -1

    def __init__(self):
        # генерируем количество часов
        self.hours = random.randint(0, 12)
        # генерируем, на каком из значений часов будет стоять минутная стрелка
        self.minutes = random.randint(0, 11)
        # гарантируем, что часовая стрелка не будет совпадать с минутной
        while self.hours == self.minutes:
            self.minutes = random.randint(0, 11)

        # вычисляем ответ с помощью формулы
        self.Answer = abs(self.hours - self.minutes) * 30
        if self.Answer > 180:
            self.Answer = 360 - self.Answer

        # корректируем значение минут для правильного отображения в условии
        self.minutes = self.minutes * 5

    def get_text(self):
        return f"Какой угол (в градусах) образуют минутная и часовая стрелки в {self.hours}:{self.minutes}?"

    def get_image(self):
        # подготовка холста
        new_img = Image.new('RGB', (400, 400), 'white')
        pencil = ImageDraw.Draw(new_img)
        font = ImageFont.load_default()

        # рисуем циферблат
        pencil.ellipse((0, 0, 390, 390), outline='black')
        # пишем цифры, обозначающие часы
        for i in range(0, 12):
            x = float(190 + 180 * sin(((i + 1) * 2 * pi) / 12).real)
            y = float(190 - 180 * cos(((i + 1) * 2 * pi) / 12).real)
            pencil.text((x, y), f"{i + 1}", font=font, fill='black', size=100)

        # рисуем часовую стрелку
        x = float(190 + 90 * sin((self.hours * 2 * pi) / 12).real)
        y = float(190 - 90 * cos((self.hours * 2 * pi) / 12).real)
        pencil.line((190, 190, x, y), fill="black")
        # рисуем минутную стрелку
        x = float(190 + 160 * sin((self.minutes / 5 * 2 * pi) / 12).real)
        y = float(190 - 160 * cos((self.minutes / 5 * 2 * pi) / 12).real)
        pencil.line((190, 190, x, y), fill="black")
        return new_img
