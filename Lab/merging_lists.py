list1 = ['Hello', 'World']
list2 = ['everyone', 'dear']
new_list = []

for x in list1:
    for y in list2:
        new_list.append(x + ' ' + y)
print(new_list)
