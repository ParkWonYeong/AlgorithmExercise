## 13305

import sys
n = int(sys.stdin.readline())

# 거리
distance = list(map(int, sys.stdin.readline().split()))
# 리터당 주유비
cost = list(map(int, sys.stdin.readline().split()))

total = distance[0]*cost[0]     # 맨 처음 최소한 다음까지 가야하는 주유를 하고 시작한다.
d = sum(distance)-distance[0]   # 처음 채운 주유 거리는 제외하고 남은 거리를 구한다.
cost.pop()                      # 목적지에서 채우는 것은 맞지 않으므로 마지막 값을 pop
total += d*min(cost)            # 나머지 최소 주유값을 더해준다

# 잉?! 틀렸는데 알고리즘 구현 과정에서 어디에서 틀린지는 잘 모르겠다..
# 아무튼 for문으로 min값을 찾아서 구현하는 방법으로 다시 시도.

import sys
n = int(sys.stdin.readline())

# 거리
distance = list(map(int, sys.stdin.readline().split()))
# 리터당 주유비
cost = list(map(int, sys.stdin.readline().split()))

mincost = cost[0]               # 맨 처음 주유소 가격으로 시작
total = 0
for i in range(n-1):
    if mincost <= cost[i]:      # 기존의 값이 다음 도시에서도 더 작으면
        total += mincost*distance[i]
    else:
        mincost = cost[i]       # 그렇지 않으면 mincost 값을 갱신
        total += mincost*distance[i]

print(total)