## 14501

# dynamic programming 기법을 사용한다.
# 이 기법은 뒤부터 계산을 한다.
# (N+1번째날 기준 수익)과 (N번째날 수익+Tn만큼 지난후 수익) 중 큰 값.

import sys
input = sys.stdin.readline

N = int(input())
t = []      # 상담을 완료하는데 걸리는 기간
p = []      # 상담을 했을 때 받는 금액

dp = [0 for _ in range(N+1)]

for _ in range(N):
    a,b = map(int, input().split())
    t.append(a)
    p.append(b)
    
# N-1번째부터 역순으로 작업 반복
for i in range(N-1, -1, -1):
    if t[i]+i > N:      # 퇴사일을 넘어선 기간일 경우
        dp[i] = dp[i+1] # dp[i]값에 이전의 최댓값을 넣어준다
    else:
        # (N+1번째날 기준 수익)과 (N번째날 수익+Tn만큼 지난 후 수익)중 큰 값 고르기
        dp[i] = max(dp[i+1], p[i]+dp[t[i]+i])
# 이런식으로 반복해서 최댓값을 넣어주고 최종적으로 dp[0]값을 출력하면 된다.
print(dp[0])

# 참고: https://pacific-ocean.tistory.com/199
# 30864KB, 72ms