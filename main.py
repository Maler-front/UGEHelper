import sys
from FirstTask.FirstTaskFactory import FirstTaskFactory as F1
from SecondTask.SecondTaskFactory import SecondTaskFactory as F2
from ThirdTask.ThirdTaskFactory import ThirdTaskFactory as F3
from FourthTask.FourthTaskFactory import FourthTaskFactory as F4
from FifthTask.FifthTaskFactory import FifthTaskFactory as F5
from SixthTask.SixthTaskFactory import SixthTaskFactory as F6
from SeventhTask.SeventhTaskFactory import SeventhTaskFactory as F7
from EightthTask.EightTaskFactory import EightthTaskFactory as F8
from NinthTask.NinthTaskFactory import NinthTaskFactory as F9
from TenthTask.TenthTaskFactory import TenthTaskFactory as F10
from EleventhTask.EleventhTaskFactory import EleventhTaskFactory as F11
from TwelvthTask.TwelvthTaskFactory import TwelvthTaskFactory as F12
from ThirteenthTask.ThirteenthTaskFactory import ThirteenthTaskFactory as F13
from FourteenthTask.FourteenthTaskFactory import FourteenthTaskFactory as F14
from FifteenthTask.FifteenthTaskFactory import FifteenthTaskFactory as F15
from SixteenthTask.SixteenthTaskFactory import SixteenthTaskFactory as F16
from SeventeenthTask.SeventeenthTaskFactory import SeventeenthTaskFactory as F17
from EighteenthTask.EighteenthTaskFactory import EighteenthTaskFactory as F18
from NinteenthTask.NinteenthTaskFactory import NinteenthTaskFactory as F19
from TwentiethTask.TwentiesTaskFactory import TwentiethTaskFactory as F20
from TwentyfirstTask.TwentyfirstTaskFactory import TwentyfirstTaskFactory as F21

choice = 0
while True:
    choice = input("Напишите номер задания для его генерирования или 0 для выхода\n")
    task = 0
    match choice:
        case "1":
            factory = F1()
        case "2":
            factory = F2()
        case "3":
            factory = F3()
        case "4":
            factory = F4()
        case "5":
            factory = F5()
        case "6":
            factory = F6()
        case "7":
            factory = F7()
        case "8":
            factory = F8()
        case "9":
            factory = F9()
        case "10":
            factory = F10()
        case "11":
            factory = F11()
        case "12":
            factory = F12()
        case "13":
            factory = F13()
        case "14":
            factory = F14()
        case "15":
            factory = F15()
        case "16":
            factory = F16()
        case "17":
            factory = F17()
        case "18":
            factory = F18()
        case "19":
            factory = F19()
        case "20":
            factory = F20()
        case "21":
            factory = F21()
        case "0":
            quit()
    if factory:
        task = factory.newTask()
        task.displayTask()
        input("Ответ:")
        task.displayAnswer()
