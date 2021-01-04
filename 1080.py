data_integer = int(input())
data_sum = 0

if 0 < data_integer <= 1000:    
    for i in range(1, 1000):
        data_sum += i
        if data_sum >= data_integer:
            print(i)
            break
else:
    print('out of range')