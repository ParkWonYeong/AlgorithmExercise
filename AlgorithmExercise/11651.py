## 11651

import sys
input = sys.stdin.readline

N = int(input())

dot=[]

for _ in range(N):
    dot.append(list(map(int, input().split())))

# 이번에는 우선순위가 y축, x축 순이다.
dot.sort(key=lambda x: (x[1],x[0]))

for i in range(N):
    print(dot[i][0], dot[i][1])
