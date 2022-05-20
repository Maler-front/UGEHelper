import random
from SeventhTask.FirstTemplate import FirstTemplate
from SeventhTask.SecondTemplate import SecondTemplate
from SeventhTask.ThirdTemplate import ThirdTemplate


class SeventhTaskFactory:

    @staticmethod
    def newTask():
        match random.randint(1, 3):
            case 1:
                return FirstTemplate()
            case 2:
                return SecondTemplate()
            case 3:
                return ThirdTemplate()
