dice_a, dice_b = map(int, input().split())

for i in range(1, dice_a+1):
    for j in range(1, dice_b+1):
        print('{0} {1}'.format(i, j))

'''
range(0, 10): 1 부터 10 미만 즉 끝 숫자는 포함되지 않음
'''