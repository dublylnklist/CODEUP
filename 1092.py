'''
1. 유클리드 호제법, 재귀함수를 통해 최대공약수(GCD)를 구한 다음
주어진 두 수를 곱해서 나눠주면 최소 공배수(LCM)를 구할 수 있다.
또, 주어진 수가 n개 이상일 때 먼저 두 수에 대한 GCD를 구하고
나머지 수와 다시 GCD를 구해 LCM을 구할 수 있다.
https://brownbears.tistory.com/454

2. 논리 연산자를 통해 구하는 방법도 있다.

'''

# 1. GCD 와 LCM

# 1-1. gcd 함수 원리
# 유클리드의 호제법을 그대로 코드에 구현한 것이다.
# x, y 를 나눈 나머지를 대입하고 x를 y에, 나머지를 y에 대입하는 것을 y가 0 이 될 때까지 반복한다.
# 반복문과 재귀문은 다음의 링크에서 확인할 수 있다.
# https://namu.wiki/w/%EC%9C%A0%ED%81%B4%EB%A6%AC%EB%93%9C%20%ED%98%B8%EC%A0%9C%EB%B2%95

def self_gcd(x, y):
    # y가 0이 될 때까지 반복
    while y:
        # y를 x에 대입
        # x를 y로 나눈 나머지 값을 y에 대입
        x, y = y, x % y
    return x

print(self_gcd(1071, 1029))

# 1-2. python 에서 지원하는 gcd 함수 이용

from math import gcd

print(gcd(1071, 1029))

# 1-3. lcm 함수 원리
# 유클리드 호제법을 이용함. 최대공약수 구한 다음 x, y를 곱한 값을 나눠주면 최소 공배수를 구할 수 있다.

def lcm(x, y):
    return x * y // gcd(x, y)

print(lcm(1071, 1029))

# 2. 1092 해결

# 2-1. 논리 연산자를 이용해서 해결
# 각각의 a, b, c 와 day 를 나눈 몫이 모두 0 이 될 때까지 day 를 진행 시키고
# 모두 0 이 되면 day 를 더 증가 시키지 않으면서 day 를 출력한다.
# 사실상 최소 공배수 구하는 것과 동일한 방법이다.

day = 1
a, b, c = 3, 7 , 9

while day%a != 0 or day%b != 0 or day%c != 0:
    day += 1

print(day)


# 2-2. gcd, lcm 을 이용해 해결하기 위해 여러 수를 입력 받아 그 수들의 GCD, LCM 을 구하는 함수 구현
# https://kimhaksung.tistory.com/entry/python3LCM

arr = list(map(int, input().rstrip().split())) # rstrip() : 문자열의 끝(보통은 NULL)을 삭제함

def GCDofTwoNumbers(arg_a, arg_b): # 입력 받은 수들 중 두 수의 GCD 를 구하는 함수
    while arg_b != 0: # arg_b 가 0 이 아닐 때까지 반복
        arg_a, arg_b = arg_b, arg_a%arg_b # #1의 원리와 동일하다.
    return arg_a # 두 인자의 GCD 반환

# 3, 3 의 최소 공배수가 3이 되듯 GCD, LCM 모두 자신 숫자가 그대로 나오는 경우 때문에
# 리스트 arr의 첫 항을 저장한다.
GCDarr = arr[0]
LCMarr = arr[0]

for i in range(len(arr)): # arr 의 길이만큼 반복
    GCDarr = GCDofTwoNumbers(LCMarr, arr[i]) # GCDarr 에 LCMarr, arr[i]의 최대 공약수를 저장
    LCMarr = LCMarr * arr[i] // GCDarr # 이전 수(LCMarr의 첫 항) 을 GCD 로 나눠서 LCM 을 구해 저장

print(LCMarr)