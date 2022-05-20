import random
from SixteenthTask.FirstTemplate import FirstTemplate
from SixteenthTask.SecondTemplate import SecondTemplate
from SixteenthTask.ThirdTemplate import ThirdTemplate


class SixteenthTaskFactory:

    @staticmethod
    def newTask():
        match random.randint(1, 3):
            case 1:
                return FirstTemplate()
            case 2:
                return SecondTemplate()
            case 3:
                return ThirdTemplate()
