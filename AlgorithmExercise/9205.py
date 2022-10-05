## 맥주 마시면서 걸어가기

# 맥주 한 박스 가지고 출발(한 박스당 20병), 50미터당 하나씩 마신다.
# 편의점에 들렀을 때 빈병을 버리고 새 맥주병을 채울 수 있다.(20개까지만 가능)
# 편의점 나선 직후부터도 50미터 가기 전에 맥주 한병 마셔야함
# 페스티벌 도착까지 맥주를 마시며 갈수있으면 "happy"/ 가면서 맥주가 바닥나 이동할 수 없으면 "sad"

### bfs ###
from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    q = deque()
    q.append(graph[0])
    print(q)
    
    while q:
        x,y = q.popleft()

        # 맨헤튼 거리 구하기(20*50 = 1000미터)
        if abs(x - graph[-1][0]) + abs(y - graph[-1][1]) <= 1000:
            print("happy")
            return
        
        for i in range(n):
            print(abs(x - graph[i+1][0]) + abs(y - graph[i+1][1]))
            if visited[i] == 0:
                if abs(x - graph[i+1][0]) + abs(y - graph[i+1][1]) <= 1000:
                    q.append(graph[i+1])      # 출발 좌표를 편의점 위치로 갱신
                    visited[i] = 1

    print("sad")
    return

t = int(input())        # 테스트 케이스 개수

for i in range(t):
    n = int(input())    # 맥주를 파는 편의점 개수
    graph = []
    visited = [0 for _ in range(n+1)]

    # 집(출발점) 좌표
    graph.append(list(map(int, input().split())))
    
    # 편의점 좌표
    for j in range(n):
        graph.append(list(map(int, input().split())))
    
    # 페스티벌 좌표
    graph.append(list(map(int, input().split())))
        
    bfs()


### 플로이드 워샬 <=== 아직 수정중

def floyd():

    # 맨헤튼 거리 계산해서 이동 가능하면 1
    for m in range(n):
        for l in range(n):
            a,b = graph[m+1]
            c = abs(a)+abs(b)
            if c <= 1000:
                graph_f[m][l] = 1

    # 플로이드 워셜 알고리즘 수행
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph_f[i][k] and graph_f[k][j]:
                    graph_f[i][j] = 1

    print(graph_f)
    return graph_f[-2][-2]


t = int(input())        # 테스트 케이스 개수

for i in range(t):
    n = int(input())    # 맥주를 파는 편의점 개수
    graph = []

    # 집(출발점) 좌표
    graph.append(list(map(int, input().split())))
    
    # 편의점 좌표
    for j in range(n):
        graph.append(list(map(int, input().split())))
    
    # 페스티벌 좌표
    graph.append(list(map(int, input().split())))

    graph_f = [[0]*(n+1) for _ in range(n+1)]

    print("happy" if floyd() else "sad")