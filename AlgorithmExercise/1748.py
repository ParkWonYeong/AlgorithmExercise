## 1748

# n = int(input())
# ans = ''
# for i in range(n):
#     ans += len(str(i+1))

# print(ans)


## 위의 방법은 시간초과에 걸림.

# 수의 범위->총자릿수
# 1*9 + 2*90 + 3*900 + 4*9000
# 10과 자릿수가 곱해져서 개수를 센다.

import sys
input = sys.stdin.readline

n = input()
ans = 0

# m 자릿수 전까지인 m-1 자릿수를 모두 계산한 뒤
for i in range(len(n)-1):
    ans += 9 * (10**i) * (i+1)
    print(ans)

# 남은 최고 자릿수 계산을 더한다.
# (최고 자릿수에 남은 숫자 개수) * (자릿수)
ans += ((int(n) + 1 - (10**(len(n)-1)))) * len(n)
print(ans)