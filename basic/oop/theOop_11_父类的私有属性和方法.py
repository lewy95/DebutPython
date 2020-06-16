class Father:

    def __init__(self):
        self.num1 = 100  # 共有属性
        self.__num2 = 200  # 私有属性

    def __test(self):
        """私有方法"""
        print("父类的私有方法 %d %d" % (self.num1, self.__num2))

    def test(self):
        """共有方法，可以在父类的共有方法中访问私有属性和方法"""
        print("父类的公有方法 %d" % self.__num2)
        # 调用父类的私有方法
        self.__test()


class Son(Father):

    def visit(self):
        # 在子类的对象方法中，不能访问父类的私有属性
        # print("访问父类的私有属性 %d" % self.__num2)

        # 在子类的对象方法中，不能调用父类的私有方法
        # self.__test()

        # 访问父类的公有属性
        print("子类方法 %d" % self.num1)

        # 调用父类的公有方法
        self.test()


# 创建一个子类对象
son = Son()

# 在外界访问父类的公有属性/调用公有方法
# print(son.num1)
# son.test()

# 在外界不能直接访问对象的私有属性/调用私有方法
# print(son.__num2)
# son.__test()

# 可以通过访问父类共有方法中从中访问父类的私有属性/方法
son.visit()




