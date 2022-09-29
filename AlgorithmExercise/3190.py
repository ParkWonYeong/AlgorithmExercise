## 뱀

# 사과를 먹으면 뱀 길이가 늘어난다.
# 시작 시 뱀은 맨위 좌측에 위치하고 뱀 길이는 1, 처음에 오른쪽을 향한다.

# 칸에 사과가 있다면 그 칸에 있던 사과가 없어지고 꼬리는 안움직임
# 사과가 없다면 몸길이를 줄여 꼬리가 위치한 칸을 비워줌

import sys
input = sys.stdin.readline

n = int(input())    # 보드의 크기 NxN
cnt = 0

board = [[0]*(n+1) for _ in range(n+1)]
rotate = []

# 사과의 개수 K(0<=K<=100)와 위치 정보
for k in range(int(input())):
    x,y = map(int, input().split())
    board[x][y] = 1

# 처음은 오른쪽을 바라보고 있으므로 그 기준으로 동남서북(시계방향)
dx = [0,1,0,-1]     # 그래프 상하 이동
dy = [1,0,-1,0]     # 그래프 좌우 이동

# 뱀의 방향 회전 정보 L(1<=L<=100)
for l in range(int(input())):
    # X초 후 왼쪽(L) 또는 오른쪽(D)으로 방향 회전
    x,c = input().split()
    rotate.append([int(x),c])


### 초기값 설정 ###
x,y = 1,1           # 뱀 머리의 위치
board[x][y] = 2     # 뱀이 차지하는 칸을 2로 설정
direction = 0       # 처음 방향(오른쪽, 즉 동쪽)
time = 0
next_direction = 0
body = [(x,y)]      # 뱀이 차지한 칸의 위치 정보(사과를 먹을수록 증가)

while True:
    nx = x+dx[direction]
    ny = y+dy[direction]

    # 그래프 범위 내에서, 자기자신의 몸이 닿지 않는 영역으로 이동하는 경우
    if (1<=nx and nx<=n and 1<=ny and ny<=n) and board[nx][ny] != 2:
        
        if board[nx][ny] == 0:  # 사과 없는 경우 - 이동
            board[nx][ny] = 2
            body.append((nx,ny))
            tx,ty = body.pop(0)     # 꼬리 제거
            board[tx][ty] = 0       # 제거했으므로 빈칸으로 갱신

        if board[nx][ny] == 1:  # 사과 있는 경우
            board[nx][ny] = 2   # 사과 제거하고 뱀 머리 추가
            body.append((nx,ny))

        # print(body)

    # 자기 자신의 몸 또는 벽에 부딪힌 경우(게임 종료)
    else:
        time += 1
        break
    
    x,y = nx,ny     # 뱀 머리 위치 갱신
    time += 1
    if next_direction <= l and time == rotate[next_direction][0]:

        if rotate[next_direction][1] == 'L':    # 왼쪽
            direction = (direction-1) % 4
        else:                                   # 오른쪽
            direction = (direction+1) % 4

        next_direction += 1

print(time)