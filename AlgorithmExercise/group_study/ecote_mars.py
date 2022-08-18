## 화성탐사

import heapq
import sys
input = sys.stdin.readline

t = int(input())    # 테스트케이스 수
INF = int(1e9)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


for _ in range(t):
    cost = []    
    n = int(input())    # 테스트 케이스마다 주어지는 탐사 공간의 크기(NxN)
    for _ in range(n):
        cost.append(list(map(int, input().split())))

dist = [[INF]*n for _ in range(n)]

x,y = 0,0   # 초기 위치

# 시작 노드로 가는 비용 = (0,0) 위치 값으로 설정
q = [(cost[x][y], x, y)]    # 초기(시작노드) 값
dist[x][y] = cost[x][y]

while q:
    d, x, y = heapq.heappop(q)

    #  이미 처리됐으면 무시
    if dist[x][y] < d:
        continue
    # 다른 인접 노드 확인
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if nx<0 or nx>=n or ny<0 or ny>=n:
            continue

        c = d + cost[nx][ny]

        # 현재 노드를 거쳐 다른 노드로 이동하는 거리가 더 가까울 때
        if c < dist[nx][ny]:
            dist[nx][ny] = c
            heapq.heappush(q, (c, nx, ny))  # 큐에 삽입

print(dist[n-1][n-1])