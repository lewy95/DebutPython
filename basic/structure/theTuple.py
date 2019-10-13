# 创建一个空元组
# tupEmpty = ()

# 创建只有一个元素的元组
tupOnlyOne = (9,)

tup1 = ('lewy', 'muller', 9, 25)
tup2 = (('lewy', 'muller'), (9, 25))
print(tup1 + tup2)
print(len(tup1 + tup2)) # 6

# 元组的访问
print(tup1[3])
print(tup1[1:2])
print(tup2[0][0])

toList = list(tup1)
print(toList)

# 元组的遍历
for t1 in tup1:  # 一维
    print(t1)

for t in tup2:  # 二维
    for t2 in t:
        print(t2)
