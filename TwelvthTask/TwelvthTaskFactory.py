import random
from TwelvthTask.FirstTemplate import FirstTemplate
from TwelvthTask.SecondTemplate import SecondTemplate


class TwelvthTaskFactory:

    @staticmethod
    def newTask():
        task = random.randint(2, 2)
        if task == 1:
            return FirstTemplate()
        else:
            return SecondTemplate()
