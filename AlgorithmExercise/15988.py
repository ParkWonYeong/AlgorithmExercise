## 15988

# 정수 n을 1,2,3의 합으로 나타내는 방법의 수

import sys
sys.setrecursionlimit(10**6)

dp = [0]*1000001
dp[0],dp[1],dp[2] = 1,2,4
dic={
    1:1,
    2:2,
    3:4
}

def sol(x):
    if x not in dic:     # 1,2,3이 아닌 경우
        dp[x-1] = sol(x-1)+sol(x-2)+sol(x-3)
    return dp[x-1]

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    print(sol(n)%1000000009)

# 위와 같은 방법으로 하니 시간초과.

import sys
sys.setrecursionlimit(10**6)

dp = [0]*1000001
dp[0],dp[1],dp[2] = 1,2,4

def sol(x):
    if x > 3:     # 1,2,3이 아닌 경우
        dp[x-1] = sol(x-1)+sol(x-2)+sol(x-3)
    return dp[x-1]

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    print(sol(n)%1000000009)

# dic을 사용해서 시간초과가 일어난 것인지 알아보기 위해 x>3으로 두었으나
# 역시 시간초과 발생. return 값을 반환하는 시간을 줄이려 sol 함수 사용x

import sys
sys.setrecursionlimit(10**6)

dp = [0]*1000001
dp[0],dp[1],dp[2] = 1,1,2

for i in range(3,1000001):
    dp[i] = dp[i-1]+dp[i-2]+dp[i-3]


t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    print(int(dp[n]) % 1000000009)

# 이번에는 메모리가 초과됐다.
# for문을 거듭할수록 dp값이 커져 그런 것같다.
# 두번째 for문 내에 위의 for문을 넣으면 시간초과가 떴다.

import sys
sys.setrecursionlimit(10**6)

dp = [0]*1000001
dp[0],dp[1],dp[2] = 1,1,2

# while문을 넣어봤으나 for문을 사용했을 때 속도가 더 빨랐다.
for i in range(3,1000001):
    dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
    dp[i] %= 1000000009

for _ in range(int(sys.stdin.readline())):
    print(dp[int(sys.stdin.readline())])

# 시간을 단축 시키기위해 sys를 사용하고 setrecursionlimit을 작성해주었으며,
# t,n 부여를 변수 선언없이 곧바로 입력에 넣었다.

# 70420KB, 604ms