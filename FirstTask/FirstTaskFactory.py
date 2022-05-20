import random
from FirstTask.FirstTemplate import FirstTemplate
from FirstTask.SecondTemplate import SecondTemplate


class FirstTaskFactory:

    @staticmethod
    def newTask():
        task = random.randint(1, 2)
        if task == 1:
            return FirstTemplate()
        else:
            return SecondTemplate()
