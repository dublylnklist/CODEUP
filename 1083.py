data_integer = int(input())

for i in range(1, data_integer+1):
    if i % 3 == 0:
        print('X', end=' ') # print() 는 자동개행 되므로 end=' ' 를 넣어 한 줄에 공백을 포함해서 입력 되도록 했다.
    else:
        print(i, end=' ')