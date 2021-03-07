a, r, n = map(int, input().split())

for i in range(0, n-1):
    a *= r

print(a)