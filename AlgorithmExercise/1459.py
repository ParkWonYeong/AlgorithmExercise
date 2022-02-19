## 1459

import sys
input = sys.stdin.readline

# (X,Y): 가고자 하는 위치, W: 한 블록 가는데 걸리는 시간, S: 대각선으로 한 블록을 가로지르는 시간
x,y,w,s = map(int, input().split())

# 평행으로만 이동할 경우 걸리는 시간은 (x+y)*w
m1 = (x+y)*w

# 대각선으로만 이동할 경우 걸리는 시간은 둘의 합이 짝수일 때 가능하며, max(x,y)*s
# 대각선+평행이동 '한번'인 경우 걸리는 시간은 둘의 합이 홀수일 때 가능하며, (max(x,y)-1)*s+w
# 따라서 짝수와 홀수에 따라 나눠 if 조건문을 사용한다.
if (x+y)%2 == 0:
    m2 = max(x,y)*s
else:
    m2 = (max(x,y)-1)*s+w

# 평행이동+대각선일 경우 걸리는 시간은 (min(x,y)*s)+(abs(x-y)*w)
# 작은 값 만큼만 대각선 이동을 하고 나머지에 대해 평행이동.
m3 = (min(x,y)*s)+(abs(x-y)*w)

# 이후 이 중에서 최솟값인 것을 출력해주면 된다.
ans = min(m1, m2, m3)

print(ans)