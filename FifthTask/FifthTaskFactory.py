import random
from FifthTask.FirstTemplate import FirstTemplate
##from FifthTask.SecondTemplate import SecondTemplate


class FifthTaskFactory:

    @staticmethod
    def newTask():
        match random.randint(1, 1):
            case 1:
                return FirstTemplate()
            case 2:
                return SecondTemplate()
