# 定义一个字典
fcb = {"brand": "bayern",
       "address": "sebera",
       "boss": "heneisi",
       "champion": True
       }

print(fcb)
print(fcb.keys()) # dict_keys(['brand', 'address', 'boss', 'champion'])
print(fcb.values()) # dict_values(['bayern', 'sebera', 'heneisi', True])
print(fcb.items()) # dict_items([('brand', 'bayern'), ('address', 'sebera'), ('boss', 'heneisi'), ('champion', True)])
print(fcb["boss"]) # heneisi
del fcb["boss"]
if "boss" in fcb.keys():
    print("yes")
else:
    print("no")
    
# fcb.clear()
print(fcb.keys()) # dict_keys(['brand', 'address', 'champion'])
print(len(fcb)) # 3

print(type(str(fcb)))

