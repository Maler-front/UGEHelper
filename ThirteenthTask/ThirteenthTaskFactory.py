import random
from ThirteenthTask.FirstTemplate import FirstTemplate
from ThirteenthTask.SecondTemplate import SecondTemplate


class ThirteenthTaskFactory:

    @staticmethod
    def newTask():
        task = random.randint(1, 2)
        if task == 1:
            return FirstTemplate()
        else:
            return SecondTemplate()
