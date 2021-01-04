data_integer_a, data_integer_b, data_integer_c = map(int, input().split())

# 1 min() 함수 이용 (max() 도 있다고 한다)
print(min(data_integer_a, data_integer_b, data_integer_c))

# 2 그 때까지 연산된 결과를 이용해 다시 순서에 따라 하나씩 연산
data_integer_min = data_integer_a if data_integer_a < data_integer_b else data_integer_b
print(data_integer_min if data_integer_min < data_integer_c else data_integer_c)

# 3 순서에 따라 한 단계씩 실행
print(
    ((data_integer_a if data_integer_a < data_integer_c else data_integer_c)
    if data_integer_a < data_integer_b else
    (data_integer_b if data_integer_b < data_integer_c else data_integer_c))
)

'''
순서에 따라 한 단계씩 실행, 미리 정해진 순서에 따라 하나씩 연산 수행,
그 때까지 연산된 결과를 이용해 다시 순서에 따라 하나씩 연산 등 다양한 소스코드 작성 시의 접근법들이 있다.

* 가장 작은 수를 찾으려면 부등호를 작은 것 위주로 맞춰줘야 한다.
'''