data_integer_a, data_integer_b = map(int, input().split())

# 1
print('%d' % (data_integer_a > data_integer_b and data_integer_a or data_integer_b))

# 2
print('%d' % (data_integer_a if data_integer_a > data_integer_b else data_integer_b))

'''
3항 연산자를 이용하는 문제였다.

보통 3항 연산자는 result = condition ? when True : when False; 로 사용된다.
그러나 python 에서는 두 가지 방법이 있다고 한다.

1. and 와 or 를 이용한 3 항 연산자
result = condition and when True or when False

2. if 와 else 를 이용한 3 항 연산자
result = when True if condition else when False

보통 c, c++ 배울 때는 result = if condition when true else when false 이런 식인데
python 에서 if 문을 이용해 3 항 연산자를 만들 때는 condition 이 참이면 when True 를 연산하고,
거짓이면 else 뒤의 when False 를 연산하게 된다고 한다.

참고 : https://blueshw.github.io/2016/01/22/python-conditional-ternary-operator/
'''