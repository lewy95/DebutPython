class Cat2:

    def __init__(self):
        self.name = "加菲猫"

    def eat(self):
        # 哪一个对象调用的方法，self就是哪一个对象的引用
        print("%s 爱吃鱼" % self.name)

    def drink(self):
        print("%s 要喝水" % self.name)


# 创建两个猫对象
tom3 = Cat2()
tom4 = Cat2()

tom4.name = "无毛猫"

tom3.eat()  # 加菲猫 爱吃鱼
tom4.eat()  # 无毛猫 爱吃鱼
