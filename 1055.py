# 1
data_integer_a, data_integer_b = map(int, input().split())

print('%d' % (data_integer_a or data_integer_b))

# 2
data_boolean_a, data_boolean_b = map(bool, map(int, input().split()))

print('%i' % (data_boolean_a or data_boolean_b))