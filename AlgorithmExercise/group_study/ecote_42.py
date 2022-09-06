## 탑승구

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

# input
g = int(input())    # gate 개수
p = int(input())    # plane 개수
plane = []
for _ in range(p):
    plane.append(int(input()))

# 부모 초기값
parent = [i for i in range(n+1)]
ans = 0

for i in plane:
    x = find(parent, i)
    
    # 어떠한 탑승구에도 도킹할 수 없는 비행기가 나오는 경우
    if x == 0:
        break   # 그 시점에서 공항의 운행 중지
    else:
        union(parent, x, x-1)
        ans += 1

print(ans)