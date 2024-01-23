from GeneratingModule.Factory import Factory
from GeneratingModule.FirstTask.FirstTemplate import FirstTemplate
from GeneratingModule.FirstTask.SecondTemplate import SecondTemplate
from GeneratingModule.FirstTask.ThirdTemplate import ThirdTemplate


class FirstTaskFactory(Factory):

    def __init__(self):
        self.templates_num = 3

    def new_task(self, template_id):
        if template_id == 1:
            return FirstTemplate()
        if template_id == 2:
            return SecondTemplate()
        if template_id == 3:
            return  ThirdTemplate()
        return None
