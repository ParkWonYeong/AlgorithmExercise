## 효율적인 화폐구성

n,m = map(int, input().split())

coin = []
for i in range(n):
    coin.append(int(input()))

dp = [10001]*(m+1)
dp[0] = 0

for i in range(1, m+1):
    
    # 원하는 금액에 해당하는 동전이 있는 경우
    if i in coin:
        dp[i] = 1       # 동전 하나가 최소개수

    for j in coin:
        # dp 기록이 된 경우(10001이 아닌경우)
        if i >= j:
            # +1: 가장 최소화된 개수에서 +1
            dp[i] = min(dp[i], dp[i-j]+1)

if dp[m] != 10001:
    print(dp[m])
else:           # 불가능하면 -1 출력
    print(-1)