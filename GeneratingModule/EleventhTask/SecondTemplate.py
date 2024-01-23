from PIL import Image
import os.path
from GeneratingModule.BaseTaskClass import BaseTaskClass


class SecondTemplate(BaseTaskClass):

    def __init__(self):
        self.Answer = 14

    def get_text(self):
        return "От деревянного кубика отпилили все его вершины (см. рисунок). \n" \
               "Сколько граней у получившегося многогранника (невидимые рёбра на рисунке не изображены)? "

    def get_image(self):
        return Image.open(os.path.dirname(os.path.abspath(__file__)) + "/Images/Cube.png")