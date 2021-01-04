data_integer = list(map(int, input().split()))

for i in data_integer:
    if i > 0:
        print('plus')
        if i % 2 == 0:
            print('even')
        else:
            print('odd')
    elif i < 0:
        print('minus')
        if i % 2 == 0:
            print('even')
        else:
            print('odd')
    elif i == 0:
        print('zero')
        if i % 2 == 0:
            print('even')
        else:
            print('odd')
