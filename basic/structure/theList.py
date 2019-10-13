import keyword

# keyword下包含了所有的关键字
#print(keyword.kwlist)

name_list2 = ['boateng','mats','alaba']

name_list = ['lewy', 'muller', 'jamse']
name_list.insert(2, 'leno') #['lewy', 'muller', 'leno', 'jamse']
name_list.append("toliso") #['lewy', 'muller', 'leno', 'jamse', 'toliso']
#name_list.append(name_list2) #['lewy', 'muller', 'leno', 'jamse', 'toliso', ['boateng', 'mats', 'alaba']]
name_list[1] = "thomas" #['lewy', 'thomas', 'leno', 'jamse', 'toliso']
name_list.remove("lewy") #['thomas', 'leno', 'jamse', 'toliso']
name_list.pop() #['thomas', 'leno', 'jamse']
name_list.pop(0) #['leno', 'jamse']
#name_list.clear() #[]
print(len(name_list)) # 2
print(name_list.count("thomas"))
name_list.sort() #['jamse', 'leno']
name_list.sort(reverse=True) #['leno', 'jamse']
name_list.reverse() #['jamse', 'leno']

print(name_list)

