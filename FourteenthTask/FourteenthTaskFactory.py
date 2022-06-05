import random
from FourteenthTask.FirstTemplate import FirstTemplate
##from FourteenthTask.SecondTemplate import SecondTemplate
##from FourteenthTask.ThirdTemplate import ThirdTemplate


class FourteenthTaskFactory:

    @staticmethod
    def newTask():
        match random.randint(1, 1):
            case 1:
                return FirstTemplate()
            case 2:
                return SecondTemplate()
            case 3:
                return ThirdTemplate()
