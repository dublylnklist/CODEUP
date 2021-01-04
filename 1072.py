data_integer_num = int(input())
data_integer = list(map(int, input().split()))

if len(data_integer) == data_integer_num: # 입력된 수가 data_integer_num 과 같은 지 유효성 검사
    for i in data_integer:
        print(i)
else:
    print('none')