data_integer_a, data_integer_b = map(bool, map(int, input().split()))
print(
    data_integer_a,
    int(data_integer_b),
    '%i' % (data_integer_a and data_integer_b)
)