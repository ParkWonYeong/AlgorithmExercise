## 1743

# 떨어진 음식물 중 제일 큰 음식물 구해 그것을 피한다.

import sys
from collections import deque
sys.setrecursionlimit(10**4)    # recursion limit 제한 설정

input = sys.stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(i,j,exist):
    queue = deque([[i,j]])
    exist[i][j] = 2     # 방문을 체크한다.
    count = 1           # 쓰레기 개수를 센다.

    while queue:
        x,y = queue.popleft()

        for i in range(4):  # 상하좌우 탐색
            nx, ny = x+dx[i], y+dy[i]
            if 0 < nx <= N and 0 < ny <= M and exist[nx][ny]==1:    # 0<nx<=M
                # 탐색할 좌표가 지도를 벗어나지 않고, 쓰레기가 있는 곳인데 탐색하지 않은 곳일 경우
                    queue.append((nx,ny))
                    exist[nx][ny] = 2
                    count += 1
    return count

# N: 통로 세로길이, M: 통로 가로길이, K: 음식물 쓰레기 개수
N,M,K = map(int, input().split())

# K개의 줄에 음식물이 떨어진 좌표(r,c)가 주어진다.
exist = [[0]*(M+1) for _ in range(N+1)]   # 음식물경로 배열
answer = 0

#쓰레기의 위치를 입력해준다
for _ in range(K):
    x,y = map(int, input().split())
    exist[x][y] = 1

for i in range(1, N+1):
    for j in range(1, M+1):
        if exist[i][j] == 1:
            ans = bfs(i,j,exist)    # 최대값을 도출한다.
            answer = max(ans, answer)

print(answer)

# 32428KB, 96ms