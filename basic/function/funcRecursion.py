"""
需求:定义一个函数 sum_numbers,能够接收一个 num 的整数参数
计算 1 + 2 + ...
"""


def sum_numbers(num):
    if num == 1:
        return 1

        # 假设 sum_numbers 能够完成 num - 1 的累加

    temp = sum_numbers(num - 1)
    # 函数内部的核心算法就是 两个数字的相加
    return num + temp


print(sum_numbers(5))
