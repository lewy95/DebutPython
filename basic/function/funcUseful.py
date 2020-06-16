import functools
import math


def say_hi(): pass


# abs 求绝对值
print(abs(-99.9))  # 99.9
# all 用于判断给定的参数中的所有元素是否都为TRUE，除(0、空、None、False)
print(all([0.1, 1, -1]))  # 返回 True
print(all((None, 1)))  # 返回 False（其中一个元素为None）
print(all([0, 1, -1]))  # 返回 False（其中一个元素为0）
print(all([" ", "0", ""]))  # 返回 False(第三个元素为空)
# any 用于判断给定的参数是否全部为False，如果有一个为True，则返回True
print(any((None, 1)))  # 返回 True（其中一个元素为True）
print(any((None, 0, "", False)))  # 返回 False（这几个元素都是False）
# bin 返回一个整数int或者长整数long int的二进制
print(bin(10))
print(bool(10))  # True
print(bool([0]))  # True
print(bool([0, 0, 0]))  # True
print(bool(0))  # False
print(bool())  # False
# bytearray 返回一个新字节数组，元素可变，并每个元素的值范围（0-255）
b = bytearray("abcd", encoding="utf-8")
print(b[0])  # 返回数字97，即把abcd的a对应的ascii码打印出来了
b[0] = 99  # 把字符串第一个字节修改为99（即对应字母为c）
print(b)  # 返回：bytearray(b'cbcd') 第一个字节a已被修改为c
# callable 函数用于检查一个对象是否可调用的
print(callable(say_hi))
print(callable(b))
# chr 用一个范围在range(256)内（即0～255）的整数作参数，返回一个对应的ASCII数值
print(chr(98))  # 把数字98在ascii码中对应的字符打印出来
# dict 函数用来将元组/列表转换为字典格式
print(dict([('one', 1), ('two', 2), ('three', 3)]))  # 可迭代对象方式来构造字典
# 返回：{'two': 2, 'one': 1, 'three': 3}
print(dict(zip(["1", "2", "3"], ["a", "b", "c"])))  # 映射函数方式来构造字典
# 返回：{'2': 'b', '3': 'c', '1': 'a'}
print(dir())  # 获得当前模块的属性列表
print(dir([]))  # 查看列表的方法
# divmod 函数把除数和余数运算结果结合起来，返回一个包含商和余数的元组（商x，余数y）
print(divmod(5, 2))  # 返回：(2, 1)
print(divmod(5, 1))  # 返回：(5, 0)
print(divmod(5, 3))  # 返回：(1, 2)
# enumerate 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print(list(enumerate(seasons)))  # 返回：[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
print(list(enumerate(seasons, start=1)))  # 返回：[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
# eval 函数用来执行一个字符串表达式，并返回表达式的值
print(eval('3 * 2'))  # 6
x = 7
print(eval('3 + x'))  # 10
# exec 执行储存在字符串或文件中的Python语句，相比于eval，exec可以执行更复杂的Python代码
exec("print('Hello World')")  # Hello World
exec("for i in range(5): print('iter time is %d'%i)")
# filter 用于过滤序列，过滤掉不符合条件的元素，返回一个迭代器对象，可用list()来转换为列表
# 接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判断，然后返回True或 False，最后将返回 True 的元素放到新列表中
res = filter(lambda n: n > 5, range(10))  # 过滤掉0-9中不符合n>5的数据
for i in res:  # 循环打印符合n>5的数据
    print(i)
# format是一种格式化字符串的函数 基本语法是通过 {} 和 : 来接受不限个参数，位置可以不按顺序
print("{}{}".format('a', '1'))  # a1
print('name:{n},url:{u}'.format(n='alex', u='www.xxxxx.com'))  # name:alex,url:www.xxxxx.com
print("{0[0]},{0[1]}".format(('baidu', 'com')))  # 按顺序 baidu,com
print("{0[2]},{0[0]},{0[1]}".format(('baidu', 'com', 'www')))  # 不按顺序 www,baidu,com
# float 函数用于将整数和字符串转换成浮点数
print(float(1))  # 1.0
print(float(0.1))  # 0.1
print(float('123'))  # 123.0
# frozenset 返回一个冻结的集合（一个无序的不重复元素序列），冻结后集合不能再添加或删除任何元素
a = frozenset(range(10))  # 先创建一个冻结集合
print(a)  # frozenset({0, 1, 2, 3, 4, 5, 6, 7, 8, 9})
# del a[0]  # 试图删除冻结集合a中的元素，报错 TypeError: 'frozenset' object doesn't support item deletion
# globals 函数会以字典格式返回当前位置的全部全局变量
print(globals())


# hasattr 函数用于判断对象是否包含对应的属性，如果对象有该属性返回 True，否则返回 False
class t:
    a = 1
    b = 2
    c = 3


