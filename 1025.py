nInteger = input()
nCount = len(nInteger) - 1

for i in range(len(nInteger)): 
    print([int(nInteger[i] + '0' * nCount)])
    nCount -= 1