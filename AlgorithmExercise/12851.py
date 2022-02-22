## 12851

from collections import deque
import sys
input = sys.stdin.readline

n,k = map(int, input().split())     # 수빈의 위치 N, 동생의 위치 K
cnt = [0]*100001
visit = [0]*100001                  # 가장 빠른 방법의 가지 수를 찾기 위해 방문 기록을 갱신한다.

def bfs(x):
    q = deque([x])
    visit[x] = 1
    while q:
        x = q.popleft()
        if x==k:                        # 동생을 찾은 경우
            print(cnt[x])               # 최단 시간을 출력하고
            print(visit[x])             # 최단 시간으로 동생을 찾는 방법의 수를 출력한다.
        for i in (x-1, x+1, x*2):
            if 0<=i<=100000:            # 이번엔 세부 조건을 두가지로 나눠준다.
                # 처음으로 접근한 경우의 수일 경우
                if visit[i]==0:
                    cnt[i] = cnt[x]+1
                    visit[i] = visit[x]
                    q.append(i)

                # 이전에 알아낸 경우의 수일 경우 
                elif cnt[i] == cnt[x]+1:
                    visit[i] += visit[x]    # 최단시간으로 찾은 방법의 수를 +1 해준다.

bfs(n)

# 35552KB, 172ms