import random
from SecondTask.FirstTemplate import First2Template
from SecondTask.SecondTemplate import Second2Template
from SecondTask.ThirdTemplate import Third2Template


class SecondTaskFactory:

    @staticmethod
    def newTask():
        task = random.randint(1, 3)
        if task == 1:
            return First2Template()
        elif task == 2:
            return Second2Template()
        else:
            return Third2Template()
