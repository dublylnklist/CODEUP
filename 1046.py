data_integer_a, data_integer_b, data_integer_c = map(int, input().split())

# 1
print(
    data_integer_a + data_integer_b + data_integer_c,
    '%.1f' % ((data_integer_a + data_integer_b + data_integer_c) / 3),
    sep = '\n'
)

# 2
'''
원하는 만큼 입력 받은 다음 그 수를 전부 더한 값, 그리고 그 평균을 나타내는 방법을
생각해보다가 작성했다. sum(data_integer_mapped) 를 print 에서 두번 사용하니깐
두번째에서 제대로 작동하지 않았다. 그래서 data_integer_sum 에 저장해서 사용했다.
'''
data_integer = input().split()
data_integer_mapped = map(int, data_integer)
data_integer_sum = sum(data_integer_mapped)

print(
    data_integer_sum,
    '%.1f' % (data_integer_sum / len(data_integer)),
    sep = '\n'
)