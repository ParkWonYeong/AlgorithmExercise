## 2798

import sys

n,m = map(int, sys.stdin.readline().split())    # 카드 개수 N, 최대수 M 받아오기

# 카드에 쓰여있는 수 받아오기
card = list(map(int, sys.stdin.readline().split()))

ans,total = 0,0
# 합이 M을 넘지 않으면서 최대한 가까운 값이 되는 카드 3장의 합을 출력한다.
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            total = card[i] + card[j] + card[k]
            if total <= m:        # 최초의 경우 ans값에 total값을 넣어준다.
                ans = max(ans, total)
            elif (total > m):   # 세 합이 M 값을 초과하면 넘어가서 다음 반복을 실행한다.
                continue

print(ans)