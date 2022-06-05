import random

from FirstTask.FirstTaskClass import FirstTaskClass


class SecondTemplate(FirstTaskClass):

    trees: []

    def __init__(self):
        self.Answer = "1"
        while self.Answer == "1":
            trees_var = [0, 1, 2]
            self.trees = [0, 0, 0]
            tree = [-1, -1, -1]

            index = random.randint(0, 2)
            self.trees[trees_var[index]] = 0
            tree[0] = trees_var[index]
            trees_var.pop(index)

            index = random.randint(0, 1)
            self.trees[trees_var[index]] = 1
            tree[1] = trees_var[index]
            trees_var.pop(index)

            self.trees[trees_var[0]] = 2
            tree[2] = trees_var[0]

            if tree[1] > tree[2]:
                self.Answer += "2"
            if tree[0] > tree[1]:
                self.Answer += "3"
            if tree[1] > tree[0]:
                self.Answer += "4"

            for i in range(0, 3):
                match self.trees[i]:
                    case 0:
                        self.trees[i] = "рябина"
                    case 1:
                        self.trees[i] = "ясень"
                    case 2:
                        self.trees[i] = "осина"

    def displayTask(self):
        print(f"Во дворе школы растут всего три дерева: ясень, рябина и осина. Известно, что {self.trees[1]} выше, чем {self.trees[0]} на 1 метр, но ниже, чем {self.trees[2]} на 2 метра. Выберите все утверждения, которые верны при указанных условиях.")
        print("1) Среди указанных деревьев не найдётся двух одной высоты. \n2) Ясень, растущий во дворе школы, выше осины, растущей там же.\n3) Любое дерево, помимо указанных, которое ниже ясеня, растущего во дворе школы, также ниже рябины, растущей там же.\n4) Любое дерево, помимо указанных, которое ниже рябины, растущей во дворе школы, также ниже ясеня, растущего там же.")
