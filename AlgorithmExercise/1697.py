## 1697

from collections import deque
import sys
input = sys.stdin.readline

n,k = map(int, input().split())     # 수빈의 위치 N, 동생의 위치 K
cnt = [0]*100001

# 방문 탐색을 위해 visit = [0]*100001 도 있어야 한다고 생각했으나, cnt로 해결 가능하여 생략했다.

def bfs(x):
    q = deque([x])
    while q:
        x = q.popleft()
        if x==k:            # 동생을 찾은 경우
            return cnt[x]   # cnt[x]값으로 간다.
        for i in (x-1, x+1, x*2):    # 걷는 경우: +1 또는 -1만큼 이동한다. 순간이동: *2만큼 이동한다.
            if 0 <= i <= 100000 and not cnt[i]:  # 값이 0보다 크거나 같고 최대값보다 작은데 방문하지 않았다면
                cnt[i] = cnt[x]+1   # cnt값을 +1 해준다.
                q.append(i)
print(bfs(n))