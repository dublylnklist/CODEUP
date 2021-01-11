data_integer = int(input())
data_sum = 0

for i in range(1, data_integer+1):
    if data_sum < data_integer:
        data_sum += i
    else:
        break

print(data_sum)