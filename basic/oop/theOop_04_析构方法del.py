class Cat3:

    def __init__(self, name):
        self.name = name

    def __del__(self):
        """__del__只需要一个self参数即可，__init__中的参数它都可以用"""
        print("%s 吃饱喝足了" % self.name)

    def eat(self):
        # 哪一个对象调用的方法，self就是哪一个对象的引用
        print("%s 爱吃鱼" % self.name)

    def drink(self):
        print("%s 要喝水" % self.name)


# 创建两个猫对象
tom3 = Cat3("橘猫")
tom4 = Cat3("无毛猫")

tom3.eat()  # 橘猫 爱吃鱼
tom4.eat()  # 无毛猫 爱吃鱼
