from GeneratingModule.Factory import Factory
from GeneratingModule.SeventhTask.FirstTemplate import FirstTemplate
#from FourteenthTask.SeventhTask import SecondTemplate
#from FourteenthTask.SeventhTask import ThirdTemplate


class SeventhTaskFactory(Factory):

    def __init__(self):
        self.templates_num = 1

    def new_task(self, template_id):
        if template_id == 1:
            return FirstTemplate()
        #if template_id == 2:
        #    return SecondTemplate()
        #if template_id == 3:
        #    return ThirdTemplate()
        return None
