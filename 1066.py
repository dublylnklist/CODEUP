data_integer = list(map(int, input().split()))

for i in data_integer:
    if i == 0:
        print('zero')
    elif i % 2 == 0:
        print('even')
    else:
        print('odd')
