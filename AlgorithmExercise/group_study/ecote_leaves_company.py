### 퇴사
# 다이나믹 프로그래밍

import sys
input = sys.stdin.readline

N = int(input())     # 퇴사 전까지 남은 날(일)
t = []               # 상담을 완료하는데 걸리는 기간
p = []               # 상담을 했을 때 받는 금액

dp = [0]*(N+1)

# 정보 받아오기
for _ in range(N):
    time,money = map(int, input().split())
    t.append(time)
    p.append(money)
    
# 뒷차례인 N-1번째(마지막날)부터 역순으로 작업 반복
for i in range(N-1, -1, -1):
    if t[i]+i > N:          # 상담 완료 기간이 퇴사일을 넘어서는 경우
        dp[i] = dp[i+1]     # 갱신 불가하므로 dp[i]값에 이전의 최댓값을 넣어준다
    else:
        # (N+1번째날 기준 수익)과 (N번째날 수익+Tn만큼 지난 후 수익)중 큰 값 고르기
        dp[i] = max(dp[i+1], p[i]+dp[t[i]+i])

# 이런식으로 반복해서 최댓값을 갱신하며 최종적으로 dp[0]값을 출력하면 된다.
print(dp[0])