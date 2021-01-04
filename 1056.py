# 1
data_integer_a, data_integer_b = map(int, input().split())

print('%d' % (data_integer_a != data_integer_b))
print('%d' % (data_integer_a ^ data_integer_b))

# 2
data_boolean_a, data_boolean_b = map(bool, map(int, input().split()))

print('%i' % (data_boolean_a != data_boolean_b))
print('%i' % (data_boolean_a ^ data_boolean_b))

'''
여기서 ^ 는 비트연산자로 xor 연산을 해준다.
'''