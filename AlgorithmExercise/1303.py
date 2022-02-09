## 1303

# 우리는 백군, 적은 청군
# 같은 팀의 병사들은 모이면 모일수록 강해진다(N명이 뭉치면 N^2의 위력)
# 같은 팀이 대각선으로만 인접한 경우는 뭉쳐있다고 보지 않음

from collections import deque
import sys
input = sys.stdin.readline

# BFS 탐색을 이용한다.
def bfs(x,y,team):
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 'visited'    # 방문한 그래프 노드에는 'visited'를 넣는다.
    count = 0

    while queue:
        x,y = queue.popleft()   # 왼쪽부터 pop한다.
        for i in range(4):  # 상하좌우 탐색
            nx,ny = x+dx[i], y+dy[i]
            if 0 <= nx < M and 0 <= ny < N: # nx와 ny가 모두 0보다 크고 M, N보다는 작을때
                if graph[nx][ny] != 'visited' and graph[nx][ny] == team:    # 방문하지 않은 곳이면
                    graph[nx][ny] = 'visited'   # 방문했다는 표시를 해준다.
                    queue.append((nx,ny))
                    count += 1
    return count + 1
    
# 전쟁터의 가로 크기 N, 세로 크기 M
N,M = map(int, input().split())
graph = [list(input().strip()) for _ in range(M)]
W,B = 0,0

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(M):
    for j in range(N):
        if graph[i][j] != 'visited':
            if graph[i][j] == 'W':  # 우리팀(백군)인 경우
                W += bfs(i, j, 'W')**2
            else:                   # 다른팀(청군)인 경우
                B += bfs(i, j, 'B')**2
print(W,B)

# 32388KB, 104ms