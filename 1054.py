# 1
data_integer_a, data_integer_b = map(int, input().split())

print('%d' % (data_integer_a and data_integer_b))

# 2
data_boolean_a, data_boolean_b = map(bool, map(int, input().split()))

print('%i' % (data_boolean_a and data_boolean_b))

'''
data_boolean_a, b 에 bool 형으로 요소들을 넣어주고 싶었는데 
input() 을 하면 문자열 리스트로 넣어지고, bool() 은 int class 만 받으니까
먼저 int 로 캐스팅하고, 이후에 bool 로 캐스팅 해야했다.
뭔가 지저분해 보이는데 공부하면서 더 좋은 방법이 있나 생각해봐야겠다.
'''