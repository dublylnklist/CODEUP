data_integer = list(map(int, input().split()))

for i in data_integer:
    if 90 <= i  <= 100:
        print('A')
    elif 70 <= i <= 89:
        print('B')
    elif 40 <= i <= 69:
        print('C')
    elif 0 <= i <= 39:
        print('D')
    else:
        print('평가 기준 밖의 수 입니다.')