# 題目1： 200-300的數字中
# 是3的倍數但不是2的倍數

for x in range(200,301):

    if x % 2 != 0 and x % 3 == 0:
        print(x)