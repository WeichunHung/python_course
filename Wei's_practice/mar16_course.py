'''
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]

thislist[1:4] = ["blackcurrant", "watermelon"]

print(thislist)
'''

#1-50的3的倍數
'''
i = 1
while i <= 50:
    if i % 3 == 0:
        print(i)
    i = i + 1
'''
for x in range(1,51):
    if x % 3 == 0:
        print(x,"是3的倍數")
    else: print(x,"不是3的倍數")
'''
nestlist= [
    (1,2,3),
    {1,2},
    [(1,2,3,4),(4,5)]
]
print(nestlist[2][1])
'''
