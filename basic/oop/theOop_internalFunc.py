def laugh():
    """happy"""
    print("r u happy?")


print(dir(laugh))  # 带参数时，返回传入参数的属性、方法列表
# ['Player', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__',
# '__name__', '__package__', '__spec__']
print(dir())  # 不带参数时，当前范围内的变量、方法和定义的类型列表
# ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__',
# '__loader__', '__name__', '__package__', '__spec__', 'player']

print(laugh.__doc__)  # 展示注解 happy
