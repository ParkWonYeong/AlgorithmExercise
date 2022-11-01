## ecote_Ch 4-1 상하좌우(구현)

# L: 왼, R: 오, U: 위, D:아래
N = int(input())    # 공간의 크기
place = list(map(str, input().split()))

h,w = 1,1           # h는 세로, w는 가로(h,w)
for i in place:
    if i == 'R':    # 오른쪽 이동
        if w+1 <= N:    w += 1
    elif i == 'L':  # 왼쪽 이동
        if w-1 >= 1:    w -= 1
    elif i == 'U':  # 위로 이동
        if h-1 >=1 :    h -= 1
    elif i == 'D':  # 아래로 이동
        if h+1 <= N:    h += 1

print(h, w)


##### 221102 복습 #####
## 상하좌우

import sys
input = sys.stdin.readline

n = int(input())        # NxN
move = list(input().split())
x,y = 1,1   # 초기 좌표 (1,1)

for i in move:
    if i == 'R' and y < n:
        y += 1
    elif i == 'L' and y > 1:
        y -= 1
    elif i == 'D' and x < n:
        x += 1
    elif i == 'U' and x > 1:
        x -= 1

print(x, y)


### 정석 코드

n = int(input())
x,y=1,1
plans = input().split()

# L,R,U,D에 따른 이동 방향
dx = [0,0,-1,1]
dy = [-1,1,0,0] # L,R,U,D 순
move_types = ['L', 'R', 'U', 'D']

# 이동계획 하나씩 확인
for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x+dx[i]
            ny = y+dy[i]
    # 공간 벗어나는 경우 무시
    if nx<1 or ny<1 or nx>n or ny>n:
        continue
    
    x,y = nx,ny

print(x, y)