class Fruit:
    """超类"""
    pass


class Apple(Fruit):
    """子类"""
    pass


# 判断 type 和 isinstance 的区别
print(isinstance(Fruit(), Fruit))  # True
print(type(Fruit()) == Fruit)  # True

print(isinstance(Apple(), Fruit))  # True
print(type(Apple()) == Fruit)  # False   type()不考虑继承关系

# 补充：用issubclass判断某类是不是另一类的子类
print(issubclass(Apple, Fruit))  # 判断 Apple 是 Fruit 的子类   # False
print(issubclass(Fruit, Apple))  # 判断 Fruit 是 Apple 的子类   # True
