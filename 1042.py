data_integer_a, data_integer_b = map(int, input().split())

print(data_integer_a//data_integer_b)

'''
1. input().split() 의 결과가 문자열 리스트여서 map 을
이용해 한번에 int로 캐스팅을 할 수 있다.

2. //: 나머지를 제외한 몫, %: 몫을 제외한 나머지
'''