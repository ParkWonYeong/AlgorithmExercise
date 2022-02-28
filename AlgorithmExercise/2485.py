## 2485

import math
import sys
input = sys.stdin.readline

n = int(input())
tree = []
for _ in range(n):
    tree.append(int(input()))

# 가로수 간의 거리(distance)
d = []
for i in range(n-1):
    d.append(tree[i+1]-tree[i])

# 공차를 간격들의 수에서 최대공약수를 사용하여 구한다.
# 최대공약수를 구하는 함수인 GCD를 이용한다.
common = d[0]
for i in d:
    common = math.gcd(common, i)

# 심는 전체 가로수(전체 수열의 길이) - 주어진 가로수 = 심어야 하는 최소한의 나무 수
ans = (max(tree)-min(tree))//common + 1 - len(tree)
print(ans)