## 2675

import sys

t = int(sys.stdin.readline())               # 테스트 케이스의 개수

for _ in range(t):                          # t만큼 반복
    ans = ''
    r, s = sys.stdin.readline().split()     # 반복할 횟수와 그 문자열
    r = int(r)
    for i in s:
        for j in range(r):
            ans += i
    print(ans)

# 30860KB, 64ms