import random
from EighteenthTask.FirstTemplate import FirstTemplate
from EighteenthTask.SecondTemplate import SecondTemplate


class EighteenthTaskFactory:

    @staticmethod
    def newTask():
        match random.randint(1, 2):
            case 1:
                return FirstTemplate()
            case 2:
                return SecondTemplate()

