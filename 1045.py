data_integer_a, data_integer_b = map(int, input().split())

print(
    data_integer_a + data_integer_b,
    data_integer_a - data_integer_b,
    data_integer_a * data_integer_b,
    data_integer_a // data_integer_b,
    data_integer_a % data_integer_b,
    '%.2f' % (data_integer_a / data_integer_b),
    sep = '\n'
)