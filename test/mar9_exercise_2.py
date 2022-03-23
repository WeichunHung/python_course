# 題目1： 0-100 的質數

for x in range(2,101):
    for y in range(2,x):
        print(x, "/", y, "=", x/y)
        # if x % y == 0:
        #     break
    # else:
    #     print(x)
