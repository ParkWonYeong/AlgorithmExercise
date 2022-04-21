## 5622

import sys
input = sys.stdin.readline

num = list(map(str, input()))
sum = 0
for i in range(len(num)-1):
    if num[i] == '1':       # 1번
        sum += 2
    elif num[i] in 'ABC':   # 2번
        sum += 3
    elif num[i] in 'DEF':   # 3번
        sum += 4
    elif num[i] in 'GHI':   # 4번
        sum += 5
    elif num[i] in 'JKL':   # 5번
        sum += 6
    elif num[i] in 'MNO':   # 6번
        sum += 7
    elif num[i] in 'PQRS':  # 7번
        sum += 8
    elif num[i] in 'TUV':   # 8번
        sum += 9
    elif num[i] in 'WXYZ':  # 9번
        sum += 10
    else:                   # 0번
        sum += 11

print(sum)

# 30840KB, 72ms