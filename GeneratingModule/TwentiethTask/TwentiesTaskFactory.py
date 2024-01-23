from GeneratingModule.Factory import Factory
from GeneratingModule.TwentiethTask.FirstTemplate import FirstTemplate
from GeneratingModule.TwentiethTask.SecondTemplate import SecondTemplate


class TwentiethTaskFactory(Factory):

    def __init__(self):
        self.templates_num = 2

    def new_task(self, template_id):
        if template_id == 1:
            return FirstTemplate()
        if template_id == 2:
            return SecondTemplate()
        return None
