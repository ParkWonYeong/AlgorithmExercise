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
n_len = len(n)-1    # 문자열이므로 길이가 +1 되기 때문에 상쇄를 위해 -1해준다.
ans = 0

# m 자릿수 전까지인 m-1 자릿수를 모두 계산한 뒤
for i in range(n_len-1):
    ans += 9 * (10**i) * (i+1)

# 남은 최고 자릿수 계산을 더한다.
# (최고 자릿수에 남은 숫자 개수) * (자릿수)
ans += ((int(n) + 1 - (10**(n_len-1)))) * (n_len)
print(ans)