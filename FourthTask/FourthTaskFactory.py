import random
from FourthTask.FirstTemplate import FirstTemplate
from FourthTask.SecondTemplate import SecondTemplate


class FourthTaskFactory:

    @staticmethod
    def newTask():
        task = random.randint(1, 2)
        if task == 1:
            return FirstTemplate()
        else:
            return SecondTemplate()
