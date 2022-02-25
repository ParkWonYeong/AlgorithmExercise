## 2468

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())    # 2차원 배열의 행열 개수를 나타내는 수 N

# 위의 줄(append 제외)은 다음과 같이 작성할 수도 있다.
r = [list(map(int, input().split())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(val,j,k):
    q = deque()
    q.append((j,k))
    visit[j][k] = 1

    while q:
        x,y = q.popleft()

        # 상하좌우 탐색
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            # 자신이 건너갈 nx, ny에 대한 유효성을 먼저 확인한다.
            if 0<=nx<n and 0<=ny<n:
                if r[nx][ny]>val and visit[nx][ny]==0:
                    visit[nx][ny] = 1
                    q.append((nx,ny))

answer = 0
# 물에 잠기는 영역을 sink로 두고
for i in range(max(map(max, r))):  # 높이는 100까지 있으므로 0부터 100까지 검사한다.
    visit = [[0]*n for _ in range(n)]    # 매 높이마다 측정하므로 반복문 안에 넣어준다
    cnt = 0    
    # 입력 받은 배열을 탐색한다.
    for j in range(n):
        for k in range(n):
            if r[j][k] > i and visit[j][k]==0:   # 물에 잠기지 않은 경우
                bfs(i,j,k)
                cnt += 1
    answer = max(answer, cnt)   # 물에 잠기지 않은 최대값을 구한다.
print(answer)

# 32412KB, 1548ms