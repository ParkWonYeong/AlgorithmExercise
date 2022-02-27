## 13913

from collections import deque
import sys
input = sys.stdin.readline

n,k = map(int, input().split())     # 수빈의 위치 N, 동생의 위치 K
cnt = [0]*100001
move = [0]*100001

def bfs(x):
    q = deque([x])
    while q:
        x = q.popleft()
        if x==k:
            print(cnt[x])
            ans = []
            # path에 저장된 경로 값을 통해 거슬러 올라가며 저장
            while x != n:
                ans.append(x)
                x = move[x] # x값을 move에 입력한다.
            ans.append(n)   # n 값을 ans에 append한다.
            ans.reverse()   # 역순으로 저장되어 있으므로 순서를 reverse한다.
            print(' '.join(map(str, ans)))
            return
        for i in (x-1, x+1, x*2):
            if 0 <= i <= 100000 and not cnt[i]:  # 값이 0보다 크거나 같고 최대값보다 작은데 방문하지 않은 경우
                cnt[i] = cnt[x]+1   # cnt값을 +1 해준다.
                move[i] = x         # 최종 경로 출력 시 i번째 값을 통해 이전위치를 알아낼 수 있도록 저장함
                q.append(i)

bfs(n)

# 46908KB, 180ms