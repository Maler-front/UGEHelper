from PIL import Image
import os.path
from FirstTask.FirstTaskClass import FirstTaskClass


class SecondTemplate(FirstTaskClass):

    def __init__(self):
        self.Answer = 14

    def displayTask(self):
        image = Image.open(os.path.dirname(os.path.abspath(__file__)) + "/Images/Cube.png")
        image.show()
        print("От деревянного кубика отпилили все его вершины (см. рисунок). Сколько граней \nу получившегося многогранника (невидимые рёбра на рисунке не изображены)? ")