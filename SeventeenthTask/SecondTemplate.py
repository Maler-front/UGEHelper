import random
from fractions import Fraction
from PIL import Image, ImageDraw, ImageFont
from FirstTask.FirstTaskClass import FirstTaskClass
from functions import degree


class SecondTemplate(FirstTaskClass):
    a: int
    b: int
    Answer = []

    def __init__(self):
        self.a = random.randint(2, 8)
        self.b = random.randint(2, 3)

        variants_generator = {
            1: random.randint(1, 1000),
            2: random.randint(1, 1000),
            3: random.randint(1, 1000),
            4: random.randint(1, 1000)
        }

        self.Answer.clear()
        for i in range(4):
            minimal = 1000
            minimal_key = 0
            for key, value in variants_generator.items():
                if value < minimal:
                    minimal = value
                    minimal_key = key
            self.Answer.append(minimal_key)
            variants_generator.pop(minimal_key)

    def displayTask(self):
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
                            pencil.line((img_x / 2 + img_x / 2 / strokes * j, y, img_x / 2 + img_x / 2 / strokes * j - 4, y - 4), fill='black')

        new_img.show()
        print("Каждому из четырёх неравенств в левом столбце соответствует одно из решений в правом столбце. Установите соответствие между неравенствами и их решениями")
        text = ""
        case_counter = 0
        letter = 'A'
        for i in self.Answer:
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

        print(text)
        print("В таблице под каждой буквой укажите соответствующий номер.")