p = t()
print(hasattr(p, 'a'))  # True
print(hasattr(p, 'b'))  # True
print(hasattr(p, 'x'))  # False
# hash() 用于获取一个对象（数字或者字符串等）的哈希值。不能直接应用于 list、set、dictionary
# 注意：在 hash() 对对象使用时，所得的结果不仅和对象的内容有关，还和对象的 id()，也就是内存地址有关
print(hash(1))  # 1
print(hash(20000))  # 20000
print(hash('123'))  # -6436280630278763230
print(hash('ab12'))  # 5468785079765213470
print(hash('ab12'))  # 5468785079765213470
# help() 函数用于查看函数或模块用途的详细说明
# help('sys')  # 查看 sys 模块的帮助
# help('str')  # 查看 str 数据类型的帮助
# hex 函数用于将一个整数转换为十六进制数。返回一个字符串，以0x开头
print(hex(1))  # 0x1
print(hex(-256))  # -0x100
print(type(hex(-256)))  # <class 'str'>
# id()函数用于获取对象的内存地址
a = "123"  # 字符串
print(id(a))  # 13870392
b = [1, 2, 3]  # 列表
print(id(b))  # 7184328
c = {'num1': 1, 'num2': 2, 'num3': 3}  # 字典
print(id(c))  # 6923656
# int 函数用于将一个字符串或数字转换为整型
print(int())  # 不传入参数时，得到结果0
print(int(0.5))  # 去掉小数部分，得到结果0
print(int(3))  # 得到结果3
print(int('0xa', 16))  # 十六进制数“0xa”转换成十进制整数，得到结果10
print(int('00010', 2))  # 二进制数“00010”转换成十进制整数，得到结果2
# isinstance 函数来判断一个对象是否是一个已知的类型，返回布尔值
# 类似 type()，不同的是 type() 不会认为子类是一种父类类型，不考虑继承关系。  　　
# 　　　　             isinstance() 会认为子类是一种父类类型，考虑继承关系。  　　
# 如果要判断两个类型是否相同推荐使用 isinstance()
a = 2
print(isinstance(a, int))  # True
print(isinstance(a, str))  # False
print(isinstance(a, (str, tuple, dict)))  # False
print(isinstance(a, (str, tuple, int)))  # 是元组其中的一个则返回True


class A:
    pass


class B(A):
    pass


print(isinstance(A(), A))  # True
print(type(A()) == A)  # True

print(isinstance(B(), A))  # True
print(type(B()) == A)  # False   type()不考虑继承关系


# issubclass 用于判断参数class是否是类型参数的子类，是则返回True，否则返回False
class a:
    pass


class b(a):  # b继承了a，即b是a的子类
    pass


print(issubclass(a, b))  # 判断 a 是 b 的子类   # False
print(issubclass(b, a))  # 判断 b 是 a 的子类   # True

# iter 函数用来生成迭代器，list、tuple等都是可迭代对象
# 可以对获取到的迭代器不断用next()函数来获取下条数据
# 一直next会越界，可以用try捕获异常
# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])

# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
        print(x)
    except StopIteration:
        break
    # 遇到StopIteration就退出循环

# len 方法返回对象（字符、列表、元组等）长度或元素个数
print(len('1234'))  # 字符串，返回字符长度4
print(len(['1234', 'asd', 1]))  # 列表，返回元素个数3
print(len((1, 2, 3, 4, 50)))  # 元组，返回元素个数5
# print(len(12))                  # 注意：整数类型不适用，否则报错 TypeError: object of type 'int' has no len()
# list() 用于将元组转换为列表
print(list((1, 2, 3)))  # [1, 2, 3]
# map()接收函数f和list，并通过把函数f依次作用在list的每个元素上，得到一个新的list并返回
res = map(lambda n: n * 2, [0, 1, 2, 3, 4, 5])  # 使用 lambda 匿名函数
for i in res:
    print(i)  # 返回以下数据：0 2 4 6 8 10
# 提供了两个列表，对相同位置的列表数据进行相加
a = map(lambda x, y: x + y, [1, 2, 3, 4, 5], [2, 4, 6, 8, 10])
for i in a:
    print(i)  # 返回以下数据：3 6 9 12 15
