from GeneratingModule.Factory import Factory
from GeneratingModule.NinthTask.FirstTemplate import FirstTemplate


class NinthTaskFactory(Factory):

    def __init__(self):
        self.templates_num = 1

    def new_task(self, template_id):
        return FirstTemplate()
