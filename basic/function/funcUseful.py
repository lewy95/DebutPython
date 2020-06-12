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
# format()是一种格式化字符串的函数 基本语法是通过 {} 和 : 来接受不限个参数，位置可以不按顺序
print("{}{}".format('a', '1'))  # a1
print('name:{n},url:{u}'.format(n='alex', u='www.xxxxx.com'))  # name:alex,url:www.xxxxx.com
print("{0[0]},{0[1]}".format(('baidu', 'com')))  # 按顺序 baidu,com
print("{0[2]},{0[0]},{0[1]}".format(('baidu', 'com', 'www')))  # 不按顺序 www,baidu,com
#https://www.cnblogs.com/wujiaqing/p/10709207.html