## 10867.py

import sys
input=sys.stdin.readline

N = int(input())

num = list(map(int, input().split()))

num=list(set(num))
num.sort()

for i in range(len(num)):
    print(num[i], end=' ')