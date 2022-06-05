import random
from NinteenthTask.FirstTemplate import FirstTemplate
from NinteenthTask.SecondTemplate import SecondTemplate


class NinteenthTaskFactory:

    @staticmethod
    def newTask():
        match random.randint(1, 1):
            case 1:
                return FirstTemplate()
            case 2:
                return SecondTemplate()