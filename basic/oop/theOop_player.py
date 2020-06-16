class Player:
    """这是一个运动员类"""

    def __init__(self, name, number):
        # self.属性 = 形参
        self.name = name
        self.number = number

    def __str__(self):
        return "Name is %s and number is %s" % (self.name, self.number)

    def defend(self):
        """防守"""
        print("running")

    def socre(self):
        """进球"""
        pass


p1 = Player("Lewy", 9)
print(p1)
