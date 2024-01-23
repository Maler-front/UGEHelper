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
    def get_task(task_id, prototipe_id):
        factory = GeneratingModule.get_factory(task_id)
        return factory.new_task(prototipe_id)

    @staticmethod
    def get_random_task(task_id):
        factory = GeneratingModule.get_factory(task_id)
        return factory.new_random_task()

    @staticmethod
    def get_factory(task_id):
        factory = None
        task_id = int(task_id)
        match task_id:
            case 1:
                factory = F1()
            case 2:
                factory = F2()
            case 3:
                factory = F3()
            case 4:
                factory = F4()
            case 5:
                factory = F5()
            case 6:
                factory = F6()
            case 7:
                factory = F7()
            case 8:
                factory = F8()
            case 9:
                factory = F9()
            case 10:
                factory = F10()
            case 11:
                factory = F11()
            case 12:
                factory = F12()
            case 13:
                factory = F13()
            case 14:
                factory = F14()
            case 15:
                factory = F15()
            case 16:
                factory = F16()
            case 17:
                factory = F17()
            case 18:
                factory = F18()
            case 19:
                factory = F19()
            case 20:
                factory = F20()
            case 21:
                factory = F21()
        if factory:
            return factory
        else:
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
