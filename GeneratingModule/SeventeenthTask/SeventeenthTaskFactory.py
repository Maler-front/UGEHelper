from GeneratingModule.Factory import Factory
from GeneratingModule.SeventeenthTask.FirstTemplate import FirstTemplate
from GeneratingModule.SeventeenthTask.SecondTemplate import SecondTemplate
from GeneratingModule.SeventeenthTask.ThirdTemplate import ThirdTemplate


class SeventeenthTaskFactory(Factory):

    def __init__(self):
        self.templates_num = 3

    def new_task(self, template_id):
        if template_id == 1:
            return FirstTemplate()
        if template_id == 2:
            return SecondTemplate()
        if template_id == 3:
            return ThirdTemplate()
        return None
