## 11659

import sys
input = sys.stdin.readline

# 누적합(prefix sum)을 미리 구해둔 다음 (j-1번째)-(i-2번째)을 꺼내 쓰면 된다. 
n,m = map(int, input().split())
num = list(map(int, input().split()))
total = [num[i] for i in range(n)]          # 미리 sum을 구할 배열 

for i in range(1,n):
    total[i] = total[i-1]+num[i]

for _ in range(m):
    a,b= map(int, input().split())
    if a==1:
        print(total[b-1])
    else:
        print(total[b-1]-total[a-2])