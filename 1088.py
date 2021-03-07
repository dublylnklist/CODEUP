'''
다시 보니 파이썬 기초 100제가 따로 분리 됐는지 파일명과 분류가 달라져서 기존대로 업로드하기로 했다.
'''

data_num = int(input())
data_start_num = 1

for i in range(data_start_num, data_num+1):
    if data_start_num % 3 != 0:
        print(data_start_num, end=' ')
        data_start_num += 1
    else:
        data_start_num += 1