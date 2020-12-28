data_integer = input ()

# 1

for i in range(len(data_integer)):
    print('[' + str(int(data_integer[i]) * (10 ** (len(data_integer) - (i+1)))) + ']')


# 2

data_count = len(data_integer) - 1

for i in range(len(data_integer)):
    print('['+ data_integer[i] + '0' * data_count + ']')
    data_count -= 1


'''
1. unsupported operand type(s) for +: 'int' and 'str'
즉, string 형과 integer 형 사이의 + 연산이 불가능하다는 메시지인데
문자열인 [, ] 과 연산하기 위해 #1 에서는 좌항, 우항을 모두 문자열로
캐스팅해서 연산할 수 있게 만들었다. 또, #2 에서는 input() 으로 받을 때
문자열로 입력 받기 때문에 data_integer 의 인덱스만 하나씩 출력해서 문자열인 '0' 을
data_count 와 곱해서 출력한 다음 data_count 를 하나씩 줄여
다음 값의 자릿수를 줄일 수 있게 만들었다.
2. print([내용]) 처럼 리스트의 내부 형식만 빌려 대괄호를 표시해도
괜찮을까에 대한 공부가 필요하다.
'''