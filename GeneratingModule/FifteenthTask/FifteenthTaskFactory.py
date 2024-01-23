from GeneratingModule.Factory import Factory
from GeneratingModule.FifteenthTask.FirstTemplate import FirstTemplate
from GeneratingModule.FifteenthTask.SecondTemplate import SecondTemplate
from GeneratingModule.FifteenthTask.ThirdTemplate import ThirdTemplate


class FifteenthTaskFactory(Factory):

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

