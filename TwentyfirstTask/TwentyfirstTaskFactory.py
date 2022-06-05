import random
from TwentyfirstTask.FirstTemplate import FirstTemplate
from TwentyfirstTask.SecondTemplate import SecondTemplate
from TwentyfirstTask.ThirdTemplate import ThirdTemplate


class TwentyfirstTaskFactory:

    @staticmethod
    def newTask():
        match random.randint(1, 3):
            case 1:
                return FirstTemplate()
            case 2:
                return SecondTemplate()
            case 3:
                return ThirdTemplate()
