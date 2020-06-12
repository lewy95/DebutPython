# 定义一个全局变量
testGlobal = "yy"

def modify_global2():
    testGlobal = "oo"
    print(testGlobal) # oo

modify_global2()

# 测试全局变量修改
def modify_global():
    global testGlobal  # global用于获取全局变量
    print(testGlobal)  # "yy"
    testGlobal = 0.0
    print(testGlobal)  # 0.0

modify_global()
print(testGlobal)