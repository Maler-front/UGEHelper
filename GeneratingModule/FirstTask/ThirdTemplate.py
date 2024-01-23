import random
from GeneratingModule.BaseTaskClass import BaseTaskClass


class ThirdTemplate(BaseTaskClass):
    volume = total = ""

    def __init__(self):
        super().__init__()
        self.total = random.randint(20, 100)
        self.volume = random.randint(1, 10)
        self.Answer = self.total // self.volume
        if self.total % self.volume != 0:
            self.Answer += 1

    def get_text(self):
        return f"Для ремонта требуется {self.total} рулона обоев.\n" \
               f"Какое наименьшее количество пачек обойного клея нужно для такого ремонта, если 1 пачка клея рассчитана на {self.volume} рулонов?"

    def get_image(self):
        return None
