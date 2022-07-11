## 미래도시

# 1번부터 N번까지의 회사. 특정 회사끼리는 서로 도로로 연결됨.
# 회사끼리 연결된 도로를 이용하여 1만큼의 시간으로 양방향으로 이동 가능.

# K번 회사에서 소개팅 -> X번 회사에서 방문판매
# 1번 회사에서 출발하여 K번 회사 방문 후 X번 회사로 이동.(최소시간)
# 만약 X번 회사에 도달할 수 없다면 -1 출력

# bfs로 풀어보려고 했으나 도중에 거치는 곳이 있기 때문에,
# 완전 탐색이 끝난 시점에서 다시 돌아가야 하는 경우 어려움이 있다.


import sys
input = sys.stdin.readline

INF = int(1e9)      # 무한(10억)

# n: 회사 개수 / m: 경로 개수
n,m = map(int, input().split())

time = [[INF]*(n+1) for _ in range(n+1)]

# 양방향 간선 추가
for _ in range(m):
    t,s = map(int, input().split())
    time[t][s] = 1
    time[s][t] = 1

x,k = map(int, input().split())     # K 회사 방문 후 X 회사

# 같은 위치에서는 이동시간 0
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            time[a][b] = 0


# 최단 경로 계산
for i in range(1, n+1):         # 거쳐야하는 경우
    for j in range(1, n+1):     # 목표지점
        for l in range(1, n+1): # 현재위치
            time[j][l] = min(time[j][l], time[j][i]+time[i][l])

# 1 -> k
from_1_to_k = time[1][k]

# k -> x
from_k_to_x = time[k][x]

## answer
ans = from_1_to_k + from_k_to_x
if ans >= INF:
    print(-1)
else:
    print(ans)