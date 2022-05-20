import random
from TwelvthTask.TwelvthTaskClass import TwelvthTaskClass


class FirstTemplate(TwelvthTaskClass):
    translater_cost = [0, 0, 0, 0, 0, 0]
    limit = 0

    def __init__(self):
        '''
            Функция регрессии выдает неправильный ответ
            Входные данные:
                skills: объект массивов способностей каждого специалиста(в будующем можно будет генерировать),
                current_cost: изменяет текущую стоимость и передает ее увеличение в более глубокий уровень,
                current_skills: скилы, которые содержит текущая группа специалистов,
                current_translaters: текущая группа специалистов(по индексам),
                n: текущий индекс специалиста
        '''
        def recursion_func(skills: {}, current_cost: int, current_skills: [], current_translaters: [], n: int):

            ##Сразу прибавляем стоимость рассматриваемого специалиста к текущей и, если она больше дозволенного, то выходим на уровень выше
            current_cost += self.translater_cost[n]
            if current_cost > self.limit:
                return

            ##Добавляем способности рассматриваемого специалиста к текущим
            for i in range(4):
                if current_skills[i] == 0:
                    current_skills[i] += skills[n][i]

            ##Добавляем самого специалиста к группе
            current_translaters.append(n)

            ##Если есть все способности, то выходим из функции, предварительно добавив текущую группу специалистов в ответ
            ##else пытаемся найти еще специалистов, вызывая эту же функцию
            skills_counter = 0
            for i in range(4):
                skills_counter += current_skills[i]
            if skills_counter == 4:
                self.Answer.append(current_translaters)
                return
            else:
                for i in range(n + 1, 5):
                    recursion_func(skills, current_cost, current_skills, current_translaters, n + 1)


        skills = [
            [0, 1, 0, 1],
            [1, 1, 0, 0],
            [1, 0, 0, 0],
            [1, 0, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ]
        self.limit = random.randint(10, 15) * 10000
        for i in range(6):
            x = random.randint(4, 8) * 1000
            self.translater_cost[i] = x

        for i in range(5):
            recursion_func(skills, self.translater_cost[i], skills[i], [i], i+1)


    def displayTask(self):
        print(f"{self.translater_cost}")
        print(f"limit:{self.limit}")
