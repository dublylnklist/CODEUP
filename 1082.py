data_integer = int(input(), 16)

for i in range(1, 16):
    print('%X*%X=%X' % (data_integer, i, data_integer * i))