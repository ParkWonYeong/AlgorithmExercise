## 2178

# 1이 지나갈 수 있는 곳, 0은 지나갈 수 없는 곳
# bfs 탐색을 이용한다.

from collections import deque
import sys
input = sys.stdin.readline

def bfs(x,y):
    queue = deque()          # queue 방식 사용
    queue.append((x,y))
    visited[0][0] = 1

    while queue:
        x,y = queue.popleft()

        if x == N-1 and y == M-1:   # 최종경로에 도착했을 경우
            print(visited[x][y])
            break

        for i in range(4):  # 상하좌우 탐색
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < N and 0 <= ny < M: #nx와 ny가 모두 0보다 크고 M,N보다는 작을때
                if visited[nx][ny] == 0 and graph[nx][ny] == '1':   # 방문하지 않은 곳으면
                    visited[nx][ny] = visited[x][y] + 1 # 지나간 경로를 count해준다.
                    queue.append((nx, ny))

# main
N,M = map(int, input().split())     # 가로크기 N, 세로크기 M
graph = [list(input().rstrip()) for _ in range(N)]
visited = [[0]*M for _ in range(N)] # 방문경로 배열

dx = [-1,1,0,0]
dy = [0,0,-1,1]

bfs(0,0)