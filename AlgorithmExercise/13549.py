## 13549

from collections import deque
import sys
input = sys.stdin.readline

n,k = map(int, input().split())     # 수빈의 위치 N, 동생의 위치 K
cnt = [0]*100001
visit = [0]*100001

# 1697번처럼 cnt로만 진행했을 경우 시간초과가 떴다. 따라서 방문을 확인하기 위한 배열을 하나 만들었다.

def bfs(x):
    q = deque([x])
    visit[x] = 1
    while q:
        x = q.popleft()
        if x==k:
            return cnt[x]
        for i in (x-1, x+1, x*2):    # 걷는 경우: +1 또는 -1만큼 이동한다. 순간이동: *2만큼 이동한다.
            if 0 <= i <= 100000 and visit[i]==0:  # 값이 0보다 크거나 같고 최대값보다 작은데 방문하지 않았다면
                visit[i] = 1
                if i == x*2:
                    cnt[i] = cnt[x] # 순간이동은 0초만에 이루어진다.
                    q.appendleft(i) # appendleft로 가장 앞으로 넘겨준다 
                else:
                    cnt[i] = cnt[x]+1   # cnt값을 +1 해준다.
                    q.append(i)
print(bfs(n))