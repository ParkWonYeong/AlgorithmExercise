## 실전문제 : 큰 수의 법칙

import sys
input = sys.stdin.readline

# 배열의 크기 N, 숫자가 더해지는 횟수 M, 특정 번호가 연속해서 K번 초과해서 더해질 수 없음
n,m,k = map(int, input().split())   # K <= M
num = list(map(int, input().split()))
num.sort()

ans = 0

while 1:
    for i in range(k):  # 가장 큰 수 k번 더하기
        if m == 0:
            break
        ans += num[-1]
        m -= 1

    if m == 0:          # 그다음 큰 수 더하기
        break
    ans += num[-2]
    m -= 1

    # 이후 다시 연속해서 큰 수 K번 더하고 반복

print(ans)