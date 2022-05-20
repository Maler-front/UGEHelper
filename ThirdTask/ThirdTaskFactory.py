import random
from ThirdTask.FirstTemplate import First3Template
from ThirdTask.SecondTemplate import Second3Template


class ThirdTaskFactory:

    @staticmethod
    def newTask():
        task = random.randint(1, 2)
        if task == 1:
            return First3Template()
        else:
            return Second3Template()
