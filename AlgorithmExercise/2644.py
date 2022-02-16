## 2644
# 여러 사람들에 대한 부모 자식들 간의 관계가 주어졌을 때, 주어진 두 사람의 촌수를 계산하라.

from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

# 그래프를 탐색하며 현재 탐색중인 노드와 연결된 노드에 현재 노드값의 +1을 한다.(연결된 노드를 이동시킨다.)
def bfs(n):
    queue = deque()
    queue.append(n)
    visit[n] = 1

    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if visit[i] == 0:   # 방문하지 않은 곳이면
                visit[i] = 1    # 방문 표시를 해주고
                result[i] = result[x]+1  # 촌수를 +1 해준다.
                queue.append(i)

n = int(input())    # 전체 사람의 수 n
a,b = map(int, input().split())  # 촌수를 계산해야하는 서로 다른 두 사람의 번호
m = int(input())    # 부모와 자식간의 관계의 개수 m

graph = [[] for _ in range(n+1)]
result = [0 for _ in range(n+1)]
visit = [0 for _ in range(n+1)]

# 부모 자식간의 관계를 나타내는 두 번호 x,y가 각 줄에 나온다.
# 앞에 나오는 번호 x는 뒤에 나오는 정수 y의 부모 번호
for _ in range(m):
    x,y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

bfs(b)  # 여기에 a를 넣고 result[b]를 계산하든, b를 넣고 result[a]를 계산하든 답은 동일하게 나옴.
print(result[a] if result[a] != 0 else -1)  # 친척관계가 없어 촌수를 계산할 수 없다면(result[b]가 0) -1을 출력한다.

# 32396KB, 92ms