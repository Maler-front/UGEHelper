import random
from EleventhTask.FirstTemplate import FirstTemplate
from EleventhTask.SecondTemplate import SecondTemplate


class EleventhTaskFactory:

    @staticmethod
    def newTask():
        match random.randint(1, 2):
            case 1:
                return FirstTemplate()
            case 2:
                return SecondTemplate()
