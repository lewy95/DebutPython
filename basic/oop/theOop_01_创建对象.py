class Cat:

    def eat(self):
        print("小猫爱吃鱼")

    def drink(self):
        print("小猫要喝水")


# 创建猫对象
tom1 = Cat()
tom3 = tom1
print(tom1)  # <__main__.Cat object at 0x10f008ad0>
print(tom3)  # <__main__.Cat object at 0x10f008ad0>
print(tom1 == tom3) # True
tom2 = Cat()
print(tom2)  # <__main__.Cat object at 0x10f0f3bd0>
print(tom1 == tom2) # False
print("%x" % id(tom1))  # 0x10f008ad0
print("%x" % id(tom2))  # 0x10f0f3bd0
print("%x" % id(tom3))  # 0x10f008ad0

tom1.eat()
tom2.drink()

# 可以通过.attribute的方法给一个对象添加属性，但是只对当前对象生效
# 这种复制方式在开发中不推荐使用，它破坏了对象的封装性
tom1.name = "i am tom1"
print(tom1.name)
# print(tom2.name)  tom2并没有name属性
