import random
from NinthTask.FirstTemplate import FirstTemplate
from NinthTask.SecondTemplate import SecondTemplate
from NinthTask.ThirdTemplate import ThirdTemplate


class NinthTaskFactory:

    @staticmethod
    def newTask():
        match random.randint(1, 3):
            case 1:
                return FirstTemplate()
            case 2:
                return SecondTemplate()
            case 3:
                return ThirdTemplate()
