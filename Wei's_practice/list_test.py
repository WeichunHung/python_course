test_list = [1, 2, 3, 4, 5]
a = []
for i in test_list:
    a.append(i * 3)
# print(a)
print([i * 3 for i in test_list])

# test_list = ['a', 'b', 'c', 'd', 'e']
# newlist = []
# a = ''.join(test_list)
#
# print(a)

lis = [{'Product': "Nandini", "age" : 20},
       {'Product': "Manjeet", "age" : 20 },
       {'Product': "Nikhil" , "age" : 19 },
       {'Product': 'newbalace', 'age': 17}]
print("The list printed sorting by age: ")
print(sorted(lis, key=lambda i: i['age']))

list =[]
a = {'Product': '[New Balance]連帽短袖上衣_女性_藍色_WT21520NGO', 'Price': 1280}
b = {'Product': '[New Balance]連帽短袖上衣_女性_暈染色_WT21526WM', 'Price': 1480}

list.append(a)
print(list)

