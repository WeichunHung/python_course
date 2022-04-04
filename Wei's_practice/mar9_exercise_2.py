# 題目1： 0-100 的質數
"""
for x in range(2,101):
    for y in range(2,x):
        if x % y == 0:
            break
    else:
        print(x)
"""
"""
x = int(input("請輸入數字: "))

for n in range(2,x):
    if x % n == 0:
        print("不是質數")
    else: print("是質數")
    break
"""

n = int(input("請輸入數字:"))
x = 2

while x < n:
    if n % x == 0:
        print("不是質數")
        break
    x = x + 1
if x == n:
    print("是質數")

