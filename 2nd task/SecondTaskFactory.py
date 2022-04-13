import random
import First2Template
import Second2Template
import Third2Template


class SecondTaskFactory:

    @staticmethod
    def newTask():
        task = random.randint(1, 2)
        if task == 1:
            return First2Template()
        elif task == 2:
            return Second2Template()
        else:
            return Third2Template()