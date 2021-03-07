'''
a = start number, d = interval number, n = sequence

* 등차수열의 일반항으로 해결하는 코드
a,d,n= map(int, input().split())
print(a + d * (n - 1))

'''

a, d, n = map(int, input().split())

for i in range(0, n-1):
    a += d
    
print(a)

