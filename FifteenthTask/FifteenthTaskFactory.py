import random
from FifteenthTask.FirstTemplate import FirstTemplate


class FifteenthTaskFactory:

    @staticmethod
    def newTask():
        return FirstTemplate()
