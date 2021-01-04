data_integer = int(input())

# 1
while data_integer:
    print(data_integer-1)
    data_integer -= 1

# 2
for i in range(data_integer-1, -1, -1): # 0 까지 출력
    print(i)