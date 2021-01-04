# 이 경우 문자를 직접 지정해줬지만 정수를 입력 받은 다음 아스키를 이용해서 할 수도 있다.

data_character = list(input().split())

for i in data_character:
    if i == 'A':
        print('best!!!')
    elif i == 'B':
        print('good!!')
    elif i == 'C':
        print('run!')
    elif i == 'D':
        print('slowly~')
    else:
        print('what?')