## 여행계획

# 크루스칼 알고리즘 사용

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

n,m = map(int, input().split())     # 여행지 수 N, 여행 계획 도시 수 M
parent = [i for i in range(n+1)]

for i in range(1,n+1):
    arr = list(map(int, input().split()))
    for j in range(n):
        if arr[j]==1:   # 연결된 경우
            union(parent, i, j+1)

plan = list(map(int, input().split()))

result = True

for i in range(m-1):

    # 사이클 발생이 없는 경우에만 집합에 포함
    if find(parent, plan[i]) != find(parent, plan[i+1]):
        result = False

if result:
    print("YES")
else:
    print("NO")