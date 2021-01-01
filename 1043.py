data_integer_a, data_integer_b = map(int, input().split())

# 1
print(data_integer_a%data_integer_b)

# 2
data_quotient, data_remainder = divmod(data_integer_a, data_integer_b)
print(data_remainder)