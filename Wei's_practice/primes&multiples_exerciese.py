# 題目1： 200-300的數字中
# 是3的倍數但不是2的倍數
'''
for x in range(200,301):

    if x % 2 != 0 and x % 3 == 0:
        print(x)
'''

# 題目2： 0-100 的質數

for x in range(2,101):
    for y in range(2,x):
        if x % y == 0:
            break
    else:
        print(x)


"""
#判斷質數
#Solution_1
x = int(input("請輸入數字: "))

for n in range(2,x):
    if x % n == 0:
        print(str(x) + "不是質數")
        break
else: print(str(x) + "是質數")
"""
#Solution_2
'''
x = int(input("請輸入數字: "))

for n in range(2, x+1):
    if n == x:
        print("是質數")
        break
    if x % n == 0:
        print("不是質數")
        break
'''

# n = int(input("請輸入數字:"))
# x = 2
#
# while x < n:
#     if n % x == 0:
#         print("不是質數")
#         break
#     x = x + 1
# if x == n:
#     print("是質數")

#1-50的3的倍數
'''
i = 1
while i <= 50:
    if i % 3 == 0:
        print(i)
    i = i + 1
'''
'''
for x in range(1,51):
    if x % 3 == 0:
        print(x,"是3的倍數")
    else: print(x,"不是3的倍數")
'''


