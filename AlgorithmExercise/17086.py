## 17086

# 이동은 인접한 8방향(동서남북 대각4)이 가능하다.
# bfs 탐색을 이용한다.

from collections import deque
import sys
input = sys.stdin.readline

# 상/하/좌/우/대각선4
dx = [1,-1,0,0,1,-1,1,-1]
dy = [0,0,1,-1,1,-1,-1,1]

def bfs():
    while queue:
        x,y = queue.popleft()
        
        for i in range(8):  # 상/하/좌/우/대각선4
            nx = x+dx[i]
            ny = y+dy[i]
            # 범위 내에 있고 탐색되지 않은 곳일 경우 탐색한다
            if 0<=nx<n and 0<=ny<m:
                if visit[nx][ny]==0:
                    visit[nx][ny] = visit[x][y]+1 # 탐색까지 걸린 이동횟수를 체크(이동거리를 누적하여 더해준다)
                    queue.append((nx,ny))

### main ###

n,m = map(int, input().split())     # 공간의 크기 N,M

visit=[]
queue = deque()
for i in range(n):                  # 공간의 상태 정보값을 append한다.
    graph = list(map(int, input().split()))
    for j in range(m):
        if graph[j]==1:             # 아기상어가 있는 칸(1)일 경우
            queue.append((i,j))
    visit.append(graph)

bfs()

distance = 0
for i in range(n):
    for j in range(m):
        distance = max(distance, visit[i][j])   # 이동거리의 최대값을 구한다.

print(distance-1)   # 처음 시작값은 뺀다.