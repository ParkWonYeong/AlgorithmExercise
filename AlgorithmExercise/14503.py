### 로봇청소기
# 이코테 Ch4 게임 문제와 유사

# NxM 직사각형. 각각의 칸은 벽 또는 빈칸
# 청소기는 바라보는 방향이 있으며, 이 방향은 동서남북 중 하나
# r은 북쪽으로부터 떨어진 칸의 개수, c는 서쪽으로부터 떨어진 칸의 개수

# 1. 현재 위치 청소
# 2. 현재 방향 기준 왼쪽 방향부터 차례로 탐색 진행(북,서,남,동)
# 2-1. 청소하지 않은 공간 존재 시 그 방향으로 회전하고 다음 한 칸 전진 후 1 진행
# 2-2. 네 방향 모두 청소가 이미 되어있거나 벽이면, 바라보는 방향 유지한 채 한칸 후진
# 2-3. 네 방향 모두 청소가 이미 되어있거나 벽이고, 뒤쪽이 벽이라 후진도 못하면 작동 멈춤
# 이미 청소된 칸을 또 청소하지 않으며, 벽을 통과할 수 없음
# 지도 첫 행, 마지막 행, 첫 열, 마지막 열에 있는 모든 칸은 벽(테두리는 다 벽)

from collections import deque

# 세로 크기 N, 가로 크기 M(3<=N, M<=50)
n,m = map(int, input().split())
# 로봇청소기가 있는 칸의 좌표(r,c), 바라보는 방향(d)

r,c,d = map(int, input().split())
graph = [[] for _ in range(n)]

for i in range(n):
    graph[i] = list(map(int, input().split()))

graph[r][c] = 2 # 현재 로봇청소기 위치는 방문 처리.

# # 0북, 1동, 2남, 3서
dx = [-1,0,1,0]
dy = [0,1,0,-1]

# 왼쪽부터 차례로 회전하며 탐색
def turn_left():
    global d
    d -= 1
    if d == -1: # 범위 내 값(0~3)으로 설정
        d = 3

count = 1
turn_time = 0

while True:
    turn_left()
    nx = r+dx[d]
    ny = c+dy[d]
    
    # 회전 직후 가본 적 없는 칸이고 쓰레기 있는 곳이면 이동
    if graph[nx][ny] == 0:
        graph[nx][ny] = 2
        r,c = nx,ny
        count += 1
        turn_time = 0

    # 회전 직후 정면에 가보지 않은 칸이 없거나 벽일 때
    else:
        turn_time += 1
    
    # 네 방향 모두 못 가면
    if turn_time == 4:
        nx = r-dx[d]
        ny = c-dy[d]
        
        # 뒤로 갈 수 있으면 뒤로 이동
        if graph[nx][ny] != 1:
            r,c = nx,ny
        else:
            break
        
        turn_time = 0

print(count)