### 선수과목

n,m = map(int, input().split())
time = [1]*(n+1)
graph = [[] for _ in range(n+1)]
pre_subject = [0]*(n+1)

for i in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)

for j in range(1, n+1):
    for k in graph[j]:
        time[k] = max(time[k], time[j]+1)

print(*time[1:])