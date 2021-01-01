data_integer = int(input(), 8)

print(data_integer)

'''
1. oct(), hex(), bin() 함수가 있지만 10진수를 8, 16, 2 진수 `문자열` 로 변환한다.
즉, int 로 캐스팅 해야한다. 문자열을 정수형으로 변환할 때int() 함수의 두번째 인자를 사용할 수 있다.
int(8진수, 8), int(16진수, 16), int(2진수, 2)

2. format()을 이용한 10, 8, 16, 2 진수 출력 방법도 있다.
print('{:#o}'.format(10진수)), print('{:#x}'.format(10진수)), print('{:#b}'.format(10진수))

참고: https://withcoding.com/70
'''