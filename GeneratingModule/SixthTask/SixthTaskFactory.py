from GeneratingModule.Factory import Factory
from GeneratingModule.SixthTask.FirstTemplate import FirstTemplate
from GeneratingModule.SixthTask.SecondTemplate import SecondTemplate


class SixthTaskFactory(Factory):

    def __init__(self):
        self.templates_num = 2

    def new_task(self, template_id):
        #if template_id == 1:
        #    return FirstTemplate()
        #if template_id == 2:
        #    return SecondTemplate()
        #return None
        return SecondTemplate()
