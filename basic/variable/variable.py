import math
import operator
import random

# money per kg
price = 8.5
# kg
weight = 7.5
# total money
money = price * weight
money -= 5

print(money)

# vac = "i am a variable"
# vac = 10086
# print(vac) # 10086

x = y = z = 10099
a, b, c = 1, 2, "haha"
print(type(c))  # <class 'str'>
# id()函数查看变量的内存地址
print(id(c))  # 2832763712432
c = 123
print(id(c))  # 140709509824576

# about num
i = 9
f1 = 9.15
f2 = -9.15
f3 = 2.5e2
print(f3 * 102) # 测试浮点数的科学计数法
print(max(2, 3, 1, 6))
print(pow(2, 3))  # 8\
print(round(9.82, 1))
print(math.ceil(f1))  # 10 向上取整
print(math.exp(2))  # 7.38905609893065 e的平方
print(math.log2(8))  # 3.0 以2为底8的对数
print(math.log(math.exp(2)))  # 2.0
print(math.modf(9.15)[1])
print(operator.abs(f2))  # 9.15 取绝对值
print(operator.eq(3, 4))  # False
print(operator.gt(3, 4))  # False
print(random.choice(range(10)))

# about str
greeting = "hello, i am lewy."
print(greeting[3:10])  # lo, i a
print("f" in greeting[3:10])  # False
print("a" in greeting[3:10])  # True

print("lewy \n anna")  # 转义
print(R"lewy \n anna")  # 不转义
print(r"lewy \n anna")  # 不转义

# My name is krala and weight is 21 kg!
print("My name is %s and weight is %d kg!" % ('krala', 21))

rawRange = range(10)
print(type(rawRange))
myTuple = tuple(rawRange)
print(myTuple)


# 得 (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

