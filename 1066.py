data_integer = list(map(int, input().split()))
data_even_number = [] # data_even_number = list() 로도 표현 가능함

for i in data_integer:
        if i % 2 == 0:
            data_even_number.append(i)

for i in data_even_number:
    print(i)

'''
python 의 for 문 개념에 대해 c, c++ 과 혼동하면 안된다.
위의 경우 data_integer 의 각각의 요소 i 에 대하여 실행하는 것이다.
또, 마지막 요소에 추가할 때는 굳이 리스트의 인덱스를 특정해 할당할 필요 없이
.append() 를 사용하면 된다는 것은 기억해두자.
'''