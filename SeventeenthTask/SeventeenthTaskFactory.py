import random
from SeventeenthTask.FirstTemplate import FirstTemplate
from SeventeenthTask.SecondTemplate import SecondTemplate


class SeventeenthTaskFactory:

    @staticmethod
    def newTask():
        match random.randint(1, 2):
            case 1:
                return FirstTemplate()
            case 2:
                return SecondTemplate()
