from GeneratingModule.Factory import Factory
from GeneratingModule.ThirdTask.FirstTemplate import FirstTemplate
from GeneratingModule.ThirdTask.SecondTemplate import SecondTemplate


class ThirdTaskFactory(Factory):

    def __init__(self):
        self.templates_num = 2

    def new_task(self, template_id):
        if template_id == 1:
            return FirstTemplate()
        if template_id == 2:
            return SecondTemplate()
        return None
