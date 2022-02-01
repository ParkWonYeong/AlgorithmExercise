## 1260

# 그래프를 DFS(깊이우선)로 탐색한 결과와 BFS(넓이우선)로 탐색한 결과를 출력하는 프로그램
# 정점 개수, 간선 개수, 탐색을 시작할 정점의 번호 N,M,V가 주어진다.
# 깊이 우선으로 탐색할 땐 함수 안에서 재귀를 해 찾아가는 경우가 많고
# 넒이 우선으로 탐색할 땐 큐나 데크에 저장을 하고 반복을 돌며 찾아가는 경우가 많다

from collections import deque
import sys

def dfs(x, visit=[]):
    # dfs 함수 내에서 visit=[]을 선언할 경우 런타임 에러가 발생했다.
    visit.append(x)
    print(x, end = ' ')

    for i in range(len(graph[x])):
        if graph[x][i] == 1 and (i not in visit):
            dfs(i, visit)

def bfs(x):
    visit=[x]
    queue = deque()    # 리스트를 써서 pop(0)하게 되면 시간복잡도가 0(N)이므로 0(1)인 deque를 사용.
    queue.append(x)

    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        
        for i in range(len(graph[x])):
            if graph[v][i] == 1 and (i not in visit):
                visit.append(i)
                queue.append(i)

# bfs에서 visit=[x]로 설정해주지 않자 무한루프를 돌아 출력 초과가 되는 문제점이 발생했다.
# 따라서 visit이라는 변수를 선언하여 이용했다.

# main
N,M,V=map(int, sys.stdin.readline().split())

# N개의 숫자가 있으므로 0으로 채워진 N+1 x N+1 의 행렬을 리스트를 통해 만든다.
# 인덱스와 값을 일치시키기 위해 N+1개의 숫자를 사용한다.
graph = [[0]*(N+1) for _ in range(N+1)]

for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    # 노드를 연결해준다.
    # 연결된 숫자의 값을 입력받아 해당되는 행과 열의 값을 1로 바꿔준다
    graph[x][y] = graph[y][x] = 1

dfs(V)
print()
bfs(V)