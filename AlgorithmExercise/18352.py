## 특정 거리의 도시 찾기
# bfs

import sys
from collections import deque

input = sys.stdin.readline

n,m,k,x = map(int, input().split())

graph = [[] for _ in range(n+1)]    # 인덱스 = 도시 번호

# 노드 연결(단방향)
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)      # 단방향이므로 a->b만 연결.

dist = [-1]*(n+1)           # 방문 여부도 계산하기 위해 -1
dist[x] = 0                 # x = 시작점인 부분이므로 0

queue = deque([x])
while queue:
    node = queue.popleft()
    # 노드 탐색
    for i in graph[node]:
        if dist[i] == -1:       # 최단거리를 구해야하므로 방문 최초시(-1)에만.
            dist[i] = dist[node]+1      # 거리 계산한 값 갱신(+1은 방문)
            queue.append(i)
    

# 최단거리 k인 도시 찾기
exist = False
for city, d in enumerate(dist):
    if d == k:               # x 도시로부터 거리 k인 도시가 있으면
        print(city)
        exist = True

# 위의 for문을 다 돌고나서도 해당하는 도시가 존재하지 않는 경우    
if exist == False:
    print(-1)

# 최단경로 알고리즘이므로 우선순위 큐(heapq) 활용도 가능.