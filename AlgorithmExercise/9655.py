## 돌 게임

# N이 3 이하의 홀수일 때를 생각하면 먼저 게임을 시작하는 상근이가 반드시 이긴다.
# 2인 경우에는 3개가 아닌 1개만 가져갈 수 있으므로 창영이가 이긴다.
# 그 외의 경우에도 홀수면 상근, 짝수면 창영이가 이긴다.

n = int(input())

if n % 2 == 0:
    print("CY")
else:
    print("SK")

# 사실 DP 문제로 출제된 것인데 게임이론으로 간단하게 풀 수 있다.

### DP 풀이 ###

n = int(input())
dp = [-1]*1001

# 1이 SK, 0이 CY
dp[1], dp[2], dp[3] = 1,0,1

for i in range(4, n+1):
    # 1개 또는 3개를 남기는 시점에서 승패가 갈린다.(앞에 남긴 사람이 진다.)
    if dp[i-1]==1 or dp[i-3]==1:
        dp[i] = 0
    else:
        dp[i] = 1

print("SK") if dp[n]==1 else print("CY")