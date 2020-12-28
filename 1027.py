data_date_year, data_date_month, data_date_day = input().split('.')

print('{0:02d}-{1:02d}-{2:04d}'.format(int(data_date_day), int(data_date_month), int(data_date_year)))

'''
format은 year, month, day 순으로 두고 순서는 2, 1, 0 순으로 바꾸고
자릿수도 바꿔줬는데 코드업에서는 잘못된 풀이로 출력 됐다. VS CODE에서는 원하는 값이 제대로 출력되는데
코드업에서는 다른 값이 출력되는 모양이다.
'''