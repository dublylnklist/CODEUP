# 1
data_month = int(input())

def WeatherIs(m):
    print(
        {12: "winter", 1: "winter", 2: "winter", 3: "spring",
        4: "spring", 5: "spring", 6: "summer", 7: "summer", 8: "summer",
        9: "fall", 10: "fall", 11: "fall"}.get(m, "none")
    )

WeatherIs(data_month)

# 2
data_month_2 = int(input())

if data_month_2 in (12, 1, 2):
    print("winter")
elif data_month_2 in (3, 4, 5):
    print("spring")
elif data_month_2 in (6, 7, 8):
    print("summer")
elif data_month_2 in (9, 10, 11):
    print("fall")
else:
    print("none")

'''
python 에는 switch 가 없다고 한다. 그 때문에 dictionary 와 if 를 사용했는데
if ~ in 을 switch 처럼 # 2 와 같이 이용하는 방법도 있다.
'''