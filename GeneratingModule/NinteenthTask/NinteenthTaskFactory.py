from GeneratingModule.Factory import Factory
from GeneratingModule.NinteenthTask.FirstTemplate import FirstTemplate


class NinteenthTaskFactory(Factory):

    def __init__(self):
        self.templates_num = 1

    def new_task(self, template_id):
            return FirstTemplate()
