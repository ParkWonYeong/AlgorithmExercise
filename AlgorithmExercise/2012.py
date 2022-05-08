## 2012

import sys
input = sys.stdin.readline

n = int(input())

grade = list(int(input()) for _ in range(n))
grade.sort()

ans = 0
for i in range(n):
    ans += abs(grade[i]-(i+1))

print(ans)

## 52192KB, 520ms