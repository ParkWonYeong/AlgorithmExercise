## 게임개발

import sys
input = sys.stdin.readline

n,m = map(int, input().split())
x,y,d = map(int, input().split())   # 좌표,방향

# 게임 전체 맵 정보(0 육지, 1 바다)
game = []
for _ in range(n):
    game.append(list(map(int, input().split())))

# N, E, S, W
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

game[x][y] = '1'         # 현재 위치를 방문한 것으로(바다로) 친다
cnt = 1
turn = 0

while True:
    d -= 1
    if d < 0:
        d = 3
    nx = x+dx[d]
    ny = y+dy[d]

    # 방문한 적 없는 칸이 존재하면 이동
    if game[nx][ny] == 0:
        game[nx][ny] = 1
        x,y = nx,ny
        cnt += 1
        turn = 0
        continue
    else:
        turn += 1

    if turn == 4:       # 네 방향 모두 가지 못함
        nx = x-dx[d]
        ny = y-dy[d]
        if game[nx][ny] == 0:    # 뒤로가기 가능할 때
            x,y = nx,ny
        else:                   # 뒤로가기 X
            break               # 움직임을 멈춘다
        turn = 0

print(cnt)