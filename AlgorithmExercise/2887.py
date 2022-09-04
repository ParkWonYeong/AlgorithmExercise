## 행성 터널

import sys
input = sys.stdin.readline

def find(parent, x):
    # 루트 parent 찾을 때까지 재귀 호출
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

# 두 원소의 집합을 합친다.
def union(parent, x, y):
    x, y = find(parent, x), find(parent, y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y

### main ###

n = int(input())        # 행성의 개수 N
parent = [i for i in range(n+1)]

# 모든 행성을 연결하는데 필요한 최소 비용 구하기
# 다 연결된걸 가정하기 때문에 크루스칼에 쓰려면 간선을 새롭게 구성

x,y,z=[],[],[]      # x,y,z 좌표별로 리스트 구성 후 정렬

for i in range(m):
    a,b,c = map(int, input().split())
    x.append((a,i))
    y.append((b,i))
    z.append((c,i))

x.sort()
y.sort()
z.sort()

# 간선 재구성
load_info = []

for lst in x,y,z:
    for i in range(1, n):
        info1, a = lst[i-1]
        info2, b = lst[i]
        load_info.append(abs(info1-info2), a, b)

load_info.sort()

# 크루스칼 알고리즘
result = 0
for info in load_info:
    cost, a, b = info

    # 사이클 발생이 없는 경우에만 집합에 포함
    if find(parent, a) != find(parent, b):
        union(parent, x, y, z)
        result += cost

print(result)