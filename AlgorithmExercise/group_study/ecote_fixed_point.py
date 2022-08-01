## 고정점 찾기

import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
# binary search
start, end, ans = 0, n-1, -1
while start <= end:
    mid = (start+end) // 2
    if num[mid] == mid:
        ans = mid
        break
    else:
        if num[mid] > mid:
            end = mid-1
        else:
            start = mid + 1

print(ans)