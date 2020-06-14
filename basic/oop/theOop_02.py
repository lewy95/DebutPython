class Cat:

    def eat(self):
        # 哪一个对象调用的方法，self就是哪一个对象的引用
        print("%s 爱吃鱼" % self.name)

    def drink(self):
        print("%s 要喝水" % self.name)


# 创建两个猫对象
tom3 = Cat()

tom4 = Cat()

tom4.name = "大懒猫"

tom4.eat()
