## 커리큘럼

# 선수 강의가 있는 강의는 선수 강의를 먼저 들어야 해당 강의를 들을 수 있다.

from collections import deque
import copy
import sys
input = sys.stdin.readline

n = int(input())        # 듣고자 하는 강의의 수(= 노드 개수)

# 노드에 대한 배열
indegree = [0]*(n+1)

# 간선 정보에 대한 값, 즉 가장 긴 강의 시간을 담을 배열
graph = [[] for _ in range(n+1)]


# 강의시간 정보를 담을 배열
time = [0]*(n+1)
for i in range(1,n+1):
    # 각 강의 시간과 들어야하는 선수 강의들. 끝은 -1을 출력
    # 몇 개의 선수강의가 있을지 모르기 때문에 변수 자체가 아닌 list로 받음.
    curri = list(map(int, input().split()))
    time[i] = curri[0]      # 맨 첫번째 원소는 강의 시간.
    
    for j in curri[1:-1]:   # -1이 나오기 직전까지 반복
        indegree[i] += 1    # 선수 강의 개수 갱신
        graph[j].append(i)


def topology_sort():    # 위상 정렬

    result = copy.deepcopy(time)
    q = deque()       # 빠른 처리를 위해 deque

    for i in range(1, n+1):
        if indegree[i] == 0:    # 선수 강의가 없는 강의
            q.append(i)

    while q:
        present = q.popleft()      # 강의를 듣는다.
        # 빼낸 강의와 연결된 노드들의 indegree 값에서 -1씩 빼기
        # 즉, 선수 강의를 들었으므로 indegree 값이 줄어든다.
        for i in graph[present]:
            result[i] = max(result[i], result[present] + time[i])
            indegree[i] -= 1

            # 반복된 과정에서 indegree 값이 0이 된 경우에는 이를 큐에 삽입
            if indegree[i] == 0:    # 선수 강의를 다 들은 강의
                q.append(i)
    
    # 위상 정렬 수행 결과
    for i in range(1,n+1):
        print(result[i])

topology_sort()