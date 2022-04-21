def func(num):
    if num == 0:
        return 0
    print(num)
    num -= 1
    return func(num)

func(10)

