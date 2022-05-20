import random
from SixthTask.FirstTemplate import FirstTemplate
from SixthTask.SecondTemplate import SecondTemplate
from SixthTask.ThirdTemplate import ThirdTemplate


class SixthTaskFactory:

    @staticmethod
    def newTask():
        task = random.randint(1, 3)
        if task == 1:
            return FirstTemplate()
        elif task == 2:
            return SecondTemplate()
        else:
            return ThirdTemplate()
