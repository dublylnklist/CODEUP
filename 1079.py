# 1
data_character = ''

while data_character != 'q':
    data_character = input()
    print('%s' % data_character, sep='\n')

# 2
data_character_2 = input().split()
for i in data_character_2:
    print(i)
    if i == 'q':
        break

'''
c++ 풀이 처럼 한 개씩 입력을 받고 q 의 여부를 검사해서 q 가 입력될 때까지 계속 입력을 받는
형태로 작성을 하려고 했으나 오류가 출력 돼서 # 2 와 같이 풀이를 했다.
'''