## 10870

dp = [0]*21
dp[0],dp[1] = 0,1

n = int(input())
if n <= 1:
    print(dp[n])
else:
    for i in range(2, n+1):
        dp[i] = dp[i-1]+dp[i-2]
    print(dp[n])

# 30864KB, 72ms