import random
from abc import abstractmethod


class Factory:
    templates_num: int

    def new_random_task(self):
        task = random.randint(1, self.templates_num)
        return self.new_task(task)

    @abstractmethod
    def new_task(self, template_id):
        pass