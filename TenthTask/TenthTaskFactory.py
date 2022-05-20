import random
from TenthTask.FirstTemplate import FirstTemplate
from TenthTask.SecondTemplate import SecondTemplate


class TenthTaskFactory:

    @staticmethod
    def newTask():
        match random.randint(2, 2):
            case 1:
                return FirstTemplate()
            case 2:
                return SecondTemplate()
