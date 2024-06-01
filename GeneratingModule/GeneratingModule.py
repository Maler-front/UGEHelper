from GeneratingModule.FirstTask.FirstTaskFactory import FirstTaskFactory as F1
from GeneratingModule.SecondTask.SecondTaskFactory import SecondTaskFactory as F2
from GeneratingModule.ThirdTask.ThirdTaskFactory import ThirdTaskFactory as F3
from GeneratingModule.FourthTask.FourthTaskFactory import FourthTaskFactory as F4
from GeneratingModule.FifthTask.FifthTaskFactory import FifthTaskFactory as F5
from GeneratingModule.SixthTask.SixthTaskFactory import SixthTaskFactory as F6
from GeneratingModule.SeventhTask.SeventhTaskFactory import SeventhTaskFactory as F7
from GeneratingModule.EightthTask.EightthTaskFactory import EightthTaskFactory as F8
from GeneratingModule.NinthTask.NinthTaskFactory import NinthTaskFactory as F9
from GeneratingModule.TenthTask.TenthTaskFactory import TenthTaskFactory as F10
from GeneratingModule.EleventhTask.EleventhTaskFactory import EleventhTaskFactory as F11
from GeneratingModule.TwelvthTask.TwelvthTaskFactory import TwelvthTaskFactory as F12
from GeneratingModule.ThirteenthTask.ThirteenthTaskFactory import ThirteenthTaskFactory as F13
from GeneratingModule.FourteenthTask.FourteenthTaskFactory import FourteenthTaskFactory as F14
from GeneratingModule.FifteenthTask.FifteenthTaskFactory import FifteenthTaskFactory as F15
from GeneratingModule.SixteenthTask.SixteenthTaskFactory import SixteenthTaskFactory as F16
from GeneratingModule.SeventeenthTask.SeventeenthTaskFactory import SeventeenthTaskFactory as F17
from GeneratingModule.EighteenthTask.EighteenthTaskFactory import EighteenthTaskFactory as F18
from GeneratingModule.NinteenthTask.NinteenthTaskFactory import NinteenthTaskFactory as F19
from GeneratingModule.TwentiethTask.TwentiesTaskFactory import TwentiethTaskFactory as F20
from GeneratingModule.TwentyfirstTask.TwentyfirstTaskFactory import TwentyfirstTaskFactory as F21


class GeneratingModule:

    @staticmethod
    def get_task(task_id, prototype_id):
        factory = GeneratingModule.get_factory(task_id)
        return factory.new_task(prototype_id)

    @staticmethod
    def get_random_task(task_id):
        factory = GeneratingModule.get_factory(task_id)
        return factory.new_random_task()

    @staticmethod
    def get_factory(task_id):
        task_id = int(task_id)
        if task_id == 1:
            return F1()
        if task_id == 2:
            return F2()
        if task_id == 3:
            return F3()
        if task_id == 4:
            return F4()
        if task_id == 5:
            return F5()
        if task_id == 6:
            return F6()
        if task_id == 7:
            return F7()
        if task_id == 8:
            return F8()
        if task_id == 9:
            return F9()
        if task_id == 10:
            return F10()
        if task_id == 11:
            return F11()
        if task_id == 12:
            return F12()
        if task_id == 13:
            return F13()
        if task_id == 14:
            return F14()
        if task_id == 15:
            return F15()
        if task_id == 16:
            return F16()
        if task_id == 17:
            return F17()
        if task_id == 18:
            return F18()
        if task_id == 19:
            return F19()
        if task_id == 20:
            return F20()
        if task_id == 21:
            return F21()

        return None

    @staticmethod
    def get_task_info(task_id):
        factory = GeneratingModule.get_factory(task_id)
        text = f'В данном задании есть {factory.templates_num} прототипа:\n\n'
        for i in range(1, factory.templates_num + 1):
            text += f'{i}.\n' + factory.new_task(i).get_text() + '\n\n'
        return text

    @staticmethod
    def get_prototipes_num(task_id):
        factory = GeneratingModule.get_factory(task_id)
        return factory.templates_num


