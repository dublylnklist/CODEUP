# 1
data_integer = 0

def InputRepeater():
    data_integer = int(input())
    
    if data_integer == 0:
        pass
    else:
        print(data_integer)
        InputRepeater()

InputRepeater()

# 2
data_integer_2 = map(int, input().split())

for i in data_integer_2:
    if i == 0:
        break
    elif i != 0:
        print(i)
    else:
        print('none')

'''
이 문제의 조건은 for, while, do ~ while 을 쓰지 않아야한다.

# 1: python 에는 없는 goto 를 위한 문제인 것으로 파악 했는데 문제 본문의 예시 처럼
계속 정수를 입력 받을 때 마다 0 의 여부를 검사해서 0 이 입력 되기 전까지 계속 입력과 출력을
해주는 코드를 작성했다.

# 2: 문제 처럼 입력된 정수 중 0 이 나올 때 까지 계속 출력하는 방법이다.
'''