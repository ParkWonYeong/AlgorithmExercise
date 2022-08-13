## 11404
## 플로이드

# 한번 사용할때 필요한 비용이 있음
# 모든 도시의 쌍에 대해 도시 A->B로 가는데 필요한 비용의 최솟값

import sys
input = sys.stdin.readline
INF = int(1e9)


city = int(input()) # 도시의 개수 n
bus = int(input())  # 버스의 개수 m


# 정답 출력할 3차원 리스트 만들고 모든 값을 무한으로 초기화.
cost = [[INF]*(city+1) for _ in range(city+1)]

# 현 위치에서 현 위치로 동일한 비용은 0으로 초기화
for i in range(1, city+1):
    for j in range(1, city+1):
        if i == j:
            cost[i][j] = 0

# 각 간선 정보받기
for _ in range(bus):
    # A->B 비용 C
    a,b,c = map(int, input().split())
    # 동일한 노선 중 작은 비용 선택
    cost[a][b] = min(c, cost[a][b])

## 플로이드 워셜 알고리즘 ##
for k in range(1, city+1):
    for i in range(1, city+1):
        for j in range(1, city+1):
            cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])

# 출력
for i in range(1, city+1):
    for j in range(1, city+1):
        # 도달할 수 없으면 0 출력(조건-시작도시와 도착도시를 연결하는 노선은 하나가 아닐 수 있음)
        if cost[i][j] == INF:
            print(0, end=' ')
        else:
            print(cost[i][j], end=' ')
    print()