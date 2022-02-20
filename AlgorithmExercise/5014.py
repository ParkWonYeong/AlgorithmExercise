## 5014

from collections import deque
import sys
input = sys.stdin.readline

# F: 가장 높은 층 / S: 현재 서있는 층 / G: 목표 층 / U: UP / D: DOWN
# 건물은 1층부터 시작한다.
f,s,g,u,d = map(int, input().split())

visit = [0]*(f+1)
cnt = [0]*(f+1)

# 방문했던 층을 또 방문하면 최솟값을 구하기 어렵다.
# 따라서 방문했던 층 외의 층을 탐색하며 G층에 도달하도록 bfs를 이용한다.
def bfs(s):
    q = deque([s])
    visit[s] = 1
    while q:
        s = q.popleft()
        if s == g:          # 현재 G층일 경우
            return cnt[g]   # cnt[g]값으로 간다.
        for i in (s+u, s-d):    # U만큼 위로 or D만큼 아래로 이동한다.
            if 0 < i <= f and not visit[i]: # 값이 0보다 크고 f(최고층)보다 작은데 방문하지 않은 곳이면
                visit[i]=1  #방문표시 해주고
                cnt[i] = cnt[s]+1   # cnt값을 +1해준다.
                q.append(i)
    if cnt[g] == 0:         # cnt[g]=0은 이동할 수 없다는 의미가 된다.
        return "use the stairs"

# S층에서 G층으로 가기 위해 눌러야하는 버튼의 수의 최솟값을 출력한다.
# 이동할 수 없을 경우 "use the stairs"를 출력한다.
print(bfs(s))

# 78376KB, 848ms