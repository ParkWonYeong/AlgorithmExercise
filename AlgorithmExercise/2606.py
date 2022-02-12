## 2606

import sys
input = sys.stdin.readline
dic = {}                # {1:{x,y}}

def dfs(x, dic):
    for i in dic[x]:
        if i not in visited:    # 방문하지 않은 노드인 경우
            visited.append(i)   # visited 인덱스에 넣어준다(방문표시)
            dfs(i, dic)

# 컴퓨터 수
N = int(input())

# 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수
L = int(input())

# 이어진 노드들을 dictionary 형태로 값을 받아준다.
# '감염된 컴퓨터 수'를 출력해야하므로 시작이 되는 1번 컴퓨터는 제외시킨다.
for i in range(N):
    dic[i+1] = set()    # 인덱스는 0부터 시작이므로 번호에 맞춰 +1을 해준다.

for j in range(L):
    x,y = map(int, input().split())
    dic[x].add(y)   # 양방향 성질(이어진 노드를 연결해준다)
    dic[y].add(x)

visited = []    # [1,2,3,5,6]
dfs(1, dic)     # 1번과 연결된 모든 노드를 탐색한다.
print(len(visited)-1)   # 감염된 컴퓨터 수이므로 1번 컴퓨터 제외

# 30860KB, 68ms