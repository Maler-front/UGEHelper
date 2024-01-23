import random
from fractions import Fraction
from PIL import Image, ImageDraw, ImageFont
from GeneratingModule.BaseTaskClass import BaseTaskClass
from functions import degree


class SecondTemplate(BaseTaskClass):
    a: int
    b: int
    answer: int

    def __init__(self):
        self.a = random.randint(2, 8)
        self.b = random.randint(2, 3)

        variants_generator = {
            1: random.randint(1, 1000),
            2: random.randint(1, 1000),
            3: random.randint(1, 1000),
            4: random.randint(1, 1000)
        }

        answer = []
        for i in range(4):
            minimal = 1000
            minimal_key = 0
            for key, value in variants_generator.items():
                if value < minimal:
                    minimal = value
                    minimal_key = key
            answer.append(minimal_key)
            variants_generator.pop(minimal_key)

        self.answer = int(''.join([str(i) for i in answer]))

    def get_text(self):
        text = ""
        case_counter = 0
        letter = 'A'
        for i in [int(i) for i in str(self.answer)]:
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
            match i:
                case 1:
                    text += f"{letter}) {self.a}{degree('n')} < {self.a ** self.b}\n"
                case 2:
                    text += f"{letter}) ({Fraction(1, self.a)}){degree('n')} > {self.a ** self.b}\n"
                case 3:
                    text += f"{letter}) ({Fraction(1, self.a)}){degree('n')} < {self.a ** self.b}\n"
                case 4:
                    text += f"{letter}) {self.a}{degree('n')} > {self.a ** self.b}\n"

        text += "\nВ таблице под каждой буквой укажите соответствующий номер." \
                "\n Каждому из четырёх неравенств в левом столбце соответствует одно из решений в правом столбце. " \
                "Установите соответствие между неравенствами и их решениями"
        return text

    def get_image(self):
        img_x = 400
        img_y = 200
        new_img = Image.new('RGB', (img_x, img_y), 'white')
        pencil = ImageDraw.Draw(new_img)
        font = ImageFont.load_default()

        for i in range(8):
            if i % 2 == 0:
                y = img_y / 20 * (2 * i + 1)
                pencil.line((0, y, img_x, y), fill="black")
                pencil.line((img_x, y, img_x - 20, y - 5), fill="black")
                pencil.line((img_x, y, img_x - 20, y + 5), fill="black")
                pencil.text((img_x - 10, y + 15), "n", font=font, fill="black")
                pencil.ellipse((img_x / 2 - 2, y - 2, img_x / 2 + 2, y + 2), outline="black")
                match i:
                    case 0 | 6:
                        pencil.text((img_x / 2, y + 15), f"{self.b}", font=font, fill='black')
                    case 2 | 4:
                        pencil.text((img_x / 2, y + 15), f"-{self.b}", font=font, fill='black')

                strokes = 50
                match i:
                    case 0 | 2:
                        for j in range(strokes):
                            pencil.line((img_x / 2 / strokes * j, y, img_x / 2 / strokes * j - 4, y - 4), fill='black')
                    case 4 | 6:
                        for j in range(strokes // 25, strokes):
                            pencil.line((
                                        img_x / 2 + img_x / 2 / strokes * j, y, img_x / 2 + img_x / 2 / strokes * j - 4,
                                        y - 4), fill='black')

        return new_img
