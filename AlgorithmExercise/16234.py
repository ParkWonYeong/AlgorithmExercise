## 인구 이동

# dfs.bfs

# 땅 크기 NxN
# L<=(두 나라 인구차이)<=R : 두 나라가 공유하는 국경선을 오늘 하루동안 연다
# 국경선이 열려 인접한 칸만을 이용해 이동 가능하면 오늘 하루동안은 "연합"
# 연합 이루는 각 칸의 인구수 = (연합 인구수)/(연합 이루는 칸 개수). 소수점 버림
# 연합 해채 후 모든 국경선 닫기

import sys
from collections import deque
input = sys.stdin.readline


# 특정 지점에서 출발 -> 연합 체크 -> 그래프 갱신
def process(x,y,index):
    united=[]   # x,y 위치와 연결된 나라 정보
    united.append((x,y))

    q = deque()
    q.append((x,y))
    union[x][y] = index # 현재 연합의 번호 할당
    summary = graph[x][y]   # 현재 연합 전체 인구 수
    count = 1               # 현재 연합 수

    # bfs
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<y and union[nx][ny]==-1:
                # 옆나라와 인구 차가 L명 이상 R명 이하일 경우 국경선 연결
                if l <= abs(graph[nx][ny]-graph[x][y]) <= r:
                    q.append((nx,ny))
                    # 연합 추가
                    union[nx][ny] = index
                    summary += graph[nx][ny]
                    count += 1
                    united.append((nx,ny))

    for i,j in united:
        graph[i][j] = summary//count    # 소수점 제외

    return count


### main ###

n,l,r = map(int, input().split())   # N,L,R

# 전체 나라 정보
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1,0,1,0]
dy = [0,-1,0,1]

result = 0
total_count = 0

# 인구 이동 없을 때까지 반복
while 1:
    union = [[-1]*n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:   # 아직 확인하지 않은 나라
                process(i,j,index)
                index += 1

    if index == n*n:
        break
    total_count += 1

print(total_count)