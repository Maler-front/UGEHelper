from GeneratingModule.FifthTask.FirstTemplate import FirstTemplate
from GeneratingModule.FifthTask.SecondTemplate import SecondTemplate
from GeneratingModule.Factory import Factory


class FifthTaskFactory(Factory):

    def __init__(self):
        self.templates_num = 2

    def new_task(self, template_id):
        if template_id == 1:
            return FirstTemplate()
        if template_id == 2:
            return SecondTemplate()
        return None
