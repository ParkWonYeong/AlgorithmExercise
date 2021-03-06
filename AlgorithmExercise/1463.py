## 1463

# dp 문제. 앞에서 구한 결과값을 저장하였다가 후에 사용한다.
n = int(input())
dp = [0]*(n+1)

for i in range(2, n+1):             # 2 이상부터 횟수를 고려한다.
    dp[i] = dp[i-1] + 1             # 각 i번째에 숫자 i-1 부여

    if i%3 == 0:
        # 3으로 나누어떨어지는 경우, i번째와 i//3번째+1 중 최솟값을 선택한다.
        dp[i] = min(dp[i], dp[i//3]+1)
    if i%2 == 0:
        # 2로 나누어떨어지는 경우, i번째와 i//2번째+1 중 최솟값을 선택한다.
        dp[i] = min(dp[i], dp[i//2]+1)

print(dp[n])