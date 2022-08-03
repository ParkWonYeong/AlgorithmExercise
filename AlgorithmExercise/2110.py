## 2110
## 공유기 설치

import sys
input = sys.stdin.readline

n,c = map(int, input().split())
router = []
for i in range(n):
    router.append(int(input()))
router.sort()

ans = 0
start, end = 0, n-1
# start: 공유기사이 최소거리 / end: 공유기사이 최대거리
while start <= end:
    if c == 2:
        ans = router[-1] - router[0]
        break

    mid = (start+end) // 2      # 공유기 사이의 거리
    cnt = 1
    now = router[0]
    for i in range(1, len(router)):
        if router[i] >= now + mid:
            now = router[i]
            cnt += 1            # 공유기 설치 횟수 +
    
    if cnt >= c:        # 설치횟수가 C 이상이라면
        start = mid+1   # Up
        ans = mid       # 최대 값으로 갱신
    
    else:               # 아직 설치가 덜됐다면
        end = mid-1

print(ans)