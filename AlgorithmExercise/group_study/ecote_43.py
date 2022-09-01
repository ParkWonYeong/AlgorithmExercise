## 어두운 길

# N개의 집과(0~N-1번째) M개의 도로
# 특정 도로의 가로등을 하루동안 켜기 위한 비용 = 해당 도로의 길이
# 임의의 두 집에 대해 가로등이 켜진 도로만으로도 오갈 수 있도록 만들고자 함.(비용 최소화)

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

n,m = map(int, input().split())     # 집의 수 N, 도로의 수 M
parent = [i for i in range(n+1)]
result = 0

load_info = []
for i in range(m):
    x,y,z = map(int, input().split())
    load_info.append([x,y,z])

load_info.sort(key=lambda x:x[2])   # 비용순 오름차순 정렬
total_cost = 0

for idx in load_info:
    x, y, cost = idx
    total_cost += cost
    # 사이클 발생이 없는 경우에만 집합에 포함
    if find(parent, x) != find(parent, y):
        union(parent, x, y)
        result += cost

print(total_cost - result)