## 그리디 실전문제 3 - 큰 수의 법칙
# 주어진 수들을 M번 더해 가장 큰 수를 만드는 법칙.
# 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과해 더할 수 X

import sys
input = sys.stdin.readline

n,m,k = map(int, input().split())
# k: 큰 수 더하는 횟수
# m: 큰수 k번 더하는 횟수와 두번째로 큰수 한번 더하는 횟수
num = list(map(int, input().split()))
num.sort(reverse=True)

ans = 0
for i in range(m):
    for j in range(k):
        if m==0:
            break
        ans += num[0]   # 가장 큰수 K번 더하기
        m -= 1
    if m==0:
        break
    ans += num[1]   # 두번째로 큰수 더하기
    m -= 1

print(ans)

