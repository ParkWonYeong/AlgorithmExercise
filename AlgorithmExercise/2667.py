## 2667

from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(a,b):
    num = len(graph)
    queue = deque()
    queue.append((a,b))
    graph[a][b] = 0   # 방문한 곳은 0으로 만들어 재탐색하지 않도록 한다.
    count = 1
    
    while queue:
        x,y = queue.popleft()
        for i in range(4):  #상하좌우 탐색
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<num and 0<=ny<num:
                if graph[nx][ny]==1:    # 집이 존재하는 경우
                    graph[nx][ny] = 0
                    queue.append((nx,ny))
                    count += 1
    return count

n = int(input())
graph = []
block = []
# 공백없이 출력되므로 split()없이 append.
for _ in range(n):
    graph.append(list(map(int, input())))   # 아래의 반복문 안에 넣지 않고 따로 반복문을 돌린다.

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:                # 그래프 내에 집이 존재할 때
            block.append(bfs(i,j))          # bfs 함수를 이용하고 그 count값을 append한다.

block.sort()        # 오름차순 정렬
print(len(block))   # 총 단지 수를 출력한다.
for i in block:
    print(i)        # 오름차순으로 정렬된 각 단지내 집의 수를 하나씩 출력한다.

# 32420KB, 84ms