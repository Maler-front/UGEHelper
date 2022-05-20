import random
from EightthTask.FirstTemplate import FirstTemplate
from EightthTask.SecondTemplate import SecondTemplate


class EightthTaskFactory:

    @staticmethod
    def newTask():
        match random.randint(1, 2):
            case 1:
                return FirstTemplate()
            case 2:
                return SecondTemplate()
