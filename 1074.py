data_integer = int(input())

# 1
while data_integer:
    print(data_integer)
    data_integer -= 1

# 2
for i in range(data_integer, 0, -1): # for 변수 in range(시작, 끝, 증가폭)
    print(i)