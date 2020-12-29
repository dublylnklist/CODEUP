data_integer = int(input(), 16)

# 1
print('{:o}' .format(data_integer))

# 2
print('%o' % data_integer)

# 3
print('%#o' % data_integer)

'''
format 을 이용한 방법과 %o 를 이용한 방법을 모두 사용해보았다.
o 앞에 # 을 붙이면 접두어 그러니까 8 진수의 경우 0o25 를 붙일 수 있다.
#1 과 #2 의 모두의 경우에서 가능하다.
'''

