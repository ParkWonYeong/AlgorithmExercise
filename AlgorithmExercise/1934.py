## 1934

from math import gcd
import sys
input = sys.stdin.readline

t = int(input())
i=0
while (i<t):
    x,y = map(int, input().split())
    ans = x*y//gcd(x,y)       # 최소공배수 = 두 수의 곱에서 두 수의 최대 공약수를 나누어 준 값과 같다.
    print(ans)
    i += 1

# 32972KB, 68ms