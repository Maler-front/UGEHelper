from GeneratingModule.Factory import Factory
from GeneratingModule.NinteenthTask.FirstTemplate import FirstTemplate
from GeneratingModule.NinteenthTask.SecondTemplate import SecondTemplate


class NinteenthTaskFactory(Factory):

    def __init__(self):
        self.templates_num = 2

    def new_task(self, template_id):
        if template_id == 1:
            return FirstTemplate()
        if template_id == 2:
            return SecondTemplate()
        return None