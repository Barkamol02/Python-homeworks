#returning uncommon elements of 2 lists using loop
list1 = [1, 1, 2]
list2 = [2, 3, 4]
uncommon= []
for i in list1:
    if i not in list2:
        uncommon.append(i)
for i in list2:
    if i not in list1:
        uncommon.append(i)        
print(uncommon)       