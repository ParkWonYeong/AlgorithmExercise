## 볼링공 고르기

n,m = map(int, input().split()) # n: 볼링공 개수 / m: 볼링공 최대무게
weight = list(map(int, input().split()))
ans = 0

# 이중반복문으로 비교
for i in range(n):
    for j in range(i,n):
        if weight[i] != weight[j]:
            ans += 1

print(ans)


### 볼링공 고르기(2회독)

import sys
input = sys.stdin.readline

n,m = map(int, input().split())
wgt = list(map(int, input().split()))
ans = 0
for i in range(n):
    for j in range(i,n):
        # i와 j의 무게가 다를 때만 경우의 수로 추가
        if wgt[i] != wgt[j]:
            ans += 1

print(ans)