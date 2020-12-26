nHour, nMinute = input ().split(':') # input() 안에 있는 인자는 ' '인 경우 공백을, split 안의 인자 ':'는 구분자로 : 전후로 나눠서 입력을 받는다.

print('%d : %d' % (int(nHour), int(nMinute)))