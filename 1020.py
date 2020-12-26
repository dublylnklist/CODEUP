nFirstNumber, nLastNumber = input().split('-')

# 주민등록번호에 맞게 정수로 캐스팅
nFirstNumber = int(nFirstNumber)
nLastNumber = int(nLastNumber)

# 앞자리가 0인 경우 생략 돼 출력되므로 자릿수를 미리 정해줘야 한다.
print('%06d%07d' % (nFirstNumber, nLastNumber))