# max()函数返回给定参数的最大值，参数可以为序列
print("max(10,20,30):", max(10, 20, 30))  # max(10,20,30): 30
print("max(10,-2,3.4):", max(10, -2, 3.4))  # max(10,-2,3.4): 10
print("max({'b':2,'a':1,'c':0}):", max({'b': 2, 'a': 1, 'c': 0}))  # 字典，默认按key排序 max({'b':2,'a':1,'c':0}): c
# min()函数返回给定参数的最小值，参数可以为序列
print("min(10,20,30):", min(10, 20, 30))  # min(10,20,30): 10
print("min(10,-2,3.4):", min(10, -2, 3.4))  # min(10,-2,3.4): -2
print("min({'b':2,'a':1,'c':0}):", min({'b': 2, 'a': 1, 'c': 0}))  # 字典，默认按key排序 min({'b':2,'a':1,'c':0}): a
# oct 函数将一个整数转换成八进制字符串
print(oct(10))  # 0o12
print(oct(255))  # 0o377
print(oct(-6655))  # -0o14777
# ord()函数是chr()的配对函数，它以一个字符（长度为1的字符串）作为参数，返回对应的ASCII数值，或者Unicode数值
# 如果所给的 Unicode 字符超出了定义范围，则会引发一个 TypeError 的异常
print(ord('b'))  # 返回：98
print(ord('%'))  # 返回：37
# pow()函数返回x的y次方的值
print(pow(2, 2))  # 2的二次方
print(pow(2, -2))  # 2的负二次方
print(math.pow(2, 2))  # 2的二次方 引入math后会返回float
# reduce 函数会对参数序列中元素进行累积
a = functools.reduce(lambda x, y: x + y, [1, 2, 3])
print(a)  # 6 ， 即从1加到3
b = functools.reduce(lambda x, y: x + y, range(10))
print(b)  # 45 ， 即从0加到9
# repr() 函数将对象转化为供解释器读取的形式, 返回一个对象的 string 格式
r = repr((1, 2, 3))
print(r)  # (1, 2, 3)
print(type(r))  # <class 'str'>
dict = repr({'a': 1, 'b': 2, 'c': 3})
print(dict)  # {'c': 3, 'a': 1, 'b': 2}
print(type(dict))  # <class 'str'>
#  reversed() 函数返回一个反转的迭代器
#  reversed(seq)要转换的序列，可以是 tuple, string, list 或 range
rev = reversed([1, 2, 3, 4, 5])  # 列表
print(list(rev))  # [5, 4, 3, 2, 1]
rev1 = reversed("school")  # 元组
print(tuple(rev1))  # ('l', 'o', 'o', 'h', 'c', 's')
rev2 = reversed(range(10))  # range
print(list(rev2))  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
# round 方法返回浮点数x的四舍五入值
print(round(4.3))  # 只有一个参数时，默认保留到整数 4
print(round(2.678, 2))  # 保留2位小数 2.68
print(round(5 / 3, 3))  # 运算表达式并保留3位小数 1.667
# set() 函数创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等
a = set('school')
print(a)  # 重复的被删除，得到结果：{'o', 'c', 's', 'l', 'h'}
b = {1, 2, 3, 4, 5}
c = {2, 4, 6, 8, 10}
print(b & c)  # 交集，得到结果为{2, 4}
print(b | c)  # 并集，得到结果为{1, 2, 3, 4, 5, 6, 8, 10}
print(b - c)  # 差集，得到结果为{1, 3, 5}
# slice() 函数实现切片对象，主要用在切片操作函数里的参数传递
a = slice("school")
print(a)  # slice(None, 'school', None)
# sorted() 函数对所有可迭代的对象进行排序（默认升序）操作
# 对列表进行排序
print(sorted([1, 2, 5, 30, 4, 22]))  # [1, 2, 4, 5, 22, 30]
# 对字典进行排序
dict = {23: 42, 1: 0, 98: 46, 47: -28}
print(sorted(dict))  # 只对key排序 [1, 23, 47, 98]
print(sorted(dict.items()))  # 默认按key进行排序 [(1, 0), (23, 42), (47, -28), (98, 46)]
print(sorted(dict.items(), key=lambda x: x[1]))  # 用匿名函数实现按value进行排序 [(47, -28), (1, 0), (23, 42), (98, 46)]
# 利用key进行倒序排序
test1 = [1, 2, 5, 30, 4, 22]
r_list = sorted(test1, key=lambda x: x * -1)
print(r_list)  # [30, 22, 5, 4, 2, 1]
# 要进行反向排序，也可以通过传入第三个参数 reverse=True：
test2 = [1, 2, 5, 30, 4, 22]
print(sorted(test2, reverse=True))  # [30, 22, 5, 4, 2, 1]
# tuple 函数将列表转换为元组
print(tuple([1, 2, 3]))  # (1,2,3)
# zip 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，
# 然后返回由这些元组组成的对象，这样做的好处是节约了不少的内存
# 可以使用 list() 转换来输出列表。如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同。
# 利用 * 号操作符，可以将元组解压为列表
a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9, 10]

for i in zip(a, b):
    print(i)

# 返回结果：
# (1, 4)
# (2, 5)
# (3, 6)

print(list(zip(a, b)))  # list() 转换为列表
# [(1, 4), (2, 5), (3, 6)]

print(list(zip(b, c)))  # 元素个数与最短的列表一致
# [(4, 7), (5, 8), (6, 9)]

a1, a2 = zip(*zip(a, b))  # 用zip(*)解压
print(list(a1))  # [1, 2, 3]
print(list(a2))  # [4, 5, 6]
