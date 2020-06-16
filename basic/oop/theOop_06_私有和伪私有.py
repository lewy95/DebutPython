class Cat6:

    def __init__(self, name):

        self.name = name
        self.__age = 18

    def __secret(self):
        # 这个一个私有方法，不允许被外部访问
        # 但在对象的方法内部，是可以访问对象的私有属性的
        print("%s 的猫龄是 %d" % (self.name, self.__age))


cat1 = Cat6("橘猫")

# 私有属性，在外界不能够被直接访问
# print(cat1.__age)  # 报错：'Cat6' object has no attribute '__age'
# 但是在python中本质上没有严格意义的私有，还是可以通过其他的方式访问到，所以应该称为伪私有
# 伪私有的处理方式：
# print(cat1._Cat6__age)  #18
# 私有方法，同样不允许在外界直接访问
# cat1.__secret()    # 报错：'Cat6' object has no attribute '__secret'
# 伪私有的处理方式：
cat1._Cat6__secret()      # 橘猫 的猫龄是 18
