## 9095

import sys
input = sys.stdin.readline

# 1 + a(n-1) / 2 + a(n-2) / 3 + a(n-3) ... 일 때가 a(n)이 나오는 경우의 수가 된다.
# 1,2,3을 이용해 만드는 경우의 수이므로 1,2,3에 대한 dp는 미리 만들어둔다.
dp = {
    1:1,    # 1 = 1
    2:2,    # 2 = 1+1, 2
    3:4     # 3 = 1+1+1, 1+2, 2+1, 3
}

def sol(x):
    if x not in dp:     # 1,2,3이 아닌 경우
        dp[x] = sol(x-1) + sol(x-2) + sol(x-3)
    return dp[x]

t = int(input())    # 테스트 케이스의 개수 T
for _ in range(t):
    n = int(input())
    print(sol(n))

# 30864KB, 72ms