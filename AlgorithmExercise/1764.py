## 1764

import sys
input = sys.stdin.readline

n,m = map(int, input().split())

nolisten,nosee = set(),set()
for _ in range(n):
    nolisten.add(input().rstrip())
for _ in range(m):
    nosee.add(input().rstrip())

# 교집합을 이용한다.
ans = list(nolisten&nosee)
ans.sort()
print(len(ans))
print('\n'.join(ans))

## 42108KB, 120~124ms