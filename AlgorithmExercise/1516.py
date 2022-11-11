## 게임 개발
# 이코테 '커리큘럼' 문제와 유사.

from collections import deque
import copy
import sys
input = sys.stdin.readline

def topology_sort():
    result = copy.deepcopy(time)
    q = deque()

    # 먼저 지어야 하는 건물 없이 곧바로 지을 수 있는 건물
    for i in range(1, n+1):
        if sub_build[i] == 0:
            q.append(i)

    while q:
        build = q.popleft()
        # 짓고 있는 건물이 사전에 지어야 하는 건물인 곳에서 sub_building 값 빼주기
        for i in graph[build]:
            result[i] = max(result[i], result[build]+time[i])
            sub_build[i] -= 1

            if sub_build[i] == 0:
                q.append(i)

    for j in range(1, n+1):
        print(result[j])

n = int(input())

sub_build = [0]*(n+1)
graph = [[] for _ in range(n+1)]    # 제일 긴 건설 시간을 담을 배열
time = [0]*(n+1)

for i in range(1, n+1):
    building = list(map(int, input().split()))
    time[i] = building[0]       # 각 건물을 세우는데 걸리는 시간
    
    for j in building[1:-1]:
        sub_build[i] += 1       # 먼저 지어야 하는 건물 개수
        graph[j].append(i)

topology_sort()