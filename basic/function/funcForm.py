def say_hello(name):
    """注释"""
    print("hola, " + name)
    print("hello")
    print("Nihao")


say_hello("anna")


def print_info(name, addr="poland"):
    """打印任何传入的字符串"""
    print("Name: " + name + ",Addr: " + addr)
    return


print_info(name="lewy")  # Name: lewy,Addr: poland
print_info(name="muller", addr="germany")  # Name: muller,Addr: germany


def test_param(*params):
    print(params[1])
    return


test_param("hello", "world", 23)  # 打印world


# 定义一个空函数
def nop():
    pass


nop()
