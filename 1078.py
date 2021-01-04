data_integer = int(input())
data_sum = 0

for i in range(0, data_integer+1):
    if i % 2 == 0: 
        data_sum += i
    else:
        pass

print(data_sum)
