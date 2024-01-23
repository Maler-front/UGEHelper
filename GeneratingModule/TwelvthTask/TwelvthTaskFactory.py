from GeneratingModule.Factory import Factory
from GeneratingModule.TwelvthTask.FirstTemplate import FirstTemplate


class TwelvthTaskFactory(Factory):

    def __init__(self):
        self.templates_num = 1

    def new_task(self, template_id):
        return FirstTemplate()
