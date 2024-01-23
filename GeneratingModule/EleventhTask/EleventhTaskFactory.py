from GeneratingModule.Factory import Factory
from GeneratingModule.EleventhTask.FirstTemplate import FirstTemplate
from GeneratingModule.EleventhTask.SecondTemplate import SecondTemplate
from GeneratingModule.EleventhTask.ThirdTemplate import ThirdTemplate


class EleventhTaskFactory(Factory):

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
