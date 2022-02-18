## 7569

# 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익는다.
# 하나의 토마토에 인접한 곳은 위, 아래, 왼쪽, 오른쪽, 앞, 뒤 여섯방향의 토마토를 의미한다.

# 며칠이 지나면 토마토들이 모두 익는지, 그 최소 일수를 구하는 프로그램을 작성하라.

from collections import deque
import sys
input = sys.stdin.readline

m,n,h = map(int, input().split())   # 가로 칸, 세로 칸, 쌓아올려지는 상자 수

graph = []
queue = deque([])
day = 0

# 토마토에 대한 정보 N개의 줄이 H번 반복하여 주어진다.
for i in range(h):
    tomato = []
    for j in range(n):
        tomato.append(list(map(int, input().split())))
        for k in range(m):
            if tomato[j][k]==1:
                queue.append([i,j,k])
    # 2차원 배열인 tomato를 graph에 추가하면서 3차원 배열로 만든다.
    graph.append(tomato)

# 3차원 방향 설정
dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

# 1 = 익은 토마토, 0 = 익지 않은 토마토, -1 = 토마토 없음
def bfs():
    while queue:
        x,y,z = queue.popleft()

        for i in range(6):  # 상하좌우, 위아래 탐색
            nx = x+dx[i]
            ny = y+dy[i]
            nz = z+dz[i]
            if 0<=nx<h and 0<=ny<n and 0<=nz<m and graph[nx][ny][nz]==0:
                # 비교한 토마토에 기존토마토 +1을 하여 하루가 지나는 것을 표현한다.
                graph[nx][ny][nz] = graph[x][y][z] + 1
                queue.append([nx, ny, nz])

bfs()

for i in graph:
    for j in i:
        for k in j:
            # bfs 함수 내의 while문을 거쳤음에도 0이 있을 경우는 토마토가 익지 못하는 상황이다.
            if k == 0:
                print(-1)   # 따라서 -1을 출력한다.
                exit()
        day = max(day, max(j))

# 처음부터 익어있던 토마토가 있으므로 시작점이 1이기 때문에 day-1을 한다.
print(day-1)

# 50888KB, 3192ms