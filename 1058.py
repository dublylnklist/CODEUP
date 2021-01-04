data_boolean_a, data_boolean_b = map(bool, map(int, input().split()))

# 1
print('%d' % (data_boolean_a == 0 and data_boolean_b == 0))

# 2
if data_boolean_a == 0 and data_boolean_b == 0:
    print(1)
else:
    print(0)