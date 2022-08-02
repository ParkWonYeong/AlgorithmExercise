## 18405
## 경쟁적 전염

# NxN 크기의 시험관
# 모든 바이러스는 1번부터 K번까지 바이러스 종류 중 하나
# 1초마다 상하좌우 방향으로 증식, 번호가 낮은 종류의 바이러스부터 먼저 증식

import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

ans = 0

def bfs(s, virus):
    global cnt_sec

    for i in range(4):  # 상하좌우 탐색
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<n and 0<=ny<n:
            if graph[nx][ny] == 0:  # 비어있는 경우에만
                return ###
    q = deque([])

    while q:

    

    #####
    #####

    return




### main ###

n,k = map(int, input().split()) # N: 시험관 크기, K: 바이러스 종류 수

# 시험관의 정보 받기
graph = [list(map(int, input().split())) for _ in range(n)]

# S, X, Y
s,x,y, = map(int, input().split())      # S: 초, X,Y: 각각 행과 열의 위치

cnt_sec = 0
# 바이러스 증식(너비 우선 탐색)
bfs(s, virus)