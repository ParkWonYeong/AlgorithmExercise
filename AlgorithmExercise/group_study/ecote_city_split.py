## 도시분할계획

# N개의 집과 그 집들을 연결하는 M개의 길(양방향 가능), 각각의 길은 유지비 존재
# 마을을 각각의 분리된 2개의 마을로 분할할 계획중.

# 조건
# 분리 시 각 마을 안의 집들은 서로 연결되어야 함. 즉, 한 팀이 되어 두 팀으로 나누어져있어야 함.
# 각 팀에는 하나의 집 이상이 존재해야함.

# 마을 내의 길은 유지하면서 드는 최소 비용 계산하기

# 크루스칼 알고리즘 : 최소 신장 트리에 포함되는 간선 중 가장 비용이 큰 간선을 제거한다.
# 그렇게 되면 최소 신장 트리가 2개의 부분 그래프로 나누어지며 문제가 요구하는 해를 만족한다.
# (그림을 그려가며 더 공부해봐야겠습니다)


import sys
input = sys.stdin.readline

# 팀 결성 문제와 유사
def find(town, x):
    if town[x] != x:
        town[x] = find(town, town[x])
    return town[x]

def merge(town, i, j):
    i,j = find(town,i), find(town,j)

    if i>j:
        town[i] = j
    else:
        town[j] = i

### main ###

n,m = map(int, input().split())

town = [i for i in range(n+1)]
cost = 0
calculate = []

for _ in range(m):
    # (a,b,c) : 집a와 집b를 연결하는 길의 유지비 c
    a,b,c = map(int, input().split())
    calculate.append([a,b,c])


# 크루스칼 알고리즘에 대한 공부가 부족하여 이 부분은 답안 참고
calculate.sort(key=lambda x:x[2])   # 비용순 오름차순 정렬
largest = 0                     # 최소 신장 트리 중 가장 비용 큰 간선을 담을 변수

for cal in calculate:
    a,b,c = cal
    # 사이클 발생이 없는 경우에만 집합에 포함 <- ???
    if find(town, a) != find(town, b):      # 소속이 다를 경우
        merge(town, a, b)                   # 소속 합침
        cost += c                           # 합친 소속 내에선 길이 있어야하므로 비용 합하기
        largest = c

print(cost-largest)