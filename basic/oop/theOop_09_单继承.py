class Animal:
    """超类"""

    def eat(self):
        print("吃")

    def drink(self):
        print("喝")

    def run(self):
        print("跑")

    def sleep(self):
        print("睡")


class Dog(Animal):
    """子类：子类拥有父类的所有属性和方法"""

    def drink(self):
        """
        重写父类方法
        如果想要调用父类方法，可以通过super来调用
        """
        super().drink()
        print("喝喝喝")

    def bark(self):
        print("汪汪汪")


# 创建一个对象 - 狗对象
wangcai = Dog()

wangcai.eat()
wangcai.drink()
wangcai.run()
wangcai.sleep()
wangcai.bark()
