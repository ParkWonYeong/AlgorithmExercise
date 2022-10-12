## 알고리즘 수업 - 깊이 우선 탐색 1
# DFS 기본 개념 공부

import sys
sys.setrecursionlimit(10**6)

n,m,r = map(int, input().split())   # N: 정점의 수, M: 간선의 수, R: 시작 정점

nodes,visited = [[] for _ in range(n+1)], [0]*(n+1)

# 노드 간 연결
for _ in range(m):
    tail, head = map(int, sys.stdin.readline().split())
    nodes[tail].append(head)
    nodes[head].append(tail)

# 각각의 정점에서 방문할 수 있는 인접 정점을 오름차순으로 정렬
for i in range(n+1):
    nodes[i].sort()
# [], [2,4], [1,3,4], [2,4], [1,2,3], []
# print(nodes)

cnt = 1

def dfs(nodes, current_node, visited):
    
    global cnt
    visited[current_node] = cnt         # 방문시 방문 순서(cnt) 표시
    # print('visited[{}]={}'.format(current_node, cnt))

    # 연결 정점 방문하기
    for next_node in nodes[current_node]:   # 현재 정점에서 연결된 노드 중 오름차순으로 이동
        # 시작 정점의 방문 순서는 1이 되고 이후 계속 +1씩 증가하며 연결 정점에 추가
        # 연결된 정점 중 방문하지 않은 정점이 있으면 재귀
        if visited[next_node]==0:        
            cnt += 1
            dfs(nodes, next_node, visited)

dfs(nodes, r, visited)

for k in range(1, n+1):
    print(visited[k])

# 160268KB, 636ms
# PyPy3는 메모리 초과 발생.

# input
# 5 5 1
# 1 4
# 1 2
# 2 3
# 2 4
# 3 4

# output
# 1
# 2
# 3
# 4
# 0