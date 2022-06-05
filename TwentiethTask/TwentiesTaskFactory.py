import random
from TwentiethTask.FirstTemplate import FirstTemplate
from TwentiethTask.SecondTemplate import SecondTemplate


class TwentiethTaskFactory:

    @staticmethod
    def newTask():
        match random.randint(1, 2):
            case 1:
                return FirstTemplate()
            case 2:
                return SecondTemplate()