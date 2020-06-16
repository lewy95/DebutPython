class Singleton(object):
    # 记录第一个被创建对象的引用
    __instance = None

    # 记录是否执行过初始化动作
    __init_flag = False

    def __new__(cls, *args, **kwargs):

        # 1. 判断类属性是否是空对象
        if cls.__instance is None:
            # 2. 调用父类的方法，为第一个对象分配空间
            cls.__instance = super().__new__(cls)

        # 3. 返回类属性保存的对象引用
        return cls.__instance

    def __init__(self):

        # 1. 判断是否执行过初始化动作
        if Singleton.__init_flag:
            return

        # 2. 如果没有执行过，在执行初始化动作
        print("进行初始化")

        # 3. 修改类属性的标记
        # print(Singleton.init_flag) # 第一次为False
        Singleton.__init_flag = True


# 创建多个对象
s1 = Singleton()
print(s1)  # <__main__.Singleton object at 0x103122dd0>

s2 = Singleton()
print(s2)  # <__main__.Singleton object at 0x103122dd0>
