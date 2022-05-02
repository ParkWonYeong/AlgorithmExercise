## 1205

import sys
input = sys.stdin.readline
n,score,p = map(int,input().split())

if n == 0:
    print(1)

else:
    rank = list(map(int,input().split()))
    if n >= p and rank[-1] >= score:
        print(-1)
    else:
        i = 0
        ans = n+1
        for i in range(n):
            if rank[i] <= score:
                ans = i+1
                break
        print(ans)

# 30840KB, 68ms