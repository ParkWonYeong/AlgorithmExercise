## 2846

# 오르막길, 내리막길, 평지. 가장 큰 오르막길의 크기를 구하려한다.
# 측정한 높이는 길이가 N인 수열로 나타낼 수 있다.
# 여기서 오르막길은 적어도 2개의 수로 이루어진 높이가 증가하는 부분 수열
# 1 2 [3 5 7 10] 6 [1 11] <= 이 길에는 2개의 오르막길이 있다.
# 첫번째 오르막길 크기는 (5-3)+(7-5)+(10-7) = 7이고, 두번째 오르막길 크기는 11-1 = 10이다

import sys
input = sys.stdin.readline

n = int(input())    # 상근이가 측정한 높이의 수이자 수열의 크기
m = []

p = list(map(int, input().split()))
min = 0     # 오르막길의 시작지점을 min에 저장한다.

# 가장 큰 오르막길의 크기를 출력하고, 오르막길이 없는 경우 0을 출력한다.

for i in range(n-1):
    if i == 0 and p[i]<p[i+1]:  # 처음부터 오르막길인 경우
        min = p[i]
    elif i>0 and p[i]<p[i+1] and p[i]<=p[i-1] and min==0:   # 처음 아닌 곳에서 오르막길 시작
        min = p[i]
    elif i>0 and p[i]>=p[i+1] and p[i]>p[i-1] and min!=0:   # 오르막길이 끝난 경우
        m += [p[i]-min]
        min = 0
    elif i == n-2 and p[i]>p[i-1] and min!=0 and p[i]<=p[i+1]:  # 끝나가는 부분이 오르막길로 끝나면
        m += [p[i+1]-min]

if m == []:
    print(0)
else:
    ans = m[0]
    for i in range(len(m)):
        if ans<m[i]:
            ans = m[i]
    print(ans)