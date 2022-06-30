## 미로탈출


# import sys
# sys.setrecursionlimit(10**6)    # 재귀 깊이 한계치
# input = sys.stdin.readline

# def dfs(x,y):
#     global cnt

#     while not (x==n and y==m):

#         if (x<0 or x>=n or y<0 or y>=m) or maze[x][y] == '0':
#             continue

#         if maze[x][y] == '1':
#             maze[x][y] == '0'   # 방문 표시
#             cnt += 1
#             # 상하좌우 확인
#             dfs(x,y-1)
#             dfs(x,y+1)
#             dfs(x-1,y)
#             dfs(x+1,y)

#     cnt += 1        # 마지막칸도 포함해서 계산


# n,m = map(int, input().split())
# cnt = 1                 # 시작칸 포함해서 계산
# maze = []               # NxM 2차원 배열의 미로
# for _ in range(n):
#     maze.append(list(input()))

# dfs(0,0)
# print(cnt)


## bfs ##
# bfs는 queue를 이용한다.

from collections import deque

def bfs(maze):
    # global cnt
    # cnt = 1
    # cnt를 출력하면 완탐이라 최단거리가 아닌 1인 곳을 전부 방문하는 수가 나온다.
    # 따라서 cnt를 이용한 계산 출력 대신 누적합을 구하기로 했다.
    x,y = 0,0     # 배열 0,0 에서 시작, 시작칸 포함
    maze[x][y] = 1
    q = deque()
    q.append((x,y))

    # 모두 pop되어서 queue에 아무것도 없을 때까지 반복문        
    while q:
        x,y = q.popleft()
        # 상하좌우 탐색
        for i in range(4):
            print('i=', i)
            nx = x+dx[i]
            ny = y+dy[i]
            print('nx,ny = ', nx+1,ny+1)
            
            # 공간을 벗어나거나 괴물이 존재/방문한 곳일 때
            if (nx<0 or nx>=n or ny<0 or ny>=m) or maze[nx][ny]==0:
                print('pass')
                continue

            # 처음 방문하는 곳일 때
            if maze[nx][ny] == 1:
                print('first visit')
                maze[nx][ny] = maze[x][y] + 1     # 누적 합
                # cnt += 1
                q.append((nx,ny))

    # print(maze)
    # print(maze[n-1][m-1])


## main ##
# global cnt

n,m = map(int, input().split())

maze = []
for _ in range(n):
    maze.append(list(map(int, input())))

dx = [0,1,0,-1]
dy = [1,0,-1,0]

bfs(maze